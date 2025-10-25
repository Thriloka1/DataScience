<!-- Broadcasting and rules with calculations -->
Rule 1: If the arrays do not have the same number of dimensions, prepend the shape of the smaller-dimensional array with ones until both shapes have the same length.

Rule 2: The sizes of the dimensions are compared element-wise from the trailing dimensions (i.e., from the last dimension to the first).

Rule 3: Two dimensions are compatible when:   
They are equal, or  

One of them is 1
Example 1: Compatible shapes for broadcasting


shape needs to match
if not:
[1,2,3] shape: (3,)
[4,5,6,7] shape: (4,)
    go from right hand side, 3 !=4 and neither of them is 1 thus broadcasting fails
eg
[
    1,2,3   shape: (2,3)
    4,5,6
]
[
    2,2,2 shape (1,3)
]
one of the dimension should be 1

1 2 
3 4
5 6

2 2 2
