import random as r
def insert_sort(arr):
     temp = None
     for i in range(1,len(arr)):
          for ind in range(i-1,0,-1):
               print(i,ind)
               if arr[i] < arr[ind]: #if current value is less than test value, switch them
                    temp = arr[ind]
                    arr[i] = arr[ind]
                    arr[ind] = temp
               

test_arr = [r.randint(0,100) for i in range(30)]
r.shuffle(test_arr)
insert_sort(test_arr)
print(test_arr)
               
