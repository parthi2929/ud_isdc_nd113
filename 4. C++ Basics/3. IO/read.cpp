#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main()
{
    string line;
    stringstream ss;

    vector < vector <float> > matrix;
    vector <float> row;

    float i;

    //reading the input from file..
    ifstream matrixfile ("matrix.txt");
    if (matrixfile.is_open())
    {
        while (getline (matrixfile, line))  //for each line
        {
            ss.clear();
            ss.str("");
            ss.str(line);


            row.clear();
            while(ss >> i) //this is not 'greater than' comparision, its just ss value fed in variable i and if thats success..
            {
                row.push_back(i);

                if (ss.peek() == ',' || ss.peek() == ' ')
                {
                    ss.ignore();
                }
            }

            matrix.push_back(row);
        }
    }
    matrixfile.close();

    //printing the output
    for(int row=0; row < matrix.size(); row++)
    {
        for(int column = 0; column < matrix[row].size(); column++)
        {
            cout << matrix[row][column] << " ";
        }
        cout << endl;
    }

    return 0;
}