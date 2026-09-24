#!/usr/bin/env python3
""" 
A program to output some results into a csv file
"""
# libraries and methods
from math import exp,pi

# let the user know whats happening
print("Opening file, outputing results to file")
# open a file to output some results
with open("results.csv", "w") as f:

    for i in range(0,101):
        x = i*0.01
        # do some calculations
        y = pi*x*exp(-x)
        # output to string and format if necessary
        str = f" {x} , {y} \n"
        f.write(str)
print("File output complete, file closed")


