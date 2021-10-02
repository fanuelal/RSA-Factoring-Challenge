#!/bin/usr/python3
import sys

fileName = sys.argv[1]
file = open(fileName, "r")
lines = file.readlines()

for line in lines:
    value = int(line)
    temp = 0
    for x in range(1,value):
        var = x + 1
        if value % var == 0:
            res = value / var
            res = int(res)
            print("{}={}*{}".format(value,res,var))
            break
file.close()
