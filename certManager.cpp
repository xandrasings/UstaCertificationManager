/* election fuss */

#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

class Discipline {
public:
  string name;
  vector<string> requirements;
  Discipline(string, vector<string>);
};

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

  cout << "adding discipline: " << name << endl;
  cout << "requirements: " << endl;
  for (int n = 0; n < requirements.size(); n++) {
    cout << requirements[n] << ", ";
  }
  cout << endl;
  cout << endl;
  cout << endl;

};

void print(string text) {
  cout << text << endl;
}

string getUserInput(string prompt) {
  print(prompt);
  string userInput;
  cin >> userInput;
  return userInput;
}

string getUserInput(string prompt, string defaultInput) {
  print(prompt);
  print("enter \'y\' for " + defaultInput);
  string userInput;
  cin >> userInput;
  if (userInput == "y") {
    userInput = defaultInput;
  }
  return userInput;
}

void presentIntroduction() {
  print("Welcome to Cert Manager.");
  print("I will help you manage certification requirements for USTA officials.");
  print("All source files must be in csv and should follow the expected format detailed in the readme.");
  print("See the readme for further details on source file requirements.");
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
  
}