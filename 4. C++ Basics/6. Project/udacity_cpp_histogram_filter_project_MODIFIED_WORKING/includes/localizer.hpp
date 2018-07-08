#ifndef LOCALIZER_H
#define LOCALIZER_H

#include "helpers.hpp"
#include <stdlib.h>
#include "debugging_helpers.hpp" 


vector< vector <float> > initialize_beliefs(vector< vector <char> > grid);

vector< vector <float> > sense(char color, 
	vector< vector <char> > grid, 
	vector< vector <float> > beliefs, 
	float p_hit,
	float p_miss);

vector< vector <float> > move(int dy, int dx, 
	vector < vector <float> > beliefs,
	float blurring);

#endif /* LOCALIZER_H */