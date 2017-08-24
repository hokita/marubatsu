import random

class Computer:
    def choose_num(self, field_data):
        select = []
        for i, data in enumerate(field_data):
            if data == 0:
                select.append(i)
        random.shuffle(select)
        return select[0]
