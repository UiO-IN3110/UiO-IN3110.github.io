#!/usr/bin/env python

class Car(object):
    """ A class representing a car """
    
    def __init__(self, year, fuel):
        self.year = year
        self.fuel = fuel
        self.speed = 0
    
    def start(self):
        if self.fuel == "electric":
            print("sssss")
        else:
            print("Wohmmm")
            
    def accelerate(self, new_speed):
        self.speed = new_speed
        

mycar = Car(2007, "bensin")

mycar.start(5)
