def binary(a,ele):
    mini,maxi=0,len(a)
    while mini<=maxi:
        mid = (maxi+mini)//2
        if a[mid]>ele:         # If element is smaller than a[mid], ignore right half of a
            maxi = mid - 1      #set upper index/limit to middle index -1
        elif a[mid]<ele:       # If element is greater than a[mid], ignore left half of a
            mini = mid + 1      #set lower index/limit to middle index +1 
        else:
            return mid          #if element is found return the index i.e. mid
    return -1               #if element is not found return -1


#driver code for the above function

a = [11,28,37,41,55,63,72,87,92]  #the list/array must be sorted before doing a binary search
print('Enter the Element to be searched:')
elementToBeFound = int(input())
indexFound = binary(a,elementToBeFound)
if indexFound == -1:
    print('Element is not present in the list')
else:
    print('Element found at index:',indexFound)
