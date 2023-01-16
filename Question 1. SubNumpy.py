""" -------------------------------------FIRST QUESTION----------------------------"""

# Question1
"""snp.ones(Int): the ones function takes an int parameter and returns an array (list) of length int 
parameter, and the array contains only ones. Example: snp.ones(5) = [1,1,1,1,1]"""


def ones(Int):
    array = []
    for x in range(Int):
        array.append(1)
    return array


print(ones(5))

# Question2
"""snp.zeros(Int): similar to the ones function, expect returns an array of zeros instead of ones."""


def zeros(Int):
    array = []
    for x in range(Int):
        array.append(0)
    return array


print(zeros(5))

# Question3
"""snp.reshape(array, (row, column)): takes an array and converts it into the dimensions specified
by the tuple (row, column). Hence this function converts from a vector to a matrix. For an
example on reshape functionality of numpy, refer to fig."""


def reshape(array, row, column):
    new_arr = []
    arr_row = len(array)
    # check if it is not single row
    try:
        arr_column = len(array[0])
        single_row = False
    except:
        arr_column = 1
        single_row = True
    flat_array = []
    i = 0
    # take all the elements if it's multiple rows or use the array itself if it's a single row
    if single_row == False:
        for x in range(arr_row):
            for y in range(arr_column):
                flat_array.append(array[x][y])
    else:
        flat_array = array
    # reshape the array according to specified row and column
    for x in range(row):
        temp_array = []
        for y in range(column):
            temp_array.append(flat_array[i])
            i = i + 1
        new_arr.append(temp_array)
    return new_arr


# Testing Section

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
array2 = [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]]

print(reshape(array, 4, 3))
print(reshape(array2, 2, 6))

# Question4
"""snp.shape(array) : returns a tuple with the matrix/vector’s dimension e.g. (# rows, # columns)."""


def shape(array):
    try:
        rows = len(array)
        columns = len(array[0])
    except:
        rows = len(array)
        columns = 1
    return (rows, columns)


# Testing Section

array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10, 11, 12]]
array2 = [[1], [2], [3]]

print(shape(array))
print(shape(array2))

# Question5
"""snp.append(array1, array2) : returns a new vector/matrix that is the combination of the two
input vectors/matrices. Note that you can’t append a vector to a matrix and vice versa and
therefore use suitable exception handling and throw/return user friendly error messages."""


def append(array1, array2):
    R = []
    c1 = len(array1[0])
    c2 = len(array2[0])
    r1 = len(array1)
    r2 = len(array2)
    print(f'Your 1st matrix has {r1} rows and {c1} columns')
    print(f'Your 2st matrix has {r2} rows and {c2} columns')

    if 1 in (r1, c1):
        print("First array is a vector")
        if 1 in (r2, c2):
            print("Second array is a vector")
            arrays = *array1, *array2
            for element in arrays:
                if len(element) > 0:
                    for sub_element in element:
                        R.append(sub_element)
                else:
                    R.append(element)
        else:
            raise TypeError('The second array is a matrix. Cannot append')
    else:
        print("First array is a matrix")
        if 1 in (r2, c2):
            raise TypeError('The second array is a vector. Cannot append')
        else:
            arrays = *array1, *array2
            for element in arrays:
                if len(element) > 0:
                    for sub_element in element:
                        R.append(sub_element)
                else:
                    R.append(element)
    return R


# Testing Section
# A and B -  Cannot append - An error should be shown.
A = [[1, 2, 3, 7], [1, 2]]
B = [[1], [2], [7]]
# C and D - Can append
C = [[1, 2], [3, 4]]
D = [[5, 6], [7, 8]]

# print(append(A,B))
print(append(C, D))

# Question6
"""snp.get(array, (row, column)): returns the value specified by the coordinate point (row, column)
of the array provided (can be vector or matrix)."""


def get(array, row, column):
    array_row = array[row]
    array_column = array_row[column]
    return array_column


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10, 11, 12]]

print(get(array, 2, 2))

# Question7
"""snp.add(array1, array1) : addition on vectors/matrices."""


def add(array1, array2):
    array3 = []
    row = len(array1)
    column = len(array1[0])
    arrresult = []
    for x in range(row):
        array3 = []
        for y in range(column):
            result = get(array1, x, y) + get(array2, x, y)
            array3.append(result)
        arrresult.append(array3)
    return arrresult


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10, 11, 12]]

print(add(array, array))

# Question8
"""snp.subtract(array1, array1) : subtraction on vectors/matrices."""


def subtract(array1, array2):
    array3 = []
    row = len(array1)
    column = len(array1[0])
    arrresult = []
    for x in range(row):
        array3 = []
        for y in range(column):
            result = get(array1, x, y) - get(array2, x, y)
            array3.append(result)
        arrresult.append(array3)
    return arrresult


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10, 11, 12]]

print(subtract(array, array))

# Question9
"""snp.dotproduct(array1, array1): computes the dot product between two arrays (which could be
vectors or/and matrices) and returns an appropriate value. Use appropriate exception handling
to output user-friendly error messages if the dot product cannot be performed between the
given arrays."""


def dotproduct(array1, array2):
    rows_1 = len(array1)
    col_1 = len(array1[0])
    rows_2 = len(array2)
    col_2 = len(array2[0])
    if col_1 != rows_2:
        raise TypeError("Row/Column dimensions should match to compute the dot product")
    else:
        arr_result = []
        for x in range(rows_1):
            arr_result.append([])
            for y in range(col_2):
                result = 0
                for z in range(rows_2):
                    result += array1[x][z] * array2[z][y]
                arr_result[x].append(result)
        return arr_result


# Testing Section

# Scenario#1 [2*3 Matrix]*[3*3 Matrix] - Can be multiplied
matrix_1 = [[1, 2, 3],
            [4, 5, 6]]
matrix_2 = [[1, 2, 5],
            [3, 4, 6],
            [5, 6, 7]]

print(dotproduct(matrix_1, matrix_2))

# Scenario#2 [1*3 Vector]*[3*1 Vector] - Can be multiplied
vector_1 = [[1, 2, 3]]
vector_2 = [[4], [5], [6]]

print(dotproduct(vector_1, vector_2))

# Scenario#3 [2*3 Matrix]*[3*2 Matrix] - Can be multiplied
matrix_4 = [[1, 2],
            [3, 4],
            [5, 6]]

print(dotproduct(matrix_1, matrix_4))

# Scenario#4 [2*3 Matrix]*[1*3 Vector] - Cannot be multiplied
matrix_3 = [[7, 8, 9],
            [10, 11, 12]]
vector_3 = [[7, 8, 9]]

# print(dotproduct(matrix_3, vector_3))