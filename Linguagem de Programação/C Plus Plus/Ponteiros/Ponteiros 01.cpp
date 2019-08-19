#include <iostream>
using namespace std;

int main(void)
{
  int IDADE = 25;
  int *PIDADE = &IDADE;

  cout << " O valor idade " << *PIDADE << "esta no ";
  cout << "endereco de memoria " << PIDADE << endl;

  cout << endl;
  cout << "tecle <ENTER> para encerrar... ";
  cin.get();
  return 0;

 }
