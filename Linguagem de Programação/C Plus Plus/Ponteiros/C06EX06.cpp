//*C06EX06.CPP

#include <iostream>
using namespace std;

int main (void)
{
  int VALOR, *PVALOR, **PPONT;

  cout << "Entre um valor inteiro: ";
  cin >> VALOR;
  cin.ignore(80, '\n');

  PVALOR = &VALOR;
  PPONT = &PVALOR;

  cout << "\n Valor informado = " << **PPONT << endl;

  cout << endl;

  cout << "Tecle <ENTER> para fechar o programa: ";
  cin.get();
  return 0;
}
