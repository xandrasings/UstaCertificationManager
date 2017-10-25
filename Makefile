main:  Discipline.o Print.o main.o
	g++ -g -Wall -o main Discipline.o Print.o main.o

main.o: main.cpp Discipline.h Print.cpp
	g++ -g -Wall -c main.cpp

Discipline.o:  Discipline.cpp Discipline.h
	g++ -g -Wall -c Discipline.cpp

Print.o:  Print.cpp
	g++ -g -Wall -c Print.cpp