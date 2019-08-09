1. "A ausência de uma modalidade dual suportada por hardware pode causar falhas graves em um sistema operacional. Por exemplo, o MS-DOS foi escrito para arquitetura intel 8088 que não possui bit de modalidade e, portanto, não tem modalidade dual".
Explique em que consiste a operação em modo dual e identifique pelo menos uma falha grave que pode ocorrer em um sistema que, como o MS-DOS, opere sobre uma arquitetura que não ofereça esse tipo de proteção.

2. Incluindo o processo pai inicial, quantos processos são criados pelo programa abaixo?
Desenhe a árvore de processo para justificar sua resposta.

          #include <stdio.h>
          #include <unistd.h>
          
          int main()
          {
            int I;
            
            for (I = 0; I < 4; I++)
               fork();
               
             return 0;
          }

3. Explique por que não existiam sistemas multiprogramados antes do desenvolvimento de sistemas de armazenamento de disco rígido.

4. Em arquiteturas multicore, o uso de threads é necessário para obter paralelismo real em um sistema, mas deve ser feito com cautela. O uso indiscriminado de threads pode fazer, por exemplo, com que a execução paralela de um processo consuma mais tempo do que sua execução sequencial. Discorra sobre as possíveis causas desta situação.

5. "Para ilustrar o conceito de processos cooperativos, vamos considerar o problema do produtor-consumidor que é um paradigma comum dos processo consumidor. Por exemplo, um compilador pode produzir código de montagem que é
