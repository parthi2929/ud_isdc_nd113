def get_row(matrix, row):
    return matrix[row]

def get_column(matrix, column_number):
    column = []
    for each_row in range(len(matrix)):
        #print('get_column row index:{} col index:{}'.format(each_row,column_number))
        column.append(matrix[each_row][column_number])
    return column

def dot_product(vector_one, vector_two):
    sum = 0
    for each_element in range(len(vector_one)):
        sum += vector_one[each_element]*vector_two[each_element]
    return sum

def matrix_multiplication(matrixA, matrixB):
    m_rows = len(matrixA)
    p_columns = len(matrixB[0])
    print('m_rows of matrixA:{} p_cols of matrixB:{}'.format(m_rows,p_columns))
    result = []
    for each_row in range(m_rows):
        row_result = []
        for each_column in range(p_columns):
            each_row_list = get_row(matrixA, each_row)
            each_column_list = get_column(matrixB, each_column)
            each_resultant_element = dot_product(each_row_list, each_column_list)
            row_result.append(each_resultant_element)
        result.append(row_result)
    print(result)
    return result

def transpose(matrix):
    matrix_transpose = []
    for each_column in range(len(matrix[0])):
        new_row = []
        for each_row in range(len(matrix)):
            new_row.append(matrix[each_row][each_column])
        matrix_transpose.append(new_row)
        #print(matrix_transpose)
    return matrix_transpose


def matrix_multiplication_new(matrixA, matrixB):
    product = []
    matrixB_T = transpose(matrixB)
    for each_row_A in range(len(matrixA)):
        new_row = []
        for each_row_B_T in range(len(matrixB_T)):
            new_row.append(dot_product(matrixA[each_row_A],matrixB_T[each_row_B_T]))
        product.append(new_row)
    print(product)
    return product

def identity_matrix(n):
    identity = []
    for i in range(n):
        row = []
        for j in range(n):
            if (i == j): row.append(1)
            else: row.append(0)
        identity.append(row)
    return identity

def inverse_matrix(matrix):
    
    inverse = []
    
    if len(matrix) != len(matrix[0]):
        raise ValueError('The matrix must be square')

    if (len(matrix) > 2):
        raise NotImplementedError('this functionality is not implemented')
        
    if (len(matrix) == 1):
        inverse.append([1/matrix[0][0]])
        #print(inverse)
    elif (len(matrix) == 2):
        determinant = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        if (determinant == 0):
            raise ValueError('The denominator of a fraction cannot be zero')
        else:
            row = []
            row.append(matrix[1][1]*(1/determinant))
            row.append(-matrix[0][1]*(1/determinant))
            inverse.append(row)
            row = []
            row.append(-matrix[1][0]*(1/determinant))
            row.append(matrix[0][0]*(1/determinant))
            inverse.append(row)
    print(inverse)
    return inverse


assert inverse_matrix([[100]]) == [[0.01]]
assert inverse_matrix([[4, 5], [7, 1]]) == [[-0.03225806451612903, 0.16129032258064516],
 [0.22580645161290322, -0.12903225806451613]]