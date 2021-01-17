## Multidimensional Array

A multidimensional array is an array of arrays. 2-dimensional arrays are the most commonly used ones.

2D arrays can be thought of as tables. A 2D array of size *N x M* has N rows and M columns, numbered from *0* to *N - 1* and *0* to *M - 1* respectively.  
The values can be accessed like they are in 1D arrays by using indices. Each value has 2 indices (one for row and the other for column), thus, the value at row *i* and column *j* can be accessed by arr[i][j].

Similarly, values in an array of N dimensions can be accessed using N indices.

### 2D array declaration

Similar to a 1D array declaration, we need the type of elements, the row size and the column size of the array.   
```
type arr[row_size][column_size];
```

### 2D array initialization

After declaration we need to initialize the array. This can happen in two ways, simultaneous declaration and initialization and initialization after declaration:

```
type arr[row_size][column_size] = {{elements}, {elements}, ..};
```

```
type arr[row_size][column_size];
arr[i][j] = element
```

The same methods can be extended for declaration and initialization of higher dimension arrays.
