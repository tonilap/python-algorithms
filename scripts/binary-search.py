#!/usr/bin/env python

import sys

# O(log n)
# Best: O(1)
# Worst: O(log n)
def binary_search(list, number):
    
    low = 0
    high = len(list) - 1
    count = 1
    
    while(low <= high):
        x = (low+high)/2
        if(number == int(list[x])):
            return count
        elif(number < int(list[x])):
            high = x - 1
            count = count +1
        else:
            low = x + 1
            count = count +1
    
    return -1
    
if __name__ == '__main__':
    
    print("Enter a list of numbers separated by commas")
    text = sys.stdin.readline().replace("\n","")
    list = text.split(",")
    
    print("Enter a number to search")
    number = int(sys.stdin.readline())
    
    steps = binary_search(list, number)
    
    if(steps != -1):
        print("Number %d found. Number of steps: %d") % (number, steps)
    else:
        print("Number %d not found in list %s") % (number, text)
    
    