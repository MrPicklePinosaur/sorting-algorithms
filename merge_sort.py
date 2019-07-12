import random as r
import math as m

def merge_sort(arr):
     if (len(arr) == 1):
          return arr

     mid = int((len(arr)+1)/2)
     arr1 = merge_sort(arr[0:mid])
     arr2 = merge_sort(arr[mid:len(arr)])

     sorted_arr = []
     
     if (arr1 <= arr2):
          sorted_arr = arr1+arr2
     else:
          sort_arr = arr2+arr1
          

     print(sorted_arr)
     return sorted_arr

arr = [i for i in range(5)]
r.shuffle(arr)
print(arr)
merge_sort(arr)

