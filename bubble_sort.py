def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(length-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]