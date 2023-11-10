## Quick Sort Algorithm

### Visual Representation
![Quick Sorting Image](https://raw.githubusercontent.com/mostafijur-rahman299/cracking-coding-interview-solutions/master/Sorting/quick-sort.jpg)

### Explaination
1. Increment i untill find greater than pivot
2. Decrement j untill find less than pivot
3. Than interchange both of them

### Code
```python
a = [10, 5, 8, 9, 3, 6, 15, 12, 16]

def partition(low, high):
    pivot = a[low]
    i, j = low, high
    
    while i < j:
        while a[i] <= pivot:
            i += 1
            
        while a[j] > pivot:
            j -= 1
            
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
        
    a[low], a[j] = a[j], a[low]
    return j
    

def quicksort(low, high):
    if low < high:
        j = partition(low, high)
        quicksort(low, j)
        quicksort(j+1, high)
    
    
quicksort(0, len(a)-1)
```