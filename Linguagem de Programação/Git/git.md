### Configuração Global github
> 

**Identidade de identificação**

> Definição de um usuario de identificação para o git.

      $ git config --global user.name {"Nome de usuário"}
      $ git config --global user.email {email pessoal}
      
      Exemplo:
      $ git config --global user.name "ThreeDP"
      $ git config --global user.email davypaulinocbjr@outlook.com
      
      
**Editor de texto ou IDE**

> Definição de um editor de texto padrão para o git.
      
      $ git config --global core.editor {nome editor}
      
      Exemplos:
      $ git config --global core.editor emacs
      $ git config --global core.editor atom
      
**Definição de ferramenta Diff*

      $ git config --global merge.tool {nome ferramenta diff}
      
      Exemplo:
      $ git config --global merge.tool vimdiff

**Verificar configurações**

      Basta usar o comando abaixo para listar as configurações:
      $ git config --list
      
      Para sair da lista de configurações basta aperta:
      q
      
Também é possivel buscar por uma key especifica:

      $ git config {key}
      
      Exemplos:
      $ git config user.name
      $ git config core.editor

### Obetendo Ajuda
> Para obter o manpage(manual de comandos) de um tipo expecifico de ação basta usar um dos comandos:

      $ git help <verb>
      $ git <verb> --help
      $ man git-<verb>
      
      Exemplo:
      $ git help config
      $ git action --help
      
Outras formas de obter ajuda é por:
      
      #git ou #github no servidor Freenode(irc.freenode.net)
      
