#import and shorten names
import matplotlib as mpl
import matplotlib.pyplot as plt
import random as random
import time as time
randint = random.randint
time = time.time

#from 2 item to 1000 items in the array
x_axis = [i for i in range(2,501)]

#array that all sorts will be run on
test_arr = []
#bubble sort data
bubble_data = []
#built in sort function in python
default_data = []
radix_data = []
merge_data = []
quick_data = []

def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(length-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

#generate random array, takes amount of numbers to generate
def generate_array(amount):
    for i in range(amount):
        #numbers are between 0 and 1000
        test_arr.append(randint(0,5000))

#run the sort on each array multiple times, graph average
runs = 5
#runtime of sorting algo, the average of this will be graphed
bubble_runtime = 0.0
default_runtime = 0.0
#set up for loop to generate arrays from length 2 to length 1000
for i in range(2,501):
    #run each length array some amount of times, dependant on runs
    for j in range(runs):
        #generate array
        generate_array(i)
        #begin timing for bubble sort
        time1 = time()
        bubble_sort(test_arr)
        #record runtime
        bubble_runtime += (time()-time1)
        #begin timing for default sort
        time2 = time()
        test_arr.sort()
        default_runtime += (time()-time2)
        #reset test array
        test_arr = []
    #add data rounded to 7 decimal points
    bubble_data.append(round(bubble_runtime/runs,7))
    default_data.append(round(default_runtime/runs,7))
    #reset runtime for next array length
    bubble_runtime = 0.0
    default_runtime = 0.0
#color is blue
plt.plot(x_axis,bubble_data)
#color is orange
plt.plot(x_axis,default_data)
#labels on x and y axis
plt.xlabel("Number of items in array")
plt.ylabel("Runtime (seconds)")
plt.show()
    
    

        
