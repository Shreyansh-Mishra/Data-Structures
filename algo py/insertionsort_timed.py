import time
from random import randint
import decimal
def insertionSort(a):
    for i in range(1, len(a)):
        key = a[i]
        # Move elements of the array: a[0..i-1], that are greater than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

#driver code
a = [i for i in range(1,1001)]
b = [i for i in range(1000,0,-1)]
c = [randint(1,1000) for i in range(1,1001)]

#measuring time for insertion sort in all 3 lists
then = time.perf_counter()
insertionSort(a)
now = time.perf_counter()
print(f'Time taken for insertion sort in list a(increasing order)  :',str(decimal.Decimal(now - then)))
then = time.perf_counter()
insertionSort(b)
now = time.perf_counter()
print(f'Time taken for insertion sort in list b(decreasing order)  :',str(decimal.Decimal(now - then)))
then = time.perf_counter()
insertionSort(c)
now = time.perf_counter()
print(f'Time taken for insertion sort in list c(random order)  :',str(decimal.Decimal(now - then)))
