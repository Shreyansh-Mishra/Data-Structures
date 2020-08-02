import time
from random import randint
import decimal

# An optimized version of Bubble Sort
def bubbleSort(a):
    n = len(a)   #gives the length of array
    for i in range(n):
        swaps = False
        for j in range(0, n - i - 1):           # Last i elements are already in place
            # traverse the array from 0 to n-i-1
            # Swap only if the next element is found smaller than the current
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]   #swap 2 elements using a python method
                #furthermore we can use
                    #temp = a[j]
                    #a[j] = a[j+1]
                    #a[j+1] = temp
                #the above written lines will also swap the elements
                swaps = True     
        if swaps == False:        #if no elements were swapped in the inner loop then break out of it 
            break


def linear(l,key):
    #iterate over the whole array
	for i in range(len(l)):   
		if l[i]==key:   
			return i       #if the element is found return the index
	else:
		return -1           #if not found return -1

#driver code
a = [i for i in range(1,1001)]
b = [i for i in range(1000,0,-1)]
c = [randint(1,1001) for i in range(1,1001)]

#measuring time for linear search in all 3 lists
then = time.perf_counter()
linear(a, 1000)
now = time.perf_counter()
print(f'Time taken for linear search in list a(increasing order)  :',str(decimal.Decimal(now - then)))
then = time.perf_counter()
bubbleSort(b)
linear(b, 1000)
now = time.perf_counter()
print(f'Time taken for linear search in list b(decreasing order)  :',str(decimal.Decimal(now - then)))
then = time.perf_counter()
bubbleSort(c)
linear(c, 1000)
now = time.perf_counter()
print(f'Time taken for linear search in list c(random order)  :',str(decimal.Decimal(now - then)))
