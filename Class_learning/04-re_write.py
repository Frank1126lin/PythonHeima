#! /usr/bin/python3
# _*_ coding:utf-8 _*_

class Animals():
    # define the animals
    def eat(self):
        print("Eat!")
    
    def drink(self):
        print("Drink!")
    
    def run(self):
        print("Run!")

class Dog(Animals):
    # Dog come from Animals
    def bark(self):
        print("bark!")


class Xiaotianquan(Dog):
    # define xiaotianquan
    def run(self):
        # re-write the fun run
        print("Fly!")
        # recommed the method below to use the parent function.
        super().run()
        # python 2.X and 3.x still can use the method below.
        # Dog.run(self)
        print("are we done?")
    

xtq = Xiaotianquan()
xtq.eat()
xtq.run()
