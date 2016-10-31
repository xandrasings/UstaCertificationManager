/* election fuss */

#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

class Event {
public:
  int size;
  bool* perm;
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
  if (Dchance > 0.5) {
    cout << name << "\t[" << 100*Dchance << "% chance of " << votes << " votes]\n";
  } else {
    cout << name << "\t[" << 100*(1-Dchance) << "% chance of " << votes << " votes]\n";

  }
}

bool operator < (const State& lhs, const State& rhs) {
  return (max(lhs.Dchance,1-lhs.Dchance) > max(rhs.Dchance,1-rhs.Dchance));
}

int main(int argc, const char* argv[]) {
  /* Parse command-line args */
  string fileName = "odds.csv";
  float riskAccepted = 0.05;
  if (argc >= 2) {
    fileName = argv[1];
  }
  if (argc >= 3) {
    riskAccepted = stof(argv[2]);
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

  sort(states.begin(),states.end());

  int DSum = 0;
  int RSum = 0;
  vector<State> givenList;
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
      states.erase(states.begin());
    } else {
      run = false;
    }
  }

  cout << "Probability of at least " << riskAccepted*100 << 
  "% that D will win " << DSum << " and R will win " << RSum <<":\n";
  cout << "Democrats win:\n";
  for (int i = 0; i < givenList.size(); i++) {
    if (givenList[i].Dchance > 0.5) {
      givenList[i].print();
    }
  }

  cout << "\nRepublicans win:" << "\n";
  for (int i = 0; i < givenList.size(); i++) {
    if (givenList[i].Dchance < 0.5) {
      givenList[i].print();
    }
  }

  float Dcount = 0;
  float Rcount = 0;

  Event event(states.size());
  run = true;
  while (run) {
    int voteSum = DSum;
    float prob = 1;

    for (int i = 0; i < event.size; i++) {
      if (event.perm[i]) {
        voteSum = voteSum + states[i].votes;
        prob = prob * states[i].Dchance;
      } else {
        prob = prob * (1 - states[i].Dchance);
      }
    }

    if (voteSum > 269) {
      Dcount = Dcount + prob;
    } else {
      Rcount = Rcount + prob;
    }

    run = event.increment();
  }

  cout << Dcount << "\t" << Rcount << "\n";
  cout << "\nGiven this assumption, " << Dcount*100 << "% chance dems win.\n";
}