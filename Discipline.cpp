#include "Discipline.h"
#include "Print.h"

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
	printLine("Discipline:");
	printSplitLight();
	printLine("Name:");
	printLine(name);
	printLine("Requirements:");
	for (int i = 0; i < requirements.size(); i++) {
		printLine(requirements[i]);
	}
	printSplitHeavy();
}

string Discipline::getName () {
  return name;
}

vector<string> Discipline::getRequirements () {
  return requirements;
}