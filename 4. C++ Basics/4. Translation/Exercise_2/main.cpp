#include <iostream>
#include <vector>
#include "matrix.hpp"
using namespace std;

int main()
{
    Matrix m1({
        {1, 2, 3},
        {4, 5, 6}
    });

    Matrix m2({
        {7, -2},
        {-3, -5}, 
        {4,1}
    });

    Matrix m3 = m1 * m2;

    for(auto each_row : m3.g) 
    {   
        for(float each_elem : each_row) cout << each_elem << " ";
        cout << endl;
    }
    return 0;
}