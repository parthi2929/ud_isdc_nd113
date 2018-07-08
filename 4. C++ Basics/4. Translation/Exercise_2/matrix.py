class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix = self.g
        matrix_transpose = []
        for each_column in range(len(matrix[0])):       #note unlike usual method, we r taking column first..
            new_row = []
            for each_row in range(len(matrix)):
                new_row.append(matrix[each_row][each_column])
            matrix_transpose.append(new_row)
            #print(matrix_transpose)
        return Matrix(matrix_transpose)

    def dot_product(self, vector_one, vector_two):
        sum = 0
        for each_element in range(len(vector_one)):
            sum += vector_one[each_element]*vector_two[each_element]    #scalar dot product summing up..
        return sum

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        product = []
        matrixA = self.g
        matrixB_T = other.T().g     #multiplication using transpose method
        for each_row_A in range(len(matrixA)):
            new_row = []
            for each_row_B_T in range(len(matrixB_T)):
                new_row.append(self.dot_product(matrixA[each_row_A],matrixB_T[each_row_B_T]))   
            product.append(new_row)
        return Matrix(product)


