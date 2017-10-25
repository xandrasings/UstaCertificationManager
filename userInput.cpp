#include "UserInput.h"
#include "Print.h"

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