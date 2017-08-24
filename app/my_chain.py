from chainer import Link, Chain, ChainList
import chainer.functions as F
import chainer.links as L

class MyChain(Chain):
    def __init__(self):
        super(MyChain, self).__init__(
                l1 = L.Linear(9, 100),
                l2 = L.Linear(100, 9)
        )

    def __call__(self, x):
        h = F.leaky_relu(self.l1(x))
        o = self.l2(h)
        return o
