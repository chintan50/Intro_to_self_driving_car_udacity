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
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        
        det=0
        
        if self.h==1:
            
            det = self.g[0]
            #print(det)
            return det
            
        else:
                    
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
        
            det = (a*d - b*c)
        
        #print(det)
        return det
    
    
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        
        tra = 0
        
        if self.h == 1:
        
            tra = self.g[0][0]
        
        else:
            
            for i in range(self.w):
                tra += self[i][i]
        
        
        return tra

    
    
    
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here   
        # Prevent division by zero, inversion not possible if determinant is zero
       
        if self.h == 1:
            
            matrix_inverse = [[1/self.g[0][0]]]
            
        if self.w == 2:
            # equation from matrix_cheat_sheet.ipynb
            
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            
            factor = 1/(a*d-b*c)
            
            matrix_inverse = [[d * factor, -b * factor], [-c * factor, a * factor]]
            
        return Matrix(matrix_inverse)
        print(matrix_inverse)
        
        #elif self.h == 2:
        
           # if self.g[0][0]*self.g[1][1] == self.g[0][1]*self.g[1][0]:
            
            #    raise ValueError('the matrix is not invertible')
            
        #else:
                #a = self[0][0]
                #b = self[1][1]
                #c = self[0][1]
                #d = self[1][0]
                
                #factor = 1/(a*b - c*d)
                
                #matrix_inverse = [[b,-c],[-d,a]]
                
                #for i in range(self.h):
                    
                    #for j in range(self.w):
                        
                        #matrix_inverse[i][j] = factor * matrix_inverse[i][j]
                        
       
                        
                        #return matrix_inverse  
                        #print(matrix_inverse)
    
    
    
    

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        
        matrix_transpose = []
        
        for c in range(self.w):
            new_row =[]
            
            for r in range(self.h):
                new_row.append(self.g[r][c])
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
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        # 
        
        m = self.g
        n= other.g
        answer = []
        row = []        
        for r in range(self.h):
                
            for c in range(self.w):
                
                answer.append(m[r][c] + n[r][c])
            
            row.append(answer)
            
            answer = []
            
        print(row)
            
        return Matrix(row) 


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
        
        answer = []
        
        for r in self.g:
            row = []
            for c in r:
                row.append(-c)
            answer.append(row)

        return Matrix(answer)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        m = self.g
        n= other.g
        
        answer = []
        
        row = []
        
        for r in range(self.h):
            
                      
            for c in range(self.w):
                
                answer.append(m[r][c] - n[r][c])
            
            row.append(answer)
            
            answer=[]
        
        print(row)
        return Matrix(row)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        grid=zeroes(self.h, other.w)
        
        for r in range(self.h):
            for c in range(other.w):
                for z in range(other.h):
                    grid[r][c] += self.g[r][z] * other.g[z][c]
        return grid
        print(grid)
        
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
        if isinstance(other, numbers.Number):
            #pass
            #   
            # TODO - your code here
            #
            grid=self
            for r in range(self.h):
                for c in range(self.w):
                    grid[r][c]*=other
            return grid