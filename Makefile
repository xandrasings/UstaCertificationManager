main:  Discipline.o main.o
	g++ -g -Wall -o main Discipline.o main.o

main.o: main.cpp Discipline.h
	g++ -g -Wall -c main.cpp

Discipline.o:  Discipline.cpp Discipline.h
	g++ -g -Wall -c Discipline.cpp