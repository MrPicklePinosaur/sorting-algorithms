#import and shorten names
import matplotlib as mpl
import matplotlib.pyplot as plt
import random as r
import time as t

from insertion_sort import *
from merge_sort import *
from bubble_sort import *

#Constants
min_size = 2
max_size = 500
runs = 5 #run the sort on each array multiple times, graph average
sorts = ["insertion_sort","merge_sort","bubble_sort","sorted_insert_sort"]

data = {sort : [] for sort in sorts}
org_arr = [] #originala array; SHOULD NOT BE MODIFIED BY SORTING ALGORITHMS

def increment_size(amount):
    new_arr = [i for i in range(amount)]
    r.shuffle(new_arr)
    return new_arr

def copy_arr(): 
    copied = []
    for i in org_arr:
        copied.append(i)
    return copied


for i in range(min_size,max_size+1):
    #regenerate array
    org_arr = increment_size(i)
    #print(org_arr)

    #Insertion sort
    test_arr = copy_arr()
    start_time = t.time()
    insert_sort(test_arr)
    total_time = t.time()-start_time
    data["insertion_sort"].append(total_time)

    #merge sort
    test_arr = copy_arr()
    start_time = t.time()
    merge_sort(test_arr)
    total_time = t.time()-start_time
    data["merge_sort"].append(total_time)

    #bubble sort
    test_arr = copy_arr()
    start_time = t.time()
    bubble_sort(test_arr)
    total_time = t.time()-start_time
    data["bubble_sort"].append(total_time)

    #sorted insert sort
    test_arr = copy_arr()
    start_time = t.time()
    sorted_insert_sort(test_arr)
    total_time = t.time()-start_time
    data["sorted_insert_sort"].append(total_time)

for s in sorts: #graph the data
    plt.plot([i for i in range(min_size,max_size+1)],data[s])

plt.show()
    

        
