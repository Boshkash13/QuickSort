def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]  
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Example usage:
arr = [5, 9, 3, 1, -4, 7, 2]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)