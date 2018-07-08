#ifndef SIMULATE_H
#define SIMULATE_H

#include "localizer.hpp"
#include <algorithm>


class Simulation {
	
private:
	vector <char> get_colors();

public: 
	vector < vector <char> > grid;
	vector < vector <float> > beliefs;

	float blur, p_hit, p_miss, incorrect_sense_prob;

	int height, width, num_colors;
	
	std::vector<int> true_pose;
	std::vector<int> prev_pose;

	vector <char> colors;
	Simulation(vector < vector<char> >, float, float, vector <int>);

};



#endif /* SIMULATE_H */