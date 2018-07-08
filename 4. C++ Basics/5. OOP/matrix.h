#ifndef MATRIX_H
#define MATRIX_H
#include <vector>
#include <iostream>
#include <stdexcept> //library for the invalid_argument method


class Matrix 
{

        private:

            std::vector< std::vector<float> > grid;
            std::vector<float>::size_type rows;
            std::vector<float>::size_type cols;
            
        public:
        
        Matrix();
        Matrix(std::vector <std::vector <float> >);
        

        void setGrid(std::vector <std::vector <float> >);
        std::vector <std::vector <float> > getGrid();
        std::vector<float>::size_type getRows();
        std::vector<float>::size_type getCols();
        

        Matrix matrix_addition(Matrix);
        void matrix_print();


};
        
#endif /* MATRIX_H */