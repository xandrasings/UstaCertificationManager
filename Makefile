# main:  BarrenPatch.o Land.o LandBlock.o main.o
# 	g++ -g -Wall -o main BarrenPatch.o Land.o LandBlock.o main.o

# main.o: main.cpp BarrenPatch.h Land.h LandBlock.h
# 	g++ -g -Wall -c main.cpp

# BarrenPatch.o:  BarrenPatch.cpp BarrenPatch.h
# 	g++ -g -Wall -c BarrenPatch.cpp

# Land.o:  Land.cpp Land.h
# 	g++ -g -Wall -c Land.cpp

# LandBlock.o: LandBlock.cpp LandBlock.h Land.cpp Land.h
# 	g++ -g -Wall -c LandBlock.cpp