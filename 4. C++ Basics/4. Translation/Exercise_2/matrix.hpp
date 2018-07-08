#include <iostream>
#include <vector>
using namespace std;
class Matrix
{
    public:

    vector < vector <float> > g;
    int h;
    int w;

    // Constructor
    Matrix(vector < vector <float> > grid)
    {
        g = grid;
        h = grid.size();
        w = grid[0].size(); //assuming all rows have equal no of columns
    }

    // Transpose
    Matrix T()
    {
        vector < vector <float> > matrix_transpose;
        for (int each_column = 0; each_column < g[0].size(); each_column++)
        {
            vector <float> new_row;
            for (int each_row = 0; each_row < g.size(); each_row++)
            {
                new_row.push_back(g[each_row][each_column]);
            }
            matrix_transpose.push_back(new_row);
        }
        return Matrix(matrix_transpose);
    }

    // Dot product
    float dot_product(vector <float> v_1, vector <float> v_2)
    {
        float sum = 0;
        for(int i=0; i<v_1.size(); i++)
        {
            sum += v_1[i]*v_2[i];
        }
        return sum;
    }

    // multiplication by operator *
    Matrix operator*(Matrix other)
    {
        /*
        Defines the behavior of * operator (matrix multiplication)
        */
       vector < vector <float> > product;
       vector < vector <float> > matrixA = g;
       vector < vector <float> > matrixB_T = other.T().g;
       for (int each_row_A = 0; each_row_A < matrixA.size() ; each_row_A++)
       {
           vector <float> new_row;
           for (int each_row_B_T = 0; each_row_B_T < matrixB_T.size(); each_row_B_T++)
           {
               new_row.push_back(dot_product(matrixA[each_row_A],matrixB_T[each_row_B_T]));
           }
           product.push_back(new_row);
       }
       return Matrix(product);
    }



};