#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

#include "Discipline.h"
#include "Print.cpp" 

using namespace std;

void printLine (string text) {
	cout << text << endl;
}

string getUserInput(string prompt) {
	printLine(prompt);
	string userInput;
	cin >> userInput;
	return userInput;
}

string getUserInput(string prompt, string defaultInput) {
	printLine(prompt);
	printLine("enter \'y\' for " + defaultInput);
	string userInput;
	cin >> userInput;
	if (userInput == "y") {
		userInput = defaultInput;
	}
	return userInput;
}

void presentIntroduction() {
	printLine("Welcome to Cert Manager.");
	printLine("I will help you manage certification requirements for USTA officials.");
	printLine("All source files must be in csv and should follow the expected format detailed in the readme.");
	printLine("See the readme for further details on source file requirements.");
}

vector<Discipline> getCertificationRequirements() {
	vector<Discipline> disciplines;

	string requirementsFileName = getUserInput("Enter name of requirements file.", "requirements.csv");
	ifstream requirementsFile(requirementsFileName);

	string fileLine;
	getline(requirementsFile, fileLine);
	istringstream fileLineStream( fileLine );

	string entry;
	getline( fileLineStream, entry, ',' );
	vector<string> requirementNames;

	while (fileLineStream) {
		if (!getline( fileLineStream, entry, ',' )) break;
		requirementNames.push_back(entry);
	}

	while (requirementsFile) {
		if (!getline( requirementsFile, fileLine )) break;

		Discipline newDiscipline (fileLine, requirementNames);
		disciplines.push_back(newDiscipline);
	}

	return disciplines;
}

int main() {
	presentIntroduction();
	vector<Discipline> disciplines = getCertificationRequirements();

	for (int i = 0; i < disciplines.size(); i++) {
		disciplines[i].print();
	}
}