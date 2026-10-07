#include <iostream>
int main(){
  double cat = 0;
  std::cout << "Welcome to the Cat Years program! This only works for cats older than 2 years old.\n";
  std::cout << "Enter your cat's age: \n";
  std::cin >> cat;
  double human = (cat - 2) * 4 + 24;
  std::cout ; "Your cat is" << double human << "years old in human years\n";
}
