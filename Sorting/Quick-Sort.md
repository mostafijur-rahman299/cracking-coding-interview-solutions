## Quick Sort Algorithm

### Visual Representation
![Quick Sorting Image](https://raw.githubusercontent.com/mostafijur-rahman299/cracking-coding-interview-solutions/master/Sorting/quick-sort.jpg)
__source__: https://www.youtube.com/watch?v=QXum8HQd_l4

### Explaination
1. Increment i untill find greater than pivot
2. Decrement j untill find less than pivot
3. Than interchange both of them

### Code
```python
a = [10, 5, 8, 9, 3, 6, 15, 12, 16]

def partition(array, low, high):
 
    # Choose the rightmost element as pivot
    pivot = array[high]
 
    # Pointer for greater element
    i = low - 1
 
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1

def partition(low, high):
    pivot = a[low]
    i, j = low, high
    
    while i < j:
        while a[i] <= pivot:
            i += 1
            
        while a[j] > pivot:
            j -= 1
            
        if i < j:
            a[i], a[j] = a[j], a[i]
        
    a[low], a[j] = a[j], a[low]
    return j
    

def quicksort(low, high):
    if low < high:
        pi = partition(low, high)
        quicksort(low, pi)
        quicksort(pi+1, high)
    
    
quicksort(0, len(a)-1)
```