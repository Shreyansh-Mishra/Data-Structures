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

#driver code to test the function written above
a = [61, 23, 11, 21, 10]
print('Array:',a)
selectionSort(a)
print('Sorted Array',a)