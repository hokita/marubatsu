class Show:
    def line_a(self):
        print("     |     |     ")

    def line_b(self):
        print("-----+-----+-----")

    def line_1(self, contents):
        print("  {0}  |  {1}  |  {2}  ".format(contents[0], contents[1], contents[2]))

    def line_2(self, contents):
        print("  {0}  |  {1}  |  {2}  ".format(contents[3], contents[4], contents[5]))

    def line_3(self, contents):
        print("  {0}  |  {1}  |  {2}  ".format(contents[6], contents[7], contents[8]))

    def field(self, contents):
        self.line_a()
        self.line_1(contents)
        self.line_a()
        self.line_b()
        self.line_a()
        self.line_2(contents)
        self.line_a()
        self.line_b()
        self.line_a()
        self.line_3(contents)
        self.line_a()
        print("")

    def winner(self, winner):
        if winner == 0:
            print("you win!")
        else:
            print("you lose...")
