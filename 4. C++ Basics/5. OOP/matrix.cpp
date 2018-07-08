#include "matrix.h"

Matrix::Matrix()
{
    std::vector< std::vector<float> > default_grid (4, std::vector<float> (4, 0));
    grid = default_grid;
    rows = default_grid.size();
    cols = default_grid[0].size();
    
}
Matrix::Matrix(std::vector< std::vector<float> > input_grid)
{
    grid = input_grid;
    rows = input_grid.size();
    cols = input_grid[0].size();
    
}

void Matrix::setGrid(std::vector <std::vector <float> > input_matrix)
{
    grid = input_matrix;
    rows = input_matrix.size();
    cols = input_matrix[0].size();
}

std::vector <std::vector <float> > Matrix::getGrid()
{
    return grid;
}
std::vector<float>::size_type Matrix::getRows()
{
    return rows;
}
std::vector<float>::size_type Matrix::getCols()
{
    return cols;
}
Matrix Matrix::matrix_addition(Matrix otherMatrix)
{
    if ( 
        ( rows != otherMatrix.rows) || 
        ( cols != otherMatrix.cols) )
    {
        throw std::invalid_argument("matrices are not the same size");
    }

    std::vector <std::vector <float> > sum_matrix;
    std::vector <float> new_row;
    for(int each_row = 0; each_row < rows; each_row++)
    {
        new_row.clear();
        for (int each_col = 0; each_col < cols; each_col++)
        {
            new_row.push_back(grid[each_row][each_col] + otherMatrix.grid[each_row][each_col]);
        }
        sum_matrix.push_back(new_row);
    }
    
    return Matrix(sum_matrix);
}

void Matrix::matrix_print()
{
    for(int each_row = 0; each_row < rows; each_row++)
    {
        for (int each_col = 0; each_col < cols; each_col++)
        {
            std::cout << grid[each_row][each_col] << " ";
        }
        std::cout << std::endl; 
    }
    std::cout << std::endl; 
}

