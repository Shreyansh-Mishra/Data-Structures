import time
import decimal
from random import randint

def partition(arr,l,h): 
    i = ( l - 1 ) 
    x = arr[h] 
  
    for j in range(l , h): 
        if   arr[j] <= x:   
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[h] = arr[h],arr[i+1] 
    return (i+1) 
  
def quickSort(arr,l,h):  
    size = h - l + 1
    stack = [0] * (size) 
    top = -1
    top = top + 1
    stack[top] = l 
    top = top + 1
    stack[top] = h 
    while top >= 0: 
        h = stack[top] 
        top = top - 1
        l = stack[top] 
        top = top - 1
        p = partition( arr, l, h ) 
        if p-1 > l: 
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = p - 1
        if p+1 < h: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h 
  
a = [i for i in range(1,10001)]
b= [i for i in range(10001,0,-1)]
c = [randint(1,10001) for i in range(1,10001)]
n = len(a)
then = time.perf_counter()
quickSort(a, 0, n-1)
now = time.perf_counter()


then2 = time.perf_counter()
quickSort(b, 0, n-1)
now2 = time.perf_counter()

then3 = time.perf_counter()
quickSort(c, 0, n-1)
now3 = time.perf_counter()

print("Time Taken: ", str(decimal.Decimal(now - then)))
print("Time Taken: ", str(decimal.Decimal(now2 - then2)))
print("Time Taken: ", str(decimal.Decimal(now3 - then3)))