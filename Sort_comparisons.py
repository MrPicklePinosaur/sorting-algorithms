#import and shorten names
import matplotlib as mpl
import matplotlib.pyplot as plt
import random as r
import time as t

#Constants
min_size = 2
max_size = 500

#The array of values that we are sorting; SHOULD NEVER BE MODIFIED BY SORTING ALGORITHMS
org_arr = []

#array that all sorts will be run on
test_arr = []

#generate random array, takes amount of numbers to generate
def increment_size(amount):
    new_arr = []
    for i in range(amount):
        #numbers are between 0 and 5000
        new_arr.append(r.randint(0,5000))
    test_arr = new_arr

#creates a copy of the current test array for actual use
def copy_arr(): 
    new_arr = []
    for i in org_arr:
        new_arr.append(i)
    return new_arr
        
def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(length-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

#run the sort on each array multiple times, graph average
runs = 5

#set up for loop to generate arrays from length 2 to length 1000
for i in range(min_size,max_size):
    increment_size(i)

    #run each length array some amount of times, dependant on runs
    for j in range(runs):

        bubble_sort(copy_arr())

        copy_arr().sort()

    
    

        
