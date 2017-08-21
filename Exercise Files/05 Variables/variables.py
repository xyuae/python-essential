#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    num = 43//3
    num  = { 'one': 1, 'two': 2}
    d = dict(
        one = 1, two = 2, three = 3, four = 4, five = 'five'
    )

    for k in sorted(d.keys()):
        print(k, d[k])
    print(type(num), num)

    print("This is the variables.py file.")

if __name__ == "__main__": main()
