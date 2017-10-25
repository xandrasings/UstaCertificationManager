#include "Discipline.h"

Discipline::Discipline (string fileLine, vector<string> requirementNames) {
	istringstream fileLineStream( fileLine );

	getline( fileLineStream, name, ',' );

	int i = 0;
	string required;
	while (getline( fileLineStream, required, ',' )) {
		if(required == "1") {
			requirements.push_back(requirementNames[i]);
		}
		i++;
	}
}

void Discipline::print () {
	cout << "Discipline" << endl;
	cout << "============================================" << endl;
	cout << "============================================" << endl;
}

string Discipline::getName () {
  return name;
}

vector<string> Discipline::getRequirements () {
  return requirements;
}