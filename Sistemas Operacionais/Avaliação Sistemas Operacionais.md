### 1. Em arquitetura de multicore, o uso de threads é necessário para obter paralelismo real em um sistema, mas deve ser feito com cautela. O uso indiscriminado pode fazer, por exemplo, com que a execução paralela de um processo consuma mais tempo do que sua execução sequencial. Discorra sobre as possíveis causas desta situação.

> 

### 2. Explique por que muitos sistemas operacionais modernos são projetados sobre um modelo de kernel híbrido, incorporando características de microkernel à sua estrutura apesar do overhead gerado pela troca de mensagens com o kernel.
> Apesar do real problema de overhead causado pela troca de mensagens em sistemas microkernel isso acaba não afetando tanto sistema com um configuração por Módulos já que o modulo principal só possiu funções básicas e o conhecimento de como carregar e se comunicar com os outros modulos existentes, isso dispensa de certa forma o overhead gerado já que os módulos podem conversar entre si evitando a transmissão de mensagem.


### 3. Considere o conjunto de processos a seguir, com a duração do pico de CPU dada em milissegundos.
     
       Processo    |    Duração do pico    |    Prioridade
       P1          |          10           |        3
       P2          |           1           |        1
       P3          |           2           |        3
       P4          |           1           |        4
       P5          |           5           |        2
     
     
- Presume-se que os processos tenham chegado na ordem P1, P2, P3, P4, P5, todos no momento 0, e um número de prioridade menor implique uma prioridade mais alta.

a. Calcule o tempo de espera de cada processo para os algoritmos de escalonamento a seguir: FCFS, SJF, por prioridade sem preempção e Round Robin (quantum = 1).

      
      TE - Tempo de espera / NP - Numero de processos
      
      =============================================================================
      ---------------------------------- FCFS -------------------------------------
      =============================================================================
      
      
      P1                                      P2  P3      P4  P5
      |---+---+---+---+---+---+---+---+---+---|---|---+---|---|---+---+---+---+---|
      0                                      10  11      13  14                  19
      
      TE = (P1 + P2 + P3 + P4 + P5)/NP
      TE = (0 + 10 + 11 + 13 + 14)/5
      TE = 9,6
      
      =============================================================================
      ----------------------------------- SJF -------------------------------------
      =============================================================================
      
      
      P2  P4  P3      P5                  P1
      |---|---|---+---|---+---+---+---+---|---+---+---+---+---+---+---+---+---+---|
      0   1   2       4                   9                                      19
      
      TE = (P2 + P4 + P3 + P5 + P1)/NP
      TE = (0 + 1 + 2 + 4 + 9)/5
      TE = 3,2
      
      
      =============================================================================
      -------------------------------- Prioridade ---------------------------------
      =============================================================================
      
      
      P2  P5                  P1                                      P3      P4
      |---|---+---+---+---+---|---+---+---+---+---+---+---+---+---+---|---+---|---|
      0   1                   6                                      16      18  19
      
      TE = (P2 + P5 + P1 + P3 + P4)/NP
      TE = (0 + 1 + 6 + 16 + 18)/5
      TE = 8
      
      
      =============================================================================
      ------------------------------- Round Robin ---------------------------------
      =============================================================================
      
      
      P1              P2  P3      P4  P5              P1              P5  P1
      |---+---+---+---|---|---+---|---|---+---+---+---|---+---+---+---|---|---+---|
      0               4   5       7   8              12              16  17      19
      
      TE = (P1 + P2 + P3 + P4 + P5)/NP
      TE = ((8 + 1) + (4) + (5) + (7) + (8 + 4))/5
      TE = 7
      
b. Qual dos algoritmos resulta no menor tempo médio de espera?    

> O algoritmo SJF resulta em um tem de 3,2 ms sendo o menor tempo.
__________________________________________________________________________________________________________________________________



### 4. No sistema operacional UNIX, o processo filho, criado a partir da chamada fork(), herda atributos de escalonamento, arquivos abertos e segmentos de memória compartilhada do pai. Neste cenário, e considerando que o processo pai tenha arquivos abertos e segmentos de memória compartilhada que serão herdados pelo filho, descreva os problemas que podem ocorrer caso o processo pai não execuute a chamada wait() após a chamda fork(). Lembre que a chamada wait() faz com que o processo pai permaneça no estado bloqueado até o encerramento do filho.

### 5. Explique como os critérios de escalonamento "utilização de CPU" e "Tempo de resposta" entram em conflito em certas configurações.


     
