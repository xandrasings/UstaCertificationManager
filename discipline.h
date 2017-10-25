#ifndef _DISCIPLINE_
#define _DISCIPLINE_

#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include "Discipline.h"

using namespace std;

class Discipline {
	string name;
	vector<string> requirements;
public:
	Discipline(string, vector<string>);
  void print();
	string getName();
  vector<string> getRequirements();
};

#endif // _DISCIPLINE_