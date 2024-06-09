# Write a function that takes an array and returns a new array with the elements in reverse order.
def reverse_array(arr):
    return arr[::-1]

# Test the function
arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))

#Write a function that returns the maximum element in an array.

def find_max(arr):
    return max(arr)

# Test the function
arr = [1, 2, 3, 4, 5]
print(find_max(arr))

#Write a function that returns the sum of all elements in an array.

def sum_array(arr):
    return sum(arr)

# Test the function
arr = [1, 2, 3, 4, 5]
print(sum_array(arr))


#Write a function that removes duplicates from an array and returns the new array.

def remove_duplicates(arr):
    return list(set(arr))

# Test the function
arr = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(arr))

#Write a function that merges two sorted arrays into a single sorted array.

def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
            
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
        
    return merged_array

# Test the function
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_sorted_arrays(arr1, arr2))

#Write a function that counts the number of occurrences of each element in an array and returns a dictionary.

def count_occurrences(arr):
    occurrences = {}
    for item in arr:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    return occurrences

# Test the function
arr = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(arr))


