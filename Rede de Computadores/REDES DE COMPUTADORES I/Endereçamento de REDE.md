# Endereçamento IP
> O endereço IP é um identificador numérico designado a cada dispositivo conectado a um rede IP.
O endereço IP é um endereço lógico e não físico.

**Intervalo de endereços validos**
> Vai de um acima do endereço de rede até um abaxio do endereço de brodcast.

**Endereço de Broadcast (broadcast address):**
> Endereço usado por aplicações e dispositivos para o envio de mensagens a todos os dispositivos de uma rede, simultaneamente(1-to-all).

**Endereço de Multicast (Multicast address):**
> Endereço usado por uma máquina para alcançar um grupo definido de máquinas (1-to-many).

**Unicast (Unicast address):**
> Comunicação de uma máquina para apenas outra máquina (1-to-1).

### Modelo hierárquico de Endereço
> Esse modelo é dividido em três níveis sendo eles:

     1º. REDE:
     identifica uma grande área.
          2º. SUBNET:
          Já é mais específica e define a área de chamada.
               3º. HOST:
               Identifica o número do cliente na rede.

### Identificador de Classe (A, B ou C)
> No primeiro Byte de um endereço sempre será definido tipo de classe de Endereço, a mascará de rede pode definir um classe A por exemplo como sendo em modo de uso classe C como no exemplo:

     10.20.10.30 - Endereço IP
     255.255.255.0 - Mascará de rede
     
*Isso faz com que mesmo sendo endereço IP classe A ele irá trabalhar como um classe C, sendo que seus 3 primeiros octedos serão "transferidos" para a REDE retirando espaço do HOST.*

### Como são divididos as Classes de endereços ?

**Classe A:**
     
     Em um endereço de classe A teremos 1 byte (1 octeto) para endereço de REDE e 3 bytes (3 octetos)
     para HOST e possiveis endereços de SUBNET sendo então (2↑24)-2 (-2 são os endereços de REDE e de BROADCAST
     que devem ser descontados), e seu primeiro bit do primeiro byte sempre será 0. Sendo assim o intervalo de
     endereçamentos no primeiro byte de um endereçamento classe A será de 0 - 127.
     
     |  REDE  |  HOST  |  HOST  |  HOST  |    -   Endereço classe A.
     
**Classe B:**

     Em um endereço de classe B teremos 2 byte (2 octeto) para endereço de REDE e 2 bytes (2 octetos)
     para HOST e possiveis endereços de SUBNET sendo então (2↑16)-2 (-2 são os endereços de REDE e de BROADCAST
     que devem ser descontados), em seu primeiro Byte o primeiro bit será sempre 1 e o segundo bit sempre será 0.
     Sendo assim o intervalo de endereçamentos no primeiro byte de um endereçamento classe B será de 128 - 191.
     
     |  REDE  |  REDE  |  HOST  |  HOST  |    -   Endereço classe B.
     
**Classe C:**

     Em um endereço de classe C teremos 3 byte (3 octeto) para endereço de REDE e 1 bytes (1 octetos)
     para HOST e possiveis endereços de SUBNET sendo então (2↑8)-2 (-2 são os endereços de REDE e de BROADCAST
     que devem ser descontados), em seu primeiro Byte o primeiro e o segundo bit será sempre 1 e o terceiro bit
     sempre será 0. Sendo assim o intervalo de endereçamentos no primeiro byte de um endereçamento classe B será
     de 192 - 223.
     
     |  REDE  |  REDE  |  REDE  |  HOST  |    -   Endereço classe C.    

> Na operação é será comparado o endereço IP com a mascará de Rede:

     Exemplo:
     00001010.00001010.00001010.00001010       -     Endereço IP
     11111111.11111111.11111111.00000000       -     Mascará de Rede
    |__________REDE_____________|__HOST__|
     00001010.00001010.00001010.00000000       -     Endereço de Rede
                               _00000001
                                         }  ----    Intervalo de endereços válidos
                               _11111110
     00001010.00001010.00001010.11111111       -     Endereço de brodcast

> Quando a mascará e o endereço IP possuírem 1 será atribuído 1 ao endereço de rede quando alguns deles estiverem em 0 será atribuído 0.
     

### Aumentar o numero de redes
 
    calculo:
    2 ↑ X - 2 >= N
    X - numero de Bits
    N - numero de maquinas necessárias
    
    exemplo:
    2 ↑ X - 2 >= 1000
    2 ↑ X >= 1002
    2 ↑ 10 >= 1002
    1024 >= 1002
