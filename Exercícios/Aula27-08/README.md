# Exercícios de Manipulação de Arquivos em Python

Esta atividade avaliativa contém uma série de questões que envolvem a manipulação de arquivos em Python. Cada função resolve um problema específico, como ler, escrever e processar arquivos de texto de maneiras diferentes. 

## Requisitos

Antes de rodar o código, é necessário instalar a biblioteca `lorem`, que é utilizada para gerar texto aleatório. Para instalar essa biblioteca, execute o comando abaixo:

```bash
pip install lorem
```

## Descrição das Questões

### Questão 1 - Leitura de Arquivo e Criação do Arquivo

Esta questão tenta abrir um arquivo chamado notas.txt. Se o arquivo não for encontrado, ele será criado com o conteúdo "Arquivo criado". O conteúdo do arquivo é então impresso no terminal.

### Questão 2 - Contagem de Linhas Não Vazias

O código tenta abrir o arquivo frases.txt, escreve um texto gerado aleatoriamente com a biblioteca lorem, e depois conta quantas linhas não estão vazias no arquivo. Ele também trata erros de permissão ao tentar escrever o arquivo.

### Questão 3 - Limpeza de Comentários

Neste exercício, o código lê um arquivo comentarios.txt com exemplos de textos contendo espaços duplos e reticências. Ele remove os espaços extras, substitui as reticências por um único ponto e salva o resultado no arquivo comentarios_limpos.txt. Além disso, o código lida com erros de codificação ao tentar abrir o arquivo.

### Questão 4 - Processamento de Jogadores e Times

A questão trabalha com a leitura de um arquivo jogadores.txt contendo nomes de jogadores e seus respectivos times. O código divide cada linha em um dicionário de jogadores e times. Caso haja uma linha inválida (sem vírgula), ela é registrada em um arquivo de log chamado linhas_invalidas.log.

### Questão 5 - Unificação e Ordenação de Listas

O código lê os arquivos lista_a.txt e lista_b.txt, junta os itens de ambas as listas, remove duplicatas e salva os itens únicos e ordenados no arquivo lista_uniq.txt. Caso algum dos arquivos não seja encontrado, o código avisa no terminal e processa apenas o arquivo que existe.

### Questão 6 - Contagem de Palavras Distintas

A função lê o arquivo texto.txt, transforma todas as palavras em minúsculas, remove a pontuação básica e conta a quantidade de palavras distintas no arquivo. Caso o arquivo não seja encontrado, uma mensagem de erro é exibida.

### Questão 7 - Unificação e Ordenação de Duas Listas de Frutas

De maneira semelhante à questão 5, o código lê dois arquivos (lista_a.txt e lista_b.txt) contendo listas de frutas. Ele junta as duas listas, remove duplicatas e ordena os itens, salvando o resultado em um arquivo lista_uniq.txt. O código lida com a falta de um dos arquivos, processando apenas o que existir.

## Como Executar o Código

Clone este repositório ou baixe os arquivos.

Instale a biblioteca lorem:

```
pip install lorem
```

Execute o código:

```
python nome_do_arquivo.py
```


## Dinâmica de Execução das Questões

O código foi estruturado para permitir uma execução dinâmica das questões com base em uma interação simples com o usuário através de um menu. Essa abordagem facilita a execução de várias funções sem que o código precise ser reescrito ou modificado cada vez que uma nova questão for adicionada.

### Como Funciona:

 **Dicionário de Questões:**
   O código utiliza um dicionário chamado `questoes` que armazena todas as funções correspondentes às questões. A chave do dicionário é um identificador (número da questão, como "1", "2", etc.) e o valor é uma tupla contendo:
   - Uma descrição breve da questão (por exemplo, "Questão 1").
   - A função que implementa a lógica daquela questão.

   Exemplo de estrutura:

   ```
   questoes = {
       "1": ("Questão 1", questao_1),
       "2": ("Questão 2", questao_2),
       "3": ("Questão 3", questao_3),
       # outras questões aqui...
   }
  ```

**Menu de Opções:**
O código exibe um menu com as opções disponíveis para o usuário. Ele mostra o número da questão e sua descrição, baseada nas chaves e valores do dicionário questoes. O usuário pode então digitar o número da questão que deseja executar.

O menu é gerado dinamicamente com base nas entradas do dicionário questoes. Isso significa que, se você adicionar ou remover questões, o menu será automaticamente ajustado para refletir essas alterações, sem a necessidade de mexer na lógica de exibição do menu.

Exemplo do menu gerado:
```
[1] Questão 1
[2] Questão 2
[3] Questão 3
[0] Sair
```
