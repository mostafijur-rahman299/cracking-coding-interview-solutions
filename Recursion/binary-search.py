def binary_search(target, arr, start, end):
    
    mid = int((start + end) / 2)
    if arr[mid] > target:
        end = mid - 1
    elif arr[mid] < target:
        start = mid + 1
    elif arr[mid] == target:
        print(f"The index number of this {target} target is =", mid)
        return
        
    if start > end:
        if arr[mid] != target:
            print("Oops! May be this number is not present in this array.")
        return
    
    binary_search(target, arr, start, end)
    
        
binary_search(89, [1, 3, 5, 6, 8, 9, 11, 13, 89, 109], 0, 9)

def binary_search2(target, arr):
    start = 0
    end = len(arr)
    while start <= end:
        mid = int((start + end) / 2)
        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        elif arr[mid] == target:
            print(f"The index number of this {target} target is =", mid)
            return
                
    print("Oops! May be this number is not present in this array.")
    
        
binary_search2(89, [1, 3, 5, 6, 8, 9, 11, 13, 89, 109])


def binary_search(target, array):
    start = 0
    end = len(array)
    mid = int((start + end)/2)
    
    new_array = array
    
    if array[mid] == target:
        print("The index of this number is ", mid)
        return
    elif array[mid] > target:
        new_array = array[:mid]
    elif array[mid] < target:
        new_array = array[mid+1:]
        
    if len(new_array) == 0:
        if array[mid] != target:
            print("Opps! not found.")
        return
    
    binary_search(target, new_array)
        
binary_search(0, [1, 4, 5, 11, 12, 13, 14, 21, 22, 23, 34])

