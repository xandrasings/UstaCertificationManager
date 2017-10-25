main: main.o
	g++ -g -Wall Discipline.o Print.o UserInput.o main.o -o main

main.o: main.cpp Discipline.o Print.o UserInput.o
	g++ -g -Wall -c main.cpp

Discipline.o: Discipline.cpp Discipline.h Print.o
	g++ -g -Wall -c Discipline.cpp

Print.o: Print.cpp Print.h
	g++ -g -Wall -c Print.cpp

UserInput.o: UserInput.cpp UserInput.h Print.o
	g++ -g -Wall -c UserInput.cpp