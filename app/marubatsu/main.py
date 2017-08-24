from ..deep import Deep
from ..settings import Settings
from .show import Show
from .contents import Contents
from .command import Command
from .computer import Computer

class Main:
    def __init__(self):
        show = Show()
        command = Command()
        computer = Computer()
        deep = Deep()

        game_time = Settings.GAME_TIME
        data_time = Settings.DATA_TIME
        play_human = Settings.PLAY_HUMAN

        # init counter
        win = 0
        lose = 0
        draw = 0
        same_place = 0

        # deep.load()

        for i in range(game_time):
            contents = Contents()
            count = 1

            while True:
                if contents.mark == 1:
                    num = deep.get(contents.get_field_data())
                    if play_human:
                        print(num)
                else:
                    if play_human:
                        show.field(contents.get_contents())

                    if play_human:
                        num = command.get()
                    else:
                        num = computer.choose_num(contents.get_field_data())

                if(contents.check_same_place(num) == True):
                    if play_human:
                        show.field(contents.get_contents())
                        print("same_place")
                        print(count)
                    if i >= game_time - data_time:
                        same_place += 1
                    deep.learn(Settings.SAME_PLACE)
                    break

                contents.put_mark(num)

                if(contents.check_win() == True):
                    if play_human:
                        show.field(contents.get_contents())
                        print("{0} win".format(contents.mark))
                        print(count)
                    if contents.mark == 1:
                        if i > game_time - data_time:
                            win += 1
                        deep.learn(Settings.WIN)
                    else:
                        if i > game_time - data_time:
                            lose += 1
                        deep.learn(Settings.LOSE)
                    break
                elif(contents.check_finish() == True):
                    if play_human:
                        show.field(contents.get_contents())
                        print("draw")
                        print(count)
                    if i > game_time - data_time:
                        draw += 1
                    deep.learn(Settings.DRAW)
                    break

                contents.turn_change()
                count += 1

        print("win: {0}".format(win / data_time))
        print("lose: {0}".format(lose / data_time))
        print("draw: {0}".format(draw / data_time))
        print("same_place: {0}".format(same_place / data_time))

        # deep.save()
