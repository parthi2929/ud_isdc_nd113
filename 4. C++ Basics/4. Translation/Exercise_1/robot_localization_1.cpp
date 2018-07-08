#include <iostream>
#include <vector>

using namespace std;
//Given the list motions=[1,1] which means the robot 
//moves right and then right again, compute the posterior 
//distribution if the robot first senses red, then moves 
//right one, then senses green, then moves right again, 
//starting with a uniform prior distribution.

vector <float> p (5 ,0.2);
vector <string> world = {"green", "red", "red", "green", "green"};
float pHit = 0.6;
float pMiss = 0.2;

vector <float> sense(vector <float> p, string Z);
vector <float> move(vector <float> p, int U);
int main()
{
    vector <string> measurements = {"red", "red"};
    vector <int> motions = {1,1};
    for (int i=0; i< measurements.size(); i++)
    {
        p = sense(p, measurements[i]);
        p = move(p, motions[i]);
    }
    for (float n: p) cout << n << " ";
    return 0;
}


vector <float> sense(vector <float> p, string Z)
{
    /*
    p = initial probability distribution list
    Z = each measurement
    q = new normalized distribution list
    */
    vector <float> q (p.size());
    for (int each_index = 0; each_index < p.size(); each_index++)
    {
        if (world[each_index] == Z)
        {
            q[each_index] = p[each_index]*pHit;
        }
        else
        {
            q[each_index] = p[each_index]*pMiss;
        }
    }
    float total = 0; for (float n: q) total += n; //https://stackoverflow.com/questions/3221812/how-to-sum-up-elements-of-a-c-vector
    for (float& n: q) n /= total;   //https://stackoverflow.com/questions/41030911/how-to-multiply-a-vector-and-scalar-in-c
    return q;
}

float pExact = 0.8;
float pOvershoot = 0.1;
float pUndershoot = 0.1;
vector <float> move(vector <float> p, int U)
{
    /*
    p = given probability distribution list
    U = amount of steps robot has moved to right (assumed as right for now)
    */
    //INEXACT MOTION
    vector <float> q (p.size());
    vector <float> temp = {pUndershoot, pExact, pOvershoot};
    for (int i = 0; i<p.size(); i++)
    {
        float undershoot_index    = (i + (U-1)) % p.size();
        float exact_index         = (i + (U)) % p.size();
        float overshoot_index     = (i + (U+1)) % p.size();

        //cout << i << undershoot_index << exact_index << overshoot_index << q[i] << endl;

        q[ undershoot_index ]   = p[i]*temp[0] + q[ undershoot_index ];
        q[ exact_index ]        = p[i]*temp[1] + q[ exact_index ];
        q[ overshoot_index ]    = p[i]*temp[2] + q[ overshoot_index ];
    }
    return q;
}