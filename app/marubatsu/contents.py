class Contents:
    def __init__(self):
        self.contents = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.field_data = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.mark = 1

    def put_mark(self, num):
        if self.mark == 1:
            self.contents[num] = '○'
            self.field_data[num] = 1
        else:
            self.contents[num] = 'x'
            self.field_data[num] = 2

    def turn_change(self):
        if self.mark == 1:
            self.mark = 2
        else:
            self.mark = 1

    def get_contents(self):
        return self.contents

    def get_field_data(self):
        data = list(self.field_data)
        return data

    def check_win(self):
        win = self.check_field(0, 1, 2) or \
              self.check_field(3, 4, 5) or \
              self.check_field(6, 7, 8) or \
              self.check_field(0, 3, 6) or \
              self.check_field(1, 4, 7) or \
              self.check_field(2, 5, 8) or \
              self.check_field(0, 4, 8) or \
              self.check_field(2, 4, 6)
        return win

    def check_same_place(self, num):
        if self.field_data[num] == 0:
            return False
        return True

    def check_finish(self):
        for i in self.field_data:
            if i == 0:
                return False
        return True

    def check_field(self, num1, num2, num3):
        if self.field_data[num1] == 0:
            return False
        win = self.field_data[num1] == self.field_data[num2] == self.field_data[num3]
        return win
