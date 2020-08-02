import time
import decimal
from random import randint
def selectionSort(a):
    for i in range(len(a)):
    # Find the minimum element in unsorted array
        minimumIndex = i
        for j in range(i + 1, len(a)):
            if a[minimumIndex] > a[j]:
                minimumIndex = j
    # Swap the found minimum element with the first element
        a[i], a[minimumIndex] = a[minimumIndex], a[i]  #swapping using python method
        #furthermore we can use
            #temp = a[j]
            #a[j] = a[j+1]
            #a[j+1] = temp
        #the above written lines will also swap the elements

#driver code
a = [i for i in range(1,1001)]
b = [i for i in range(1000,0,-1)]
c = [randint(1,1000) for i in range(1,1001)]

#measuring time for selection sort in all 3 lists
then = time.perf_counter()
selectionSort(a)
now = time.perf_counter()
print(f'Time taken for selection sort in list a(increasing order)  :',str(decimal.Decimal(now - then)))
then = time.perf_counter()
selectionSort(b)
now = time.perf_counter()
print(f'Time taken for selection sort in list b(decreasing order)  :',str(decimal.Decimal(now - then)))
then = time.perf_counter()
selectionSort(c)
now = time.perf_counter()
print(f'Time taken for selection sort in list c(random order)  :',str(decimal.Decimal(now - then)))
