#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : Class.py
# @Author: Frank
# @Date  : 4/21/2019


class Cat:
    """
    This is a cat class
    """
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("The cat %s like fish!" % self.name)

    def drink(self):
        print("The cat %s need water!" % self.name)


Tom = Cat("Tom")

Tom.drink()
Tom.eat()
print(Tom.name)

lazy_cat = Cat("Lazy_cat")
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat.name)
