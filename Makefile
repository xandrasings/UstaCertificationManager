main: Discipline.o Print.o main.o
	g++ -g -Wall Discipline.o Print.o main.o -o main

main.o: main.cpp Discipline.o Print.o
	g++ -g -Wall -c main.cpp

Discipline.o: Discipline.cpp Discipline.h Print.o
	g++ -g -Wall -c Discipline.cpp

Print.o: Print.cpp Print.h
	g++ -g -Wall -c Print.cpp