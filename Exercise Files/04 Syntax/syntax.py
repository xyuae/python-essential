#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC
class Egg:
    def __init__(self, kind = "friend"):
        self.kind = kind

    def whatKind(self):
        return self.kind

def main():
    fried = Egg()
    scrambled = Egg('scrambled')
    print(fried.whatKind())


def main():
    print("This is the syntax.py file.")
    a = [1,2,3,4,5]
    a, b = 0, 1
    s = "less than" if a < b else "not less than"
    print(type(a), a)

if __name__ == "__main__": main()
