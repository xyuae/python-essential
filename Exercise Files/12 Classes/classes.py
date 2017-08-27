#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def bark(self):
        print('The duck cannot bark')

    def fur(self):
        pass

class Dog:
    def bark(self):
        print('Woof!')

    def fur(self):
        print('The dog has brown and white fur')

    def quack(self):
        pass

    def walk(self):
        pass

def main():
    donald = Duck()
    fido = Dog()
    donald.quack()
    donald.walk()
    


if __name__ == "__main__": main()
