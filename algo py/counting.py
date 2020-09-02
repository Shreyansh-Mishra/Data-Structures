from random import randint,random
import time
import decimal
def countSort(arr):  
    #initialise count and out list
    output = [0 for i in range(len(arr)+1)] 
    count = [0 for i in range(len(arr)+1)] 

    ans = [0 for _ in arr] 
    for i in arr: 
        count[i] += 1       #count all occurences of arr[i] in index of count list
    for i in range(len(arr)): 
        count[i] += count[i-1] #taking running sum of count list
    for i in range(len(arr)): 
        output[count[arr[i]]-1] = arr[i] #storing it in output array
        count[arr[i]] -= 1      #decrementing the count
    for i in range(len(arr)): 
        ans[i] = output[i] 
    return ans  

arr = [randint(0,2000) for i in range(0,2000)]
then1 = time.perf_counter()
ans1 = countSort(arr)
now1 = time.perf_counter()


arr = [randint(0,4000) for i in range(0,4000)]
then2 = time.perf_counter()
ans2 = countSort(arr)
now2 = time.perf_counter()

arr = [randint(0,6000) for i in range(0,6000)]
then3 = time.perf_counter()
ans3 = countSort(arr)
now3 = time.perf_counter()

arr = [randint(0,8000) for i in range(0,8000)]
then4 = time.perf_counter()
ans4 = countSort(arr)
now4 = time.perf_counter()

arr = [randint(0,10000) for i in range(0,10000)]
then5 = time.perf_counter()
ans5 = countSort(arr)
now5 = time.perf_counter()

print('Time Taken: ',str(decimal.Decimal(now1 - then1)))
print('Time Taken: ',str(decimal.Decimal(now2 - then2)))
print('Time Taken: ',str(decimal.Decimal(now3 - then3)))
print('Time Taken: ',str(decimal.Decimal(now4 - then4)))
print('Time Taken: ',str(decimal.Decimal(now5 - then5)))

