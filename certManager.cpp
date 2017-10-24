/* election fuss */

#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

void print(string text) {
  cout << text << endl;
}

void presentIntroduction() {
  print("Welcome to Cert Manager.");
  print("I will help you manage certification requirements for USTA officials.");
  print("All source files must be in csv and should follow the expected format detailed in the readme.");
  print("See the readme for further details on source file requirements.");
}

void processInputs() {
  cout << "Enter Name of file .\n";
}

int main() {
  presentIntroduction();
  processInputs();
}