import random as r
'''
insertion sort assumes that the subarray to the left of the value is sorted
and therefore the current value can be inserted into the sorted array in sorted order
'''
def insert_sort(arr):
     #for each value
     for i in range(1,len(arr)):
          for ind in range(i):
               if arr[i] < arr[ind]:
                    #remove val from its cuurent position to its sorted position
                    temp = arr[i]
                    del arr[i]
                    arr.insert(ind,temp)
                    break
     return arr
               

test_arr = [i for i in range(10)]
r.shuffle(test_arr)
print(test_arr)
print(insert_sort(test_arr))

               
