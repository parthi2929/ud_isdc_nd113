#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
    vector < vector <int> > matrix (5 , vector <int> (3,2));
    vector <int> row;

    ofstream outputfile;
    outputfile.open("matrixoutput.txt");

    if (outputfile.is_open())
    {
        for (int row = 0; row < matrix.size(); row++)
        {
            int noOfColumns = matrix[row].size();
            for(int col = 0; col < noOfColumns; col++)
            {
                if (col != noOfColumns - 1) //not end of row
                {
                    outputfile << matrix[row][col] << ",";
                }
                else
                {
                    outputfile << matrix[row][col];
                }
                
            }
            outputfile << endl;
        }
    }
    outputfile.close();
    return 0;
}