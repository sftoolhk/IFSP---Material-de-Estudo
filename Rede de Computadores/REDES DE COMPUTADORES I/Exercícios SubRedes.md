### Atividade 
**Identificar nos exercícios os seguintes dados:**
- Nº de Hosts válidos;
- Nº de hosts válidos para cada subrede;
- Intervalo válido das subredes;
- Endereço de rede e broadcast de cada subrede;
- Máscara resultante;

### Exercícios:
     
     1 - 192.168.020.199/24    -   03 bits para rede
     
         Endereço IP ........................: 11000000.10101000.00010100.11000111
         Endereço de Máscara ................: 11111111.11111111.11111111.00000000
         Hosts válidos ......................: (2 ↑ 8) - 2 = 254 válidos
         Numero de subredes .................: (2 ↑ 3) - 2 = 6 subredes válidas
         Intervalo de SubRedes ---------------------------------------------------
         
         11000000.10101000.00010100.000 --| 00000 { NA }
                 Essa faixa de endereço representa o endereço de rede
                 da máscara padrão sem aplicação de subrede.
         
                                          | 00000 { Endereço de rede }
         11000000.10101000.00010100.001 --| 00001 á 11110 / (2 ↑ 5) - 2 = 30 Hosts 
                                          | 11111 { Broadcast }
         host válidos ....................: 192.168.020.033  /  192.168.020.062
         Endereço de rede / broadcast ....: 192.168.020.032  /  192.168.020.063  
         
         
                                          | 00000 { Endereço de rede }
         11000000.10101000.00010100.010 --| 00001 á 11110 / (2 ↑ 5) - 2 = 30 Hosts
                                          | 11111 { Broadcast }
         host válidos ....................: 192.168.020.065  /  192.168.020.094
         Endereço de rede / broadcast ....: 192.168.020.064  /  192.168.020.095  
         
                                          | 00000 { Endereço de rede }
         11000000.10101000.00010100.011 --| 00001 á 11110 / (2 ↑ 5) - 2 = 30 Hosts
                                          | 11111 { Broadcast }
         host válidos ....................: 192.168.020.097  /  192.168.020.126
         Endereço de rede / broadcast ....: 192.168.020.096  /  192.168.020.127 
         
                                          | 00000 { Endereço de rede }
         11000000.10101000.00010100.100 --| 00001 á 11110 / (2 ↑ 5) - 2 = 30 Hosts
                                          | 11111 { Broadcast }
         host válidos ....................: 192.168.020.129  /  192.168.020.158
         Endereço de rede / broadcast ....: 192.168.020.128  /  192.168.020.159  
         
                                          | 00000 { Endereço de rede }
         11000000.10101000.00010100.101 --| 00001 á 11110 / (2 ↑ 5) - 2 = 30 Hosts
                                          | 11111 { Broadcast }
         host válidos ....................: 192.168.020.161  /  192.168.020.190
         Endereço de rede / broadcast ....: 192.168.020.160  /  192.168.020.191  
         
                                          | 00000 { Endereço de rede }
         11000000.10101000.00010100.110 --| 00001 á 11110 / (2 ↑ 5) - 2 = 30 Hosts
                                          | 11111 { Broadcast }
         host válidos ....................: 192.168.020.193  /  192.168.020.222
         Endereço de rede / broadcast ....: 192.168.020.192  /  192.168.020.223  
                                          
         11000000.10101000.00010100.111 --| 00000 { NA }
                 Essa faixa de endereço representa o Broadcast da
                 máscara padrão sem aplicação de subrede.
         ___________________________________________________________________________________
         
         Intervalo válido de subredes .......: 192.168.20.32 á 192.168.20.192
         Soma dos Hosts válidos .............: 6 * 30 = 180 Hosts válidos
         Máscara Resultante .................: 11111111.11111111.11111111.11100000
                                               255.255.255.224
     
     2 - 200.251.232.168/16    -   10 bits para rede
          
         Endereço IP ........................: 11001000.11111001.11101000.10101000
         Endereço de Máscara ................: 11111111.11111111.00000000.00000000
         Hosts válidos ......................: (2 ↑ 16) - 2 = 65.534 válidos
         Numero de subredes .................: (2 ↑ 10) - 2 = 1.022 subredes válidas
         Intervalo de SubRedes --------------------------------------------------------------
         
         11001000.11111001.00000000.00 --| 000000 { NA }
                 Essa faixa de endereço representa o endereço de rede
                 da máscara padrão sem aplicação de subrede.
         
                                         | 000000 { Endereço de rede }
         11001000.11111001.00000000.01 --| 000001 á 111110 / (2 ↑ 6) - 2 = 62 Hosts 
                                         | 111111 { Broadcast }
         host válidos ....................: 200.251.000.065  /  200.251.000.126
         Endereço de rede / broadcast ....: 200.251.000.064  /  200.251.000.127
         
                                         | 000000 { Endereço de rede }
         11001000.11111001.00000000.10 --| 000001 á 111110 / (2 ↑ 6) - 2 = 62 Hosts 
                                         | 111111 { Broadcast }
         host válidos ....................: 200.251.000.129  /  200.251.000.190
         Endereço de rede / broadcast ....: 200.251.000.128 /  200.251.000.191
         
                                         | 000000 { Endereço de rede }
         11001000.11111001.00000000.11 --| 000001 á 111110 / (2 ↑ 6) - 2 = 62 Hosts 
                                         | 111111 { Broadcast }
         host válidos ....................: 200.251.000.193  /  200.251.000.254
         Endereço de rede / broadcast ....: 200.251.000.192  /  200.251.000.255
         
                                         | 000000 { Endereço de rede }
         11001000.11111001.00000001.00 --| 000001 á 111110 / (2 ↑ 6) - 2 = 62 Hosts 
                                         | 111111 { Broadcast }
         host válidos ....................: 200.251.001.001  /  200.251.001.62
         Endereço de rede / broadcast ....: 200.251.001.000  /  200.251.001.63
         
                                         | 000000 { Endereço de rede }
         11001000.11111001.00000001.01 --| 000001 á 111110 / (2 ↑ 6) - 2 = 62 Hosts 
                                         | 111111 { Broadcast }
         host válidos ....................: 200.251.001.065  /  200.251.001.126
         Endereço de rede / broadcast ....: 200.251.001.064  /  200.251.001.127
         
                                         | 000000 { Endereço de rede }
         11001000.11111001.00000001.10 --| 000001 á 111110 / (2 ↑ 6) - 2 = 62 Hosts 
                                         | 111111 { Broadcast }
         host válidos ....................: 200.251.001.129  /  200.251.001.190
         Endereço de rede / broadcast ....: 200.251.001.128  /  200.251.001.191
                                         
                                         | 000000 { Endereço de rede }
         11001000.11111001.00000001.11 --| 000001 á 111110 / (2 ↑ 6) - 2 = 62 Hosts 
                                         | 111111 { Broadcast }
         host válidos ....................: 200.251.001.193  /  200.251.001.254
         Endereço de rede / broadcast ....: 200.251.001.192  /  200.251.001.255
                                         .
                                         .
                                         .                                   
                                         | 000000 { Endereço de rede }
         11001000.11111001.11111111.10 --| 000001 á 111110 / (2 ↑ 6) - 2 = 62 Hosts 
                                         | 111111 { Broadcast }
         host válidos ....................: 200.251.255.129  /  200.251.255.254
         Endereço de rede / broadcast ....: 200.251.255.128  /  200.251.255.255
                                         
         11001000.11111001.11111111.11 --| 111111 { NA }
                 Essa faixa de endereço representa o Broadcast da
                 máscara padrão sem aplicação de subrede.
         ________________________________________________________________________________        
         
         Intervalo válido de subredes .......: 200.251.0.64 á 200.251.255.190                               
         Soma dos Hosts válidos .............: 1.022 * 62 =  63.364 Hosts válidos
         Máscara Resultante .................: 11111111.11111111.11111111.11000000
                                               255.255.255.192
         
     3 - 172.163.200.030/16    -   04 bits para rede
         
         Endereço IP ........................: 10101100.10100011.11001000.00011110
         Endereço de Máscara ................: 11111111.11111111.00000000.00000000
         Hosts válidos ......................: (2 ↑ 16) - 2 = 65.534 válidos
         Numero de subredes .................: (2 ↑ 4) - 2 = 14 subredes válidas
         Intervalo de SubRedes --------------------------------------------------------------
         
         10101100.10100011.0000 --| 0000.00000000 { NA }
                 Essa faixa de endereço representa o endereço de rede
                 da máscara padrão sem aplicação de subrede.
         
                                  | 0000.00000000 { Endereço de rede }
         10101100.10100011.0001 --| 0000.00000001 á 1111.11111110 / (2 ↑ 12) - 2 = 4.094 Hosts 
                                  | 1111.11111111 { Broadcast }
         host válidos ....................: 127.163.016.001  /  127.163.031.254
         Endereço de rede / broadcast ....: 127.163.016.000  /  127.163.031.255
         
                                  | 0000.00000000 { Endereço de rede }
         10101100.10100011.0010 --| 0000.00000001 á 1111.11111110 / (2 ↑ 12) - 2 = 4.094 Hosts 
                                  | 1111.11111111 { Broadcast }
         host válidos ....................: 127.163.032.001  /  127.163.047.254
         Endereço de rede / broadcast ....: 127.163.032.000  /  127.163.047.255

                                  | 0000.00000000 { Endereço de rede }
         10101100.10100011.0011 --| 0000.00000001 á 1111.11111110 / (2 ↑ 12) - 2 = 4.094 Hosts 
                                  | 1111.11111111 { Broadcast }
         host válidos ....................: 127.163.048.001  /  127.163.063.254
         Endereço de rede / broadcast ....: 127.163.048.000  /  127.163.063.255
         
                                  | 0000.00000000 { Endereço de rede }
         10101100.10100011.0100 --| 0000.00000001 á 1111.11111110 / (2 ↑ 12) - 2 = 4.094 Hosts 
                                  | 1111.11111111 { Broadcast }
         host válidos ....................: 127.163.064.001  /  127.163.079.254
         Endereço de rede / broadcast ....: 127.163.064.000  /  127.163.079.255
         
                                  | 0000.00000000 { Endereço de rede }
         10101100.10100011.0101 --| 0000.00000001 á 1111.11111110 / (2 ↑ 12) - 2 = 4.094 Hosts 
                                  | 1111.11111111 { Broadcast }
         host válidos ....................: 127.163.080.001  /  127.163.095.254
         Endereço de rede / broadcast ....: 127.163.080.000  /  127.163.095.255
         
                                  | 0000.00000000 { Endereço de rede }
         10101100.10100011.0110 --| 0000.00000001 á 1111.11111110 / (2 ↑ 12) - 2 = 4.094 Hosts 
                                  | 1111.11111111 { Broadcast }
         host válidos ....................: 127.163.096.001  /  127.163.111.254
         Endereço de rede / broadcast ....: 127.163.096.000  /  127.163.111.255
                                  
                                  | 0000.00000000 { Endereço de rede }
         10101100.10100011.0111 --| 0000.00000001 á 1111.11111110 / (2 ↑ 12) - 2 = 4.094 Hosts 
                                  | 1111.11111111 { Broadcast }
         host válidos ....................: 127.163.096.001  /  127.163.111.254
         Endereço de rede / broadcast ....: 127.163.096.000  /  127.163.111.255
         
                                  | 0000.00000000 { Endereço de rede }
         10101100.10100011.1000 --| 0000.00000001 á 1111.11111110 / (2 ↑ 12) - 2 = 4.094 Hosts 
                                  | 1111.11111111 { Broadcast }
                  
                                  | 0000.00000000 { Endereço de rede }
         10101100.10100011.1001 --| 0000.00000001 á 1111.11111110 / (2 ↑ 12) - 2 = 4.094 Hosts 
                                  | 1111.11111111 { Broadcast }
         
                                  | 0000.00000000 { Endereço de rede }
         10101100.10100011.1010 --| 0000.00000001 á 1111.11111110 / (2 ↑ 12) - 2 = 4.094 Hosts 
                                  | 1111.11111111 { Broadcast }
         
                                  | 0000.00000000 { Endereço de rede }
         10101100.10100011.1011 --| 0000.00000001 á 1111.11111110 / (2 ↑ 12) - 2 = 4.094 Hosts 
                                  | 1111.11111111 { Broadcast }
         
                                  | 0000.00000000 { Endereço de rede }
         10101100.10100011.1100 --| 0000.00000001 á 1111.11111110 / (2 ↑ 12) - 2 = 4.094 Hosts 
                                  | 1111.11111111 { Broadcast }
         
                                  | 0000.00000000 { Endereço de rede }
         10101100.10100011.1101 --| 0000.00000001 á 1111.11111110 / (2 ↑ 12) - 2 = 4.094 Hosts 
                                  | 1111.11111111 { Broadcast }
         
                                  | 0000.00000000 { Endereço de rede }
         10101100.10100011.1110 --| 0000.00000001 á 1111.11111110 / (2 ↑ 12) - 2 = 4.094 Hosts 
                                  | 1111.11111111 { Broadcast }

         10101100.10100011.1111 --| 1111.11111111 { NA }
                 Essa faixa de endereço representa o Broadcast da
                 máscara padrão sem aplicação de subrede.
         ________________________________________________________________________________        
         
         Intervalo válido de subredes .......: 172.163.16.0 á 172.163.224                             
         Soma dos Hosts válidos .............: 14 * 4.094 =  16.376 Hosts válidos
         Máscara Resultante .................: 11111111.11111111.11110000.00000000
         
     4 - 010.020.030.040/24    -   06 bits para rede
         
         Endereço IP ........................: 00001010.00010100.00011110.00101000
         Endereço de Máscara ................: 11111111.11111111.11111111.00000000
         Hosts válidos ......................: (2 ↑ 8) - 2 = 254 válidos
         Numero de subredes .................: (2 ↑ 6) - 2 = 62 subredes válidas
         Intervalo de SubRedes --------------------------------------------------------------
         
         00001010.00010100.00011110.000000 --| 00 { NA }
                 Essa faixa de endereço representa o endereço de rede
                 da máscara padrão sem aplicação de subrede.
         
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.000001 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.000010 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.000011 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.000100 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.000101 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.000110 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.000111 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.001000 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                  
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.001001 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.001010 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.001011 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.001100 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.001101 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.001110 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.001111 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.010000 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.010001 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
         
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.010010 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.010011 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.010100 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.010101 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.010110 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.010111 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.011000 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.011001 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.011010 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.011011 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.011100 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.011101 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.011110 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.011111 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.100001 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.100010 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.100011 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.100100 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.100101 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.100110 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.100111 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.101000 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                  
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.101001 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.101010 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.101011 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.101100 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.101101 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.101110 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.101111 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.110000 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.110001 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
         
                                                      | 00 { Endereço de rede }
         00001010.00010100.00011110.110010 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.110011 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.110100 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.110101 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.110110 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.110111 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.111000 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.111001 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.111010 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                                      
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.111011 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.111100 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.111101 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
                                             | 00 { Endereço de rede }
         00001010.00010100.00011110.111110 --| 01 á 10 / (2 ↑ 2) - 2 = 2 Hosts 
                                             | 11 { Broadcast }
                                             
         00001010.00010100.00011110.111111 --| 11 { NA }
                 Essa faixa de endereço representa o Broadcast da
                 máscara padrão sem aplicação de subrede.
         ________________________________________________________________________________        
         
         Intervalo válido de subredes .......: 10.20.30.4 á 10.20.30.252                           
         Soma dos Hosts válidos .............: 62 * 2 =  128 Hosts válidos
         Máscara Resultante .................: 11111111.11111111.11111111.11111100
         
     5 - 199.189.149.031/24    -   02 bits para rede
     
         Endereço IP ........................: 11000111.10111101.10010101.00011111
         Endereço de Máscara ................: 11111111.11111111.11111111.00000000
         Hosts válidos ......................: (2 ↑ 8) - 2 = 254 válidos
         Numero de subredes .................: (2 ↑ 2) - 2 = 2 subredes válidas
         Intervalo de SubRedes ---------------------------------------------------
         
         11000111.10111101.10010101.00 --| 000000 { NA }
                 Essa faixa de endereço representa o endereço de rede
                 da máscara padrão sem aplicação de subrede.
         
                                         | 000000 { Endereço de rede }
         11000111.10111101.10010101.01 --| 000001 á 111110 / (2 ↑ 6) - 2 = 62 Hosts 
                                         | 111111 { Broadcast }
         
                                         | 000000 { Endereço de rede }
         11000111.10111101.10010101.10 --| 000001 á 111110 / (2 ↑ 6) - 2 = 62 Hosts 
                                         | 111111 { Broadcast }
         
         11000111.10111101.10010101.11 --| 111111 { NA }
                 Essa faixa de endereço representa o Broadcast da
                 máscara padrão sem aplicação de subrede.
         ___________________________________________________________________________________
         
         Intervalo válido de subredes .......: 199.189.149.64 á 199.189.149.128
         Soma dos Hosts válidos .............: 2 * 62 = 128 Hosts válidos
         Máscara Resultante .................: 11111111.11111111.11111111.11000000
