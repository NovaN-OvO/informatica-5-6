#include <iostream>
int main(){
  std::string username;
  std::cout << "Enter your name: ";
  std::cin >> username;
  std::cout << username;
  int month1 = 0;
  int month2 = 0;
  std::cout << "Enter the first month: \n";
  std::cin >> month1;
  std::cout << "\nEnter the second month: ";
  std::cin >> month2;
  double mom = ((month2 - month1) / month1) * 100;
  std::cout << mom;
}
