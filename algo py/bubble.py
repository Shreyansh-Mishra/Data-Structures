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

# Driver code to test the function written above
a = [61, 32, 23, 11, 21, 10, 90]
print('Array:', a)
bubbleSort(a)
print('Sorted array:', a)