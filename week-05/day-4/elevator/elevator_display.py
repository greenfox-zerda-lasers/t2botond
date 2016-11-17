class Display:
    def top(self):
        print("___________________________________")
        print("`._______________________________.'")

    def floor(self):
        print("   || ||       || ||       || ||")

    def floor_fullift(self):
        print("   || || [ X ] || ||       || ||")

    def floor_emptylift(self):
        print("   || || [   ] || ||       || ||")

    def floor_emptyfloor(self):
        print("  _||_||_______||_||_______||_||_")
        print(".'_______________________________`.")

    def floor_liftfloor(self):
        print("  _||_||_[ X ]_||_||_______||_||_")
        print(".'_______________________________`.")


    def floor_liftemptyfloor(self):
        print("  _||_||_[   ]_||_||_______||_||_")
        print(".'_______________________________`.")


    def draw(self, height, floor, isempty):
        self.top()
        self.height = height
        self.state = floor
        self.isemp = isempty
        i = self.height
        for i in range(self.height):
            if i == self.height-self.state:
                if self.isemp == False:
                    self.floor_emptylift()
                else: self.floor_fullift()
            else:
                self.floor()
        if self.state == 0:
            if self.isemp == False:
                self.floor_liftemptyfloor()
            else:
                self.floor_liftfloor()
        if self.state != 0:
            self.floor_emptyfloor()
