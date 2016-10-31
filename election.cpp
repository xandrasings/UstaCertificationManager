/* election fuss */

#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <array>

using namespace std;

class Event {
  int size;
  bool* perm;
public:
  Event (int);
  ~Event ();
  bool increment ();
  void print ();
};

Event::Event (int set) {
  size = set;
  perm = new bool[size];
  for (int i = 0; i < size; i++) {
    perm[i]=false;
  }
}

Event::~Event () {
  delete [] perm;
}

bool Event::increment () {
  int cursor = size-1;
  while (perm[cursor] == 1) {
    perm[cursor] = 0;
    cursor--;
    if (cursor < 0) {return false;}
  }
  perm[cursor] = 1;
  return true;
}

void Event::print () {
  cout << "[";
  for (int i = 0; i < size; i++) {
    cout << perm[i];
    if (i < size-1) {
      cout << ", ";
    }
  }
  cout << "]" << "\n";
}

class State {
public:
  string name;
  int votes;
  float Dchance;
  State(string, int, float);
  State(string);
  void print();
};

State::State (string n, int v, float c) {
  name = n;
  votes = v;
  Dchance = c;
}

State::State (string line) {
  name = line.substr(0,line.find(","));
  votes = stoi(line.substr(line.find(",")+1,line.rfind(",")-line.find(",")-1));
  Dchance = stof(line.substr(line.rfind(",")+1,line.find("%")-line.find(",")-1))*0.01;
}

void State::print () {
  cout << name << ",\t" << votes << ",\t" << Dchance*100 << "%\n";
}

bool operator < (const State& lhs, const State& rhs) {
  return (max(lhs.Dchance,1-lhs.Dchance) < max(rhs.Dchance,1-rhs.Dchance));
}

int main(int argc, const char* argv[]) {
  /* Parse command-line args */
  string fileName = "odds.csv";
  if (argc == 2) {
    fileName = argv[1];
  }
  ifstream dataFile(fileName);

  vector<State> states;
  string line;
  int del1, del2;

  getline(dataFile, line, '\n');
  while(getline(dataFile, line, '\n')) {
    State newState(line);
    states.push_back(newState);
  }

  sort(states.rbegin(),states.rend());
  for (int i=0; i<states.size(); i++) {
    states[i].print();
  }

  int DSum = 0;
  int RSum = 0;
  vector<State> givenList;
  float riskAccepted = 0.50;
  float riskProduct = 1;
  bool run = true;

  while(run) {
    bool lead;
    if (states[0].Dchance > 0.5) {
      lead = true;
    } else {
      lead = false;
    }

    float riskAdded;
    if (lead) {
      riskAdded = states[0].Dchance;
    } else {
      riskAdded = 1-states[0].Dchance;
    }
    if (riskProduct * riskAdded > riskAccepted) {
      riskProduct = riskProduct * riskAdded;
      givenList.push_back(states[0]);
      if (lead) {
        DSum = DSum + states[0].votes;
      } else {
        RSum = RSum + states[0].votes;
      }
      DSum = DSum + states[0].votes;
      states.erase(states.begin());
    } else {
      run = false;
    }
  }

  cout << "Probability of at least " << riskAccepted*100 << 
  "% that D will win " << DSum << " and R will win " << RSum << 
  " from the following: " << "\n";
  for (int i = 0; i < givenList.size(); i++) {
    givenList[i].print();
  }
  cout << "\n" << "\n" << "\n" << "\n";
  for (int i = 0; i < states.size(); i++) {
    states[i].print();
  }


  Event event(5);
  // event.print();
  while (event.increment()) {
    // event.print();
  }
  
}