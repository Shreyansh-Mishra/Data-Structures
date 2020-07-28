def insertionSort(a):
    for i in range(1, len(a)):
        key = a[i]
        # Move elements of the array: a[0..i-1], that are greater than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

# Driver code to test the function written above
a = [11, 10, 12, 4, 5]
print('Array:',a)
insertionSort(a)
print('Sorted Array:',a)