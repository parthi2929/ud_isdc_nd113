import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise ValueError("Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise NotImplementedError("Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:     #if 1x1 matrix the only one element itself is determinant
            return self.g[0]
        if self.h == 2:
            g = self.g
            return g[0][0]*g[1][1] - g[0][1]*g[1][0]    #return determinant as per formula
        

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise ValueError("Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        sum = 0
        for i in range(len(self.g)):
            for j in range(len(self.g[0])):
                if i==j: sum += self.g[i][j]    #calcuating sum only for diagonal implied by i = j
        return sum

    def inverse(self):
        """
        Calculates the inversed of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise ValueError("Non-square Matrix does not have an inversed.")
        if self.h > 2:
            raise NotImplementedError("inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        matrix = self.g
        inversed = []
        if (len(matrix) == 1):
            inversed.append([1/matrix[0][0]])       #inverse of 1x1 would be simply the same
            #print(inversed)
        elif (len(matrix) == 2):
            determinant = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
            if (determinant == 0):
                raise ValueError('The denominator of a fraction cannot be zero')
            else:                                   #inverse of 2x2 is more
                row = []
                row.append(matrix[1][1]*(1/determinant))
                row.append(-matrix[0][1]*(1/determinant))
                inversed.append(row)
                row = []
                row.append(-matrix[1][0]*(1/determinant))
                row.append(matrix[0][0]*(1/determinant))
                inversed.append(row)
        #print(inversed)
        return Matrix(inversed)

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

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise ValueError("Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        result = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] + other.g[i][j])    #straight forward adding
            result.append(row)
        return Matrix(result)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        result = []
        for i in range(len(self.g)):
            row = []
            for j in range(len(self.g)):
                row.append(-self.g[i][j])   #negating each element
            result.append(row)
        return Matrix(result)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        result = []
        for i in range(len(self.g)):
            row = []
            for j in range(len(self.g)):
                row.append(self.g[i][j] - other.g[i][j])    #subtracting 
            result.append(row)
        return Matrix(result)

    def dot_product(self, vector_one, vector_two):
        sum = 0
        for each_element in range(len(vector_one)):
            sum += vector_one[each_element]*vector_two[each_element]    #scalar dot product summing up..
        return sum

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        product = []
        matrixA = self.g
        matrixB_T = other.T().g     #multiplication using transpose method
        for each_row_A in range(len(matrixA)):
            new_row = []
            for each_row_B_T in range(len(matrixB_T)):
                new_row.append(self.dot_product(matrixA[each_row_A],matrixB_T[each_row_B_T]))   
            product.append(new_row)
        return Matrix(product)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        product = []
        if isinstance(other, numbers.Number):
            for i in range(len(self.g)):
                row = []
                for j in range(len(self.g[0])):
                    row.append(other*self.g[i][j])
                product.append(row)
        #print('product h:{} w:{}'.format(len(product),len(product[0])))
        return Matrix(product)
