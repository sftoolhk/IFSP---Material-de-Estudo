# CLASS   X   STRUCT
> Em C++ class e struct são os dois registros tendo apenas uma pequena diferença no momento de sua aplicação.
Quando se quer que os métodos sejam privados é recomendado o uso de class, já em casos que não á a necessidade o uso de struct é o mais recomendado.

    Class                    X                    Struct
    
    - possui método                      possui método -
    - possui encapsulamento      possui encapsulamento -
    {com padrão privado}            {com padrão publico}


# Bibliotecas
- <iostream>
- <iomanip>
- <cstdlib>
- <ctime>

# Comandos
- atof ( Biblioteca <cstdlib>) converte da tabela ASCII para um Float Real
- atoi ( Biblioteca <cstdlib>) converte da tabela ASCII para um inteiro
- atol ( Biblioteca <cstdlib>) converte da tabela ASCII para um Long

- 

# Estudo CPP

Setiosflags habilita comandos da biblioteca <iomanip> exemplo:
  EX;
  int main(void)
{
  cout << "10 em decimal     = " << dec << 10 << endl;
  cout << "\n";
  cout << "10 em octal       = " << oct << 10 << endl;
  cout << "10 em hexadecimal = " << hex << 10 << endl;
  cout << setiosflags(ios::uppercase);
  cout << "\n";
  cout << "10 em octal       = " << oct << 10 << endl;
  cout << "10 em hexadecimal = " << hex << 10 << endl;
  cout << resetiosflags(ios::uppercase);
  cout << setiosflags(ios::showbase);
  cout << "\n";
  cout << "10 em octal       = " << oct << 10 << endl;
  cout << "10 em hexadecimal = " << hex << 10 << endl;
  cout << resetiosflags(ios::showbase);
  cout << setiosflags(ios::uppercase);
  cout << "\n";
  
  
  
  Showbase - mostra a base em que o numero está, adiciona ao numero uma forma de representação
  ex: 0x para hexa, 0 antes do numeto para octa


Operadores pré-definidos/pós -definidos
  ++ - Adição sucessiva (Acrescenta "1" ao valor existente)
  -- - Subtração sucessiva ( decrementa "1" ao valor existente)
  
  PRÉ-DEFINIDO
  
 ++X - (Soma "1" no valor de "x" antes de acessar "x".)
 
 
 PÓS-DEFINIDO
 
 X++ - (Soma "1" em "x" após acessar "x".)
 
 
 # DESIÇÃO SELETIVA
 
 Exemplo de ação com switch:
 // C03EX12.CPP

#include <iostream>
using namespace std;

int main(void)
{

  int MES;

  cout << "Entre um numero equivalente a um MES: ";
  cin >> MES;
  cin.ignore(80, '\n');

  cout << endl;

  switch (MES)
    {
      case  1: cout << "Janeiro";      break;
      case  2: cout << "Fevereiro";    break;
      case  3: cout << "Marco";        break;
      case  4: cout << "Abril";        break;
      case  5: cout << "Maio";         break;
      case  6: cout << "Junho";        break;
      case  7: cout << "Julho";        break;
      case  8: cout << "Agosto";       break;
      case  9: cout << "Setembro";     break;
      case 10: cout << "Outubro";      break;
      case 11: cout << "Novembro";     break;
      case 12: cout << "Dezembro";     break;
      default: cout << "Mes invalido"; break;
    }
  cout << endl << endl;

  cout << "Tecle <Enter> para encerrar... ";
  cin.get();
  return 0;
}

Do while é obrigatorio o bloco {}
Para funções não usar espaçamento:
ex: cin.get() sem espaçamento entre ( cin.get e ())


# Passagem de Parâmetro

### Parâmetro formal

Quando dentro da subrotina, o parâmetro passado para á mesma é um parâmetro formal.

### Parâmetro Real

Quando dentro do Rotina Main ou rotina que envia o parametro, esse mesmo é um parametro Real.

### Passagem de parâmetro VALOR

### Passagem de parâmetro REFÊRENCIA

Para passagem de parâmetro por Refêrencia é necessário colocar um & (e cormecial).
EX:
int FAT
void fatorial(int N, long int *&FAT*)

### Função

É preciso dar um return na variavel á qual se quer u, retorno de valor:
EX:

int fatorial(int N)
{
  int I, FAT = 1;
  for (I = 1; I <= N; I++)
    FAT *= I;
  return FAT;

É possivel elabora equações dentro do return:

bool compara(int A, int B)
{
  return (A == B);
}


### Criando Bibliotecas

Toda biblioteca possui dois arquivos - comercial
1 - Arquivo de cabeçalho (.h)
2 - Arquivo de código (.cpp)
Os dois devem ser vinculados.

Comando para limpar tela (sistema operacional linux) na linguagem CPP
cout << "\033[2]"

Bibliotecas proprias devem ser involtas por "" (aspas)
EX:
#include "minhabiblioteca.h"

Para executar o programa no Prompt de Comando é necessário fazer a execução da seguinte linha:
g++ -std=c==17 NOME_DO_PROGRAMA.CPP NOME_BIBLIOTECA.CPP -o NOME_PROG.EXE


 
 
