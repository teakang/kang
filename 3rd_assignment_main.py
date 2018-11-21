#########################################################################
# Date: 2018/10/02
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 3RD_ASSIGNMENT_CODE
    # Complete the code to perform Third Assignment
    # =======================================================================
    
    def car_startup(self):
        stop = True
        distance_detector = self.car.distance_detector.get_distance()
        line_detector = self.car.line_detector.read_digital()
        vRight = ([1,0,0,0,0],[1,1,0,0,0])
        rRight = [0,1,1,0,0]
        front = [0,0,1,0,0]
        rLeft = [0,0,1,1,0]
        vLeft = ([0,0,0,1,1],[0,0,0,0,1])
        nothing = [0,0,0,0,0]
        go_left = self.car.steering.turn(65)
        go_light = self.car.steering.turn(115)
        go_front = self.car.steering.turn(90)
        while(stop == True):
            user = input()
            if user == "wa" or user == "aw":
                self.car.steering.turn(65)
                self.car.accelerator.go_forward(self.car.SLOW)
                continue
            if user == "wd" or user == "dw":
                self.car.steering.turn(115)
                self.car.accelerator.go_forward(self.car.SLOW)
                continue
            if user == "w":
                self.car.steering.turn(90)
                self.car.accelerator.go_forward(self.car.SLOW)
                continue
            if user == "s":
                self.car.steering.turn(90)
                self.car.accelerator.go_backward(self.car.SLOW)
                continue
            if user == "sa" or user == "as":
                self.car.steering.turn(115)
                self.car.accelerator.go_backward(self.car.SLOW)
                continue
            if user == "sd" or user == "ds":
                self.car.steering.turn(65)
                self.car.accelerator.go_backward(self.car.SLOW)
                continue
            else:
                continue


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()