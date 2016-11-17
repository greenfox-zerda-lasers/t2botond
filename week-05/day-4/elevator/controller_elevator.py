# Create an elevator controller class
# It should take an user input by listening to user input
# List of commands:
#
#  - Move elevator up
#  - Move elevator down
#  - Add people
#  - Remove people
#
#  Features to implement:
#   - Always draw the state of the elevator as depicted in "art.txt"
#   - [ x ] is the elevator. X means it has at least 1 person inside
#   - Moving floors should take time
#   - don't move beyond limits
#
# Create the class with MVC pattern in mind. It should get and store data in the model object
# and it should pass the data to the view objects
import elevator_model
import elevator_display
import os

class Controller:

    def __init__(self):
        self.lift2 = elevator_model.Elevator()
        self.lift3 = elevator_display.Display()

    def Move_elevator_up(self):
        self.lift2.floorup()
        pass

    def Move_elevator_down(self):
        self.lift2.floordown()
        pass

    def Add_people(self):
        self.lift2.geton()
        pass

    def Remove_people(self):
        self.lift2.getoff()
        pass

    def events(self):
        self.move = True
        while self.move == True:
            os.system("clear")
            self.lift3.draw(10, self.lift2.floor, self.lift2.people)
            print("Up:u Down:d GetOn:n GetOff:f Quit:q")
            self.event = input()
            if self.event == "u":
                self.Move_elevator_up()
            elif self.event == "q":
                self.move = False
            elif self.event == "d":
                self.Move_elevator_down()
            elif self.event == "n":
                self.Add_people()
            elif self.event == "f":
                self.Remove_people()
            else:
                pass

lift1 = Controller()
lift1.events()
