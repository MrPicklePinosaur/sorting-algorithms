import random as r
import math as m

def merge_sort(arr):
     if (len(arr) == 1):
          return arr

     mid = int((len(arr)+1)/2)
     arr1 = merge_sort(arr[0:mid])
     arr2 = merge_sort(arr[mid:len(arr)])

     for i in arr2: #for each value that we want to insert
          sorted_insert(i,arr1)

     print(arr1)
     return arr1

def sorted_insert(n_val,host_array): #sorted insert assuming host array is sorted least to greatest
     for ind in range(len(host_array)-1,-1,-1):
          h_val = host_array[ind] #get the current val in host_array
          if (n_val >= h_val):
               host_array.insert(ind,n_val)
               return
          
     host_array.append(n_val) #if array has index of zero

'''
arr = [i for i in range(5)]
r.shuffle(arr)
print(arr)
merge_sort(arr)

'''
arr = []
for i in range(10):
     sorted_insert(r.randint(0,30),arr)
     print(arr)

