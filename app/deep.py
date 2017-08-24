#!user/bin/env python
# coding:utf-8
import numpy as np
import chainer.functions as F
import chainer.links as L
from chainer import Variable, optimizers, serializers

from .my_chain import MyChain
from .settings import Settings

class Deep:
    def __init__(self):
        self.model = MyChain()
        # 確率的勾配降下法(Stocastic Gradient Descent)を使用
        self.opt = optimizers.SGD()
        self.opt.setup(self.model)
        self.models = []
        self.marks = []

    def save(self):
        serializers.save_npz('marubatsu.npz', self.model)

    def load(self):
        serializers.load_npz("marubatsu.npz", self.model)

    def get(self, field_data):
        x = Variable(np.array([field_data], dtype=np.float32))

        # 勾配を0に初期化
        self.model.zerograds()

        # 入力xを変換し出力yへ
        y = self.model(x)

        # print(x.data)
        # print(y.data)

        # 出力されたyを表示
        self.models.append(y)
        self.marks.append(self.max_value(y.data))
        return self.max_value(y.data)

    def learn(self, result):
        for i, y in enumerate(self.models):
            if result == Settings.SAME_PLACE and i == len(self.models) - 1:
                teacher = self.teacher(result, self.marks[i], y.data[0], True)
            else:
                teacher = self.teacher(result, self.marks[i], y.data[0], False)
            t = Variable(np.array([teacher], dtype=np.float32))

            # print(teacher)

            # 出力yと正解tとの差分を算出(平均二乗誤差)
            loss = F.mean_squared_error(y, t)

            # 逆伝播
            loss.backward()

            # 最適化
            self.opt.update()

            # 学んだらリセット
        del self.models[:]
        del self.marks[:]

    def max_value(self, data):
        return data.argmax()

    def teacher(self, result, mark, model, last_flg):
        data = []
        # win
        if result == Settings.WIN:
            for i in range(9):
                if i == mark:
                    data.append(1)
                else:
                    data.append(model[i])
        # lose
        elif result == Settings.LOSE:
            for i in range(9):
                if i == mark:
                    data.append(-1)
                else:
                    data.append(model[i])
        # same plase
        elif result == Settings.SAME_PLACE:
            if last_flg == True:
                for i in range(9):
                    if i == mark:
                        data.append(-2)
                    else:
                        data.append(model[i])
            else:
                for i in range(9):
                    data.append(model[i])
        # draw
        else:
            for i in range(9):
                if i == mark:
                    data.append(0)
                else:
                    data.append(model[i])
        return data
