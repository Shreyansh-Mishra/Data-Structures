class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def get_parent(self, i):
        return int((i-1)//2)
    def get_left_child(self, i):
        return 2*i+1
    def get_right_child(self, i):
        return 2*i+2

    def has_parent(self, i):
        return self.get_parent(i)>=0
    def has_left_child(self, i):
        return self.get_left_child(i) < len(self.heap)
    def has_right_child(self, i):
        return self.get_right_child(i) < len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert_key(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self, i):
        size = len(self.heap)
        while(self.has_parent(i) and self.heap[i] > self.heap[self.get_parent(i)]):
            self.swap(i, self.get_parent(i))
            i = self.get_parent(i)
    
    def print_heap(self):
        print(self.heap)

    def delete_root(self):
        if len(self.heap)==0:
            return -1
        last_index = len(self.heap) - 1
        self.swap(0, last_index)
        root = self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_down(self,i):
        while(self.has_left_child(i)):
            max_child_ind = self.get_max_child_index(i)
            if max_child_ind == -1:
                break
            if self.heap[i] < self.heap[max_child_ind]:
                self.swap(i, max_child_ind)
                i= max_child_ind
            else:
                break

    def get_max_child_index(self, i):
        if(self.has_left_child(i)):
            left_c = self.get_left_child(i)
            if(self.has_right_child(i)):
                right_c = self.get_right_child(i)
                if(self.heap[left_c]> self.heap[right_c]):
                    return left_c
                else:
                    return right_c 
        else:
            return -1

def heapify(arr, n, i): 
    largest = i   
    l = 2 * i + 1      
    r = 2 * i + 2       
    if l < n and arr[i] < arr[l]: 
        largest = l 
   
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]   
  
        heapify(arr, n, largest) 
  
 
def heapSort(arr): 
    n = len(arr) 
  
    for i in range(n // 2 - 1, -1, -1): 
        heapify(arr, n, i) 
  
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   
        heapify(arr, i, 0)

max_heap = MaxHeap()

a = [i for i in range(2000)]
for i in a:
    max_heap.insert_key(i)

print("Initial Heap:")
max_heap.print_heap()
max_heap.delete_root()
print('\n\nAfter Deletion of Root: ')
max_heap.print_heap()

heapSort(a)
print('\n\nSorted array: ')
print(a)