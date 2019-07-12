import random as r

'''
heap sort is NOT stable, meaning it may not perserve the original order of
duplicate items

'''
def heap_sort():



test_arr = [i for i in range(10)]
r.shuffle(test_arr)
print(test_arr)
print(heap_sort(test_arr))



     
