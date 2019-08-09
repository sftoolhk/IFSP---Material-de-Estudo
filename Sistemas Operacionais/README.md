# Sistemas-Operacionais
> Introduzindo conceitos de sistemas operacionais e suas funcionalidades.

# Trabalhos
1. Runtime.JS
2. NODE OS
3. GNU / HURD
4. Nest labs
5. Richard Stallman
6. XKCD - Operantions Systems / Non - sequitor
7. Explain XKCD
8. UNIX
9. MS-DOS
10. MACOS
11. Linux
12. Windows 95
13. Meltdown
14. Spectre
15. High Performance Computing
16. MPI
17. Open MP
18. CUDA
19. Tails OS
20. Subgraph OS
21. QUBES OS
22. Video Logan CIJIG: Future os OS

# Processos
> Processo é um programa em execução seja ele do sistema operacional ou de terceiros.

### Estados de um Processo
> Um processo pode ser dividido em cinco estados.

**Novo:** O processo está sendo criado.

**Em Execução:** Instruções do processo (programa) estão sendo executadas.

**Em Espera:** O processo está esperando que algm evento ocorra (como a conclusão de uma operação de I/O ou o recebimento de um sinal).

**Pronto:** O processo está esperando ser atribuído a um processador (entrar em execução).

**Concluído:** O processo terminou sua execução.

### PCB - Process control block (Bloco de controle de processo)
> O PCB serve como repositório de qaulquer informação que possa variar de um processo para o outro como informações de status de I/O, informações de contabilização, gerenciamento da memória, scheduling da CPU, registradores da CPU, contator de programa e estado do processo.


# Algoritmos de Escalonamento (Algoritmos de Scheduling)
> Entenda como funciona cada algoritmo de execução de processos de acordo com o exemplo de processos e como cada um desses algoritmos se comportariam executando os mesmos processos.

    
     Processos     |     Duração     |     Prioridade
     P1            |        2        |         2
     P2            |        1        |         1
     P3            |        8        |         4
     P4            |        4        |         2
     P5            |        5        |         3
     
*OBS:*
> 1. **TE:** será o tempo medio de espera necessário para a execução do processo.
(não para sua conclusão mais sim para o inicio do processamento.
> 2. **NP:** Será o numero de processos no algoritmo.  
     
     
     

### FCFS - First Come, First Served:
> Algoritmo organizado de acordo com a chegada dos processos, sendo o primeiro processo a chegar o primeiro a ser executado, simula uma fila por ordem de chegado.

     Exemplo de aplicação:
     
     P1    P2 P3                      P4          P5
      |--+--|--|--+--+--+--+--+--+--+--|--+--+--+--|--+--+--+--+--|
      0     2  3                       11          15             20
      
      TE = (P1 + P2 + P3 + P4 + P5) / NP 
      TE = (0 + 2 + 3 + 11 + 15) / 5
      TE = 6,2
      
### SJF - Shortest Job First
> Algoritmo ordenado de acordo com o processo com menor tempo para finalizar o job. Processos com menores tempos de conclusão são colocados em primeiro.

     Exemplo de aplicação:
     
     P2 P1    P4          P5             P3          
      |--|--+--|--+--+--+--|--+--+--+--+--|--+--+--+--+--+--+--+--|
      0  1     3           7             12                      20
      
      TE = (P2 + P1 + P4 + P5 + P3) / NP 
      TE = (0 + 1 + 3 + 7 + 12) / 5
      TE = 4,6
 
 ### Prioridade
> Algoritmo ordenado de acordo com a prioridade dos processos onde processos com prioridade 1 são os mais prioritarios e quando processos possuirem o mesmo grau de prioridade o primeiro processo a chegar será o primeiro a ser executado.

     Exemplo de aplicação:
     
     P2 P1    P4          P5             P3          
      |--|--+--|--+--+--+--|--+--+--+--+--|--+--+--+--+--+--+--+--|
      0  1     3           7             12                      20
      
      TE = (P2 + P1 + P4 + P5 + P3) / NP 
      TE = (0 + 1 + 3 + 7 + 12) / 5
      TE = 4,6
      
### Round - Robin
> Algoritmo ordenado de acordo com o processo com menor tempo para finalizar o job. Processos com menores tempos de conclusão são colocados em primeiro.

     Exemplo de aplicação:
     
     P1    P2 P3          P4          P5          P3          P5
      |--+--|--|--+--+--+--|--+--+--+--|--+--+--+--|--+--+--+--|--|
      0     2  3           7          11          15          19 20
      
      *Q = 1 Quantum 
      
      TE = (P1 + P2 + P3 + P4 + P5 + (P3) + (P5)) / NP 
      TE = (0 + 2 + 3 + 7 + 11 + (15 - 3) + (19 - 11)) / 5
      TE = 8,6
      
# Threads
> 
