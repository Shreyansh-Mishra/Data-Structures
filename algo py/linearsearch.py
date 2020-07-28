def linearSearch(l,key):
    #iterate over the whole array
	for i in range(len(l)):   
		if l[i]==key:   
			return i       #if the element is found return the index
	else:
		return -1           #if not found return -1

#driver code to test the function written above
a = [67,21,35,2,53,31,12]
print('Enter the Element to be searched:')
elementToBeFound = int(input())
indexFound = linearSearch(a,elementToBeFound)
if indexFound == -1:
    print('Element is not present in the list')
else:
    print('Element found at index:',indexFound)

