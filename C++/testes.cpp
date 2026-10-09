#include <iostream>
using namespace std;
int main(){
  float cat = 0;
  cout << "Welcome to the Cat Years program! This only works for cats older than 2 years old.\n";
  cout << "Enter your cat's age: \n";
  cin >> cat;
  float human = (cat - 2) * 4 + 24;
  cout << "Your cat is " << human << " years old in human years.\n";
}
