# Gizzel Ruiz
# 02/23/2022
# This program takes an array and finds the low index, high index, and sum of a subarray.
# The array is hardcoded and shows an example using values from our textbook and an array
# of random values created by the program


import numpy as np
import random

# function to create list with random numbers
def createList(n):
    list = []
    for i in range(n+1):
        list.append(i)
    return ('      '.join(map(str, list)))

# funtion to determine difference between list values
def priceChanges(a):
    list = np.diff(a)
    return ('      '.join(map(str, list)))

# function to find max subarray by starting check from middle and working outwards
def findMaxSubarray(a, start, end):
    if start == end - 1:
        return start, end, a[start]
    else:
        mid = (start + end)//2
        leftStart, leftEnd, leftMax = findMaxSubarray(a, start, mid)
        rightStart, rightEnd, rightMax = findMaxSubarray(a, mid, end)
        crossStart, crossEnd, crossMax = findMaxCrossingSubarray(a, start, mid, end)
        if (leftMax > rightMax and leftMax > crossMax):
            return leftStart, leftEnd, leftMax
        elif (rightMax > leftMax and rightMax > crossMax):
            return rightStart, rightEnd, rightMax
        else:
            return crossStart, crossEnd, crossMax

# method to find max crossing subarray
def findMaxCrossingSubarray(a, start, mid, end):
    sumLeft = float('-inf')
    sumTemp = 0
    crossStart = mid
    for i in range(mid - 1, start - 1, -1):
        sumTemp = sumTemp + a[i]
        if sumTemp > sumLeft:
            sumLeft = sumTemp
            crossStart = i

    sumRight = float('-inf')
    sumTemp = 0
    crossEnd = mid + 1
    for i in range(mid, end):
        sumTemp = sumTemp + a[i]
        if sumTemp > sumRight:
            sumRight = sumTemp
            crossEnd = i + 1
    return crossStart, crossEnd, sumLeft + sumRight



if __name__ == '__main__':

    # code for test values from book
    print ('*************************************')
    print ('****   SAMPLE VALUES FROM BOOK   ****')
    print ('*************************************')
    print ('\n')
    testPrices = [100,113,110,85,105,102,86,63,81,191,94,106,101,79,94,90,97]
    print ('    Day:  ', createList(16))
    print (' - '*50)
    print ('  Price:  ', '     '.join(map(str, testPrices)))
    print ('Changes:         ', priceChanges(testPrices))
    print ('\n')
    start, end, maximum = findMaxSubarray(testPrices, 0, len(testPrices))
    print ('Low index: {} \nHigh index: {} \nMax sum: {}'.format(start, end - 1, maximum))

    print ('\n')
    print ('\n')

    # code for 100 random values generated
    print ('*************************************')
    print ('****   RANDOM VALUES GENERATED   ****')
    print ('*************************************')
    randRand = np.random.randint(50,121,100)
    randPrice = map(str, randRand)
    print ('\n')
    print ('    Day:      ', createList(100))
    print (' - '*300)
    print ('   Price: ', '      '.join(map(str, randRand)))
    print ('Changes:          ', priceChanges(randRand))
    print ('\n')
    start, end, maximum = findMaxSubarray(randRand, 0, len(randRand))
    print ('Low index: {} \nHigh index: {} \nMax sum: {}'.format(start, end - 1, maximum))