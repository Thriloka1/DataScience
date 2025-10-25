import numpy as np


array = np.array([1, 2, 3, 4, 5])
print(array)

# Indexing
print(array[2])

# Slicing
print(array[1:4])

# Multi-dimensional array
multi_array = np.array([[1, 2, 3], [4, 5, 6]])
print(multi_array)

# Indexing
print(multi_array[1, 2])

# Slicing
print(multi_array[:2, :2])

# Boolean indexing  
bool_index = array > 2
print(array[bool_index])    

# Fancy indexing
indices = [0, 2, 4]
print(array[indices])

# Modifying
array[0] = 10
print(array)
array[1:3] = [20, 30]
print(array)

# Reshaping an array
reshaped_array = array.reshape((1, 5))
print(reshaped_array)

# Transposing
transposed_array = multi_array.T
print(transposed_array)    

# Combining indexing and slicing
print(multi_array[0, 1:3])

# Using ellipsis 
print(multi_array[..., 1]) 

# Advanced indexing with arrays
row_indices = np.array([0, 1])  
col_indices = np.array([2, 0])
print(multi_array[row_indices, col_indices])   

# Negative indexing
print(array[-1])

# Slicing with step
print(array[0:5:2])

# Copying arrays to avoid modifying the original    
array_copy = array.copy()
array_copy[0] = 99
print(array)
print(array_copy)    

# Using np.where for conditional indexing
conditional_indices = np.where(array > 15)
print(conditional_indices)
print(array[conditional_indices])  

# Using np.take for fancy indexing
taken_elements = np.take(array, [0, 3, 4])
print(taken_elements)

# Using np.put for modifying elements at specific indices
np.put(array, [1, 2], [55, 66])
print(array)

# Using np.split for splitting arrays
split_arrays = np.split(array, 1)
print(split_arrays)

# Using np.concatenate for combining arrays
combined_array = np.concatenate((array, np.array([7, 8, 9])))
print(combined_array)

# Using np.flatten to convert multi-dimensional array to 1D
flattened_array = multi_array.flatten()
print(flattened_array)    

# Using np.ravel to get a flattened view of the array
raveled_array = multi_array.ravel()
print(raveled_array)

# Using np.newaxis to increase dimensions
newaxis_array = array[:, np.newaxis]
print(newaxis_array)

# Using np.squeeze to remove single-dimensional entries
squeezed_array = newaxis_array.squeeze()
print(squeezed_array)

# Using np.expand_dims to add a new axis
expanded_array = np.expand_dims(array, axis=0)
print(expanded_array)

# Using np.swapaxes to swap two axes of a multi-dimensional array
swapped_array = np.swapaxes(multi_array, 0, 1)
print(swapped_array)

# Using np.rollaxis to roll the specified axis backwards
rolled_array = np.rollaxis(multi_array, 1)
print(rolled_array)    

# Using np.diagonal to get the diagonal of a multi-dimensional array
diagonal_elements = multi_array.diagonal()
print(diagonal_elements)    

# Using np.trace to get the sum of diagonal elements
trace_value = np.trace(multi_array)
print(trace_value)

# Using np.full to create an array filled with a scalar value
filled_array = np.full((2, 3), 7)
print(filled_array)

# Using np.copyto to copy values from one array to another based on a condition
target_array = np.array([0, 0, 0, 0, 0])
np.copyto(target_array, array, where=array > 20)
print(target_array)

# Using np.putmask to set elements of an array based on a condition
np.putmask(array, array < 30, -1)
print(array)

# Using np.take_along_axis for advanced indexing
indices = np.array([[0, 2], [1, 0]])
taken_along_axis = np.take_along_axis(multi_array, indices, axis=1)
print(taken_along_axis)

# Using np.choose for selecting elements from multiple arrays
choices = np.array([[10, 20, 30], [40, 50, 60]])
selector = np.array([0, 1, 0])
chosen_elements = np.choose(selector, choices)
print(chosen_elements)

# Using np.compress for selecting elements based on a condition
compressed_array = np.compress(array > 0, array)
print(compressed_array)

# Using np.extract to extract elements based on a condition
extracted_elements = np.extract(array > 0, array)
print(extracted_elements)

# Using np.nonzero to get indices of non-zero elements
nonzero_indices = np.nonzero(array)
print(nonzero_indices)
print(array[nonzero_indices])

# Using np.unique to get unique elements of an array
unique_elements = np.unique(np.array([1, 2, 2, 3, 4, 4, 5]))
print(unique_elements)

# Using np.sort to sort an array
sorted_array = np.sort(np.array([5, 2, 3, 1, 4]))
print(sorted_array)

# Using np.argsort to get the indices that would sort an array
argsorted_indices = np.argsort(np.array([5, 2, 3, 1, 4]))
print(argsorted_indices)

# Using np.lexsort for sorting by multiple keys
keys = (np.array([3, 2, 1]), np.array([1, 2, 3]))
lexsorted_indices = np.lexsort(keys)
print(lexsorted_indices)

# Using np.partition to partition an array
partitioned_array = np.partition(np.array([5, 2, 3, 1, 4]), 2)
print(partitioned_array)

# Using np.argpartition to get indices that would partition an array
argpartitioned_indices = np.argpartition(np.array([5, 2, 3, 1, 4]), 2)
print(argpartitioned_indices)

# Using np.clip to limit the values in an array
clipped_array = np.clip(np.array([1, 2, 3, 4, 5]), 2, 4)
print(clipped_array)

# Using np.where with three arguments for conditional selection
conditional_selection = np.where(array < 0, 0, array)   
print(conditional_selection)

# Using np.select for multiple conditions
conditions = [array < 0, array == 0, array > 0] 
choices = [-1, 0, 1]
selected_array = np.select(conditions, choices)
print(selected_array)

# Using np.isin to check for membership
membership_check = np.isin(array, [10, 30, 50])
print(membership_check)

# Using np.all and np.any for logical checks
all_positive = np.all(array > 0)
any_negative = np.any(array < 0)
print(all_positive)
print(any_negative)


#broadcasting in numpy
arr1=np.array([1,2,3,4]) #shape (4,)
arr2=np.array([6,7,8,9]) #shape (4,)
print(arr1)
print(arr2)
# arr3=arr1+arr2
arr3=arr1+4 #scalar value
print(arr3) #shape (4,) ==> col,row


arr2=np.array([[9],[8],[7]]) #shape (3,1)
print(arr2)

print(arr1+arr2) #final shape (3,4) after broadcasting




arr2=np.array([9,8,7,6,5]) #shape (5,)
try:
    print(arr1+arr2) 
except Exception as e:
    print("Error:", e)









