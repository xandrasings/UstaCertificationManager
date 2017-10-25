main: main.o
	g++ -g -Wall print.o userInput.o discipline.o setUpHandler.o main.o -o main

main.o: main.cpp print.o userInput.o discipline.o setUpHandler.o
	g++ -g -Wall -c main.cpp

print.o: print.cpp print.h
	g++ -g -Wall -c print.cpp

userInput.o: userInput.cpp userInput.h print.o
	g++ -g -Wall -c userInput.cpp

discipline.o: discipline.cpp discipline.h print.o
	g++ -g -Wall -c discipline.cpp

setUpHandler.o: setUpHandler.cpp setUpHandler.h print.o userInput.o
	g++ -g -Wall -c setUpHandler.cpp