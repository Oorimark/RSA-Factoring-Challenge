#!/usr/bin/python3
import sys

def two_factors(n):
    for i in range(2, n):
        if n % i == 0:
            return [int(n / i), i]
            break


with open(sys.argv[1]) as file:
    rfile = file.read()
    for value in rfile.split():
         result = two_factors(int(value))
         print("{0}={1}*{2}".format(value, result[0], result[1]))

