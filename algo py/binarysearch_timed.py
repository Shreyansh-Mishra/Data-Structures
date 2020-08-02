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

def binary(a,ele):
    mini,maxi=0,len(a)
    while mini<=maxi:
        mid = (maxi+mini)//2
        if mid>len(a)-1:
            return -1
        if a[mid]>ele:         # If element is smaller than a[mid], ignore right half of a
            maxi = mid - 1      #set upper index/limit to middle index -1
        elif a[mid]<ele:       # If element is greater than a[mid], ignore left half of a
            mini = mid + 1      #set lower index/limit to middle index +1 
        else:
            return mid          #if element is found return the index i.e. mid
    return -1               #if element is not found return -1


#driver code
a = [i for i in range(1,1001)]
b = [i for i in range(1000,0,-1)]
c = [randint(1,1001) for i in range(1,1001)]

#measuring time for binary search in all 3 lists
then = time.perf_counter()
binary(a, 1000)
now = time.perf_counter()
print(f'Time taken for binary search in list a(increasing order)  :',str(decimal.Decimal(now - then)))
then = time.perf_counter()
bubbleSort(b)
binary(b, 1000)
now = time.perf_counter()
print(f'Time taken for binary search in list b(decreasing order)  :',str(decimal.Decimal(now - then)))
then = time.perf_counter()
bubbleSort(c)
binary(c, 1000)
now = time.perf_counter()
print(f'Time taken for binary search in list c(random order)  :',str(decimal.Decimal(now - then)))
