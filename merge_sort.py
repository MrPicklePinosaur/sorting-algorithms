import random as r
import math as m

def merge_sort(arr):
     if (len(arr) == 1):
          return arr

     mid = int((len(arr)+1)/2)
     arr1 = merge_sort(arr[:mid])
     arr2 = merge_sort(arr[mid:])

     for i in arr2: #for each value that we want to insert
          sorted_insert(i,arr1)

     print(arr1)
     return arr1

def sorted_insert(n_val,host_array): #sorted insert assuming host array is sorted least to greatest
     for ind in range(len(host_array)):
          h_val = host_array[ind] #get the current val in host_array
          if n_val < h_val:
               host_array.insert(ind,n_val)
               return
          
     host_array.append(n_val) #if array is empty


arr = [i for i in range(200)]
r.shuffle(arr)
print(arr)
merge_sort(arr)


