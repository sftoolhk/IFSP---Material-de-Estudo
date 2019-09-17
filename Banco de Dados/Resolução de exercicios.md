# Capitulo 01

**Questões:**

1. Discuta cada um dos seguintes termos:

*Resposta a. dados:*
    
> Dados são um conjunto bruto de fatos que poderam ou não se tornar informações dependendo de seu contexto ou aplicação e de como é o trabalho sobre esses dados. Por exemplo um dado pode gerar uma informação muito importante e valiosa pra uma determinada empresa e para outra empresa pode permanecer em forma de dado ou seja sem relevancia para a empresa aplicação. Exemplos podem ser datas de aniversário, nome de fornecedor ou lucro mensal.
    
*Resposta b. campo:*
    
> Um campo recebera um rótulo e normalmente ira armazenar somente um tipo de dado, ou seja ele seria como uma coluna em uma aplicação comum. Um campo poderia ser Nome ou idade por exemplo.
    
*Resposta c. registro:*

> Registro, tupla ou linha será onde os dados de um unico item de dado será armazenado em um agrupamento lógico de dados. Por exemplo as informações de um individuo como nome, idade, sexo e altura.
    
*Resposta d. arquivo:*

> Conjunto de dados e registros que compoem uma informação ou não. Um exemplo seria as matriculas de alunos em uma escola.
    
____________________________________________________________________________________________________________________________

2. O que é redundância de dados e quais características do sistema de arquivos podem levar a ela?
    
*Resposta 2.*
    
> Quando diferentes versôes de um mesmo dado aparecem em locais diferentes. Por exemplo, quando o departamento de vendas de uma empresa armazena o nome de uma representante de vendas como "Cris Silva" e o departamento de recursos humanos armazena o nome da mesma pessoa como "Cris G. da Silva" nesse caso o perfil de um mesmo colaborador estaria duplicado em nosso banco de dados.
____________________________________________________________________________________________________________________________

4. O que é um SGBD e quais são suas funções?
    
*Resposta 4.*
    
> SGBD ( Sistema de gerenciamento de bancos de dados é um conjunto de programas que gerenciam a estrutura do banco de dados e controlam o acesso aos dados armazenados.
____________________________________________________________________________________________________________________________

7. Qual é o papel de um SGBD e quais são suas vantagens? E as suas desvantagens?

*Resposta 7.*

> O SGBD serve como intermediário entre o usuário e o banco de dados. o SGBD recebe todas as solicitações de aplicações e as traduz nas operações complexas necessárias para atendê-las. Suas vantagens são aprimoramento do compartilhamento de dados, aprimoramento da segurança de dados, melhoria na integração dos dados, minimizaçãoda inconsistência dos dados, aprimoramento do acesso aos dados, aprimoramento da tomada de decisão, aumento de produtividade do usuário final entre outras muitas. Em suas desvantagens estão no custo alto para implementação de um sistema SGBD alem do alto tempo demandado, que só aumenta conforme o tamanho da empresa, e Risco com a seguranção já que por mais que o sistema administre os varios usuários em casos necessários ainda abre muitas portas de risco para que usuarios não autorizados acessem informações que não eram de sua grade.
____________________________________________________________________________________________________________________________

10. O que São metadados?

*Resposta 10.*

> Um metadado traz uma visão mais completa dos dados de um banco de dados. Ele fornece uma descrição das caracteristics dos dados e do conjunto de relacionamento que liga os dados encontrados no banco de dados. Um exemplo seria um valor de 1000 em um dado em nosso banco seu metadado pode ser metros, R$, unidades, Kg, etc...
____________________________________________________________________________________________________________________________

11. Explique por que o projeto do banco de dados é importante.

*Resposta 11.*

>  Porquê determina a estrutura do banco, facilita o gerenciamento dos dados e gera informações precisas e valiosas. Caso seja mal projetado pode levar ao fracasso de uma organização.

# Capitulo 02
    
**Questões:**

1. Discuta a importância da modelagem de dados.
    
2. O que é uma regra de negócio e qual é sua finalidade na modelagem de dados?
    
3. Como é possivel traduzir regras de negócio em componentes de modelos de dados?
    
14. O que é um relacionamento e quais são seus três tipos?
    
**Problemas:**
    
24. Apresente as regras de negócio que representam o DER apresentado na Figura P2.6. (Observe que o DER reflete alguns pressupostos de simplificação. Por exemplo, cada livro é escrito por apenas um autor. Além disso, lebre-se de que o DER é sempre lido do lado "1" para o lado "M", independente da orientação de seus componentes.)
    
    
![Figura P2.6: DER pé de galinha
para o Problema 24](https://github.com/ThreeDP/IFSP---Material-de-Estudo/blob/master/Banco%20de%20Dados/Untitled%20Diagram.png)
    
25. Crie um DER pé de galinha para cada uma das seguintes descrições. (Observação: A palavra vários significa simplesmente "mais de um" no ambiente de modelagem de bancos de dados.)
    
a. Cada divisão da meaCo Corporation é composta de vários departamentos. Cada departamento possui vários funcionários atribuídos a ele, mas cada funcionário trabalha em apenas um departamento. Cada departamento é gerenciado por um funcionário trabalha em apenas um departamento. Cada departamento é gerenciado por um funcionário e cada um desses gerentes pode gerenciar apenas um departamento ao mesmo tempo.
    
b. Durante determinado período de tempo, um cliente pode alugar várias fitas de vídeo da locadora BigVid. Cada fita de vídeo da BigVid pode ser alugada a vários clientes nesse período.
    
c. Um avião de linhas aéreas pode ser encarregado de vários voos, mas cada voo é feito por apenas um avião.
    
d. A KwikTite Corporation opera várias fábricas. Cada fábrica localiza-se em uma única região. Cada região pode "abrigar" várias fábricas da KwikTite. Cada fábrica emprega muitos funcionários , mas cada um desses funcionários é empregado de apenas um fábrica.
    
e. Um funcionário pode obter vários graus de ensino e cada grau de ensino pode ser obtido por vários funcionários.
    
# Capitulo 03
    
**Questões:**

1. Qual é a iferença entre banco de dados e uma tabela?
    
2. O que significa dizer que um banco de dados apresenta integridade de entidades e integridade referencial?
    
9. O que são os homônimos e sinônimos e por que devem ser evitados no projeto de bancos de dados?

**problemas:**
    
8. Para cada tabela, identigique a chave primária e a(s) chave(s) estrangeira(s). Se uma tabela não tiver uma chave estrangeira, escreva Nenhum no espaço fornecido.
    
![Tabela exercicio 8: ](https://github.com/ThreeDP/IFSP---Material-de-Estudo/blob/master/Banco%20de%20Dados/TABELA%20CAP03%20EX08.png)

16. Crie o diagrama relacional para mostrar o relacionameto entre funcionários, loja e região.
    
    Utilize o banco de dados apresentado na Figura P3.3 para desenvolver os Problemas 17-22.
        
![P3.3 Tabela de banco de dados: ](https://github.com/ThreeDP/IFSP---Material-de-Estudo/blob/master/Banco%20de%20Dados/P3.3.jpg)        
    
    
