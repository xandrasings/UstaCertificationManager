#include "Discipline.h"

using namespace std;

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