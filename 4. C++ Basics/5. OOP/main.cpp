#include <iostream>
#include <vector>
#include "matrix.h"

int main () {
    
	std::vector <std:: vector <float> > initial_grid (7, std::vector <float>(5, 0.4));
    
    Matrix m1(initial_grid);
    m1.matrix_print();
    std::cout << "m1 No of rows: " << m1.getRows() << std::endl;
    std::cout << "m1 No of cols: " << m1.getCols() << std::endl;

    std::vector <std:: vector <float> > initial_grid2 (7, std::vector <float>(5, 0.2));

    Matrix m2(initial_grid2);
    Matrix m3 = m1.matrix_addition(m2);
    m3.matrix_print();

    return 0;
}