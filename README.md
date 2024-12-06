# data-analysis
 English: This folder presents data analyses I performed, along with comments. It includes the scripts, tables used, comments, and analysis of the results.  
 Portuguese: Esta pasta apresenta análises de dados realizadas por mim, com comentários. Contém os scripts, tabelas utilizadas, comentários e análise dos resultados obtidos
 
## Utilização dos Scripts de Análise no Spyder (Anaconda)
### Introdução
Este repositório contém dois scripts Python que realizam análises estatísticas sobre um conjunto de dados de corrupção e outro sobre o estudo da relação entre a idade e o comprimento de bebês. Os scripts utilizam bibliotecas populares como pandas, numpy, matplotlib, seaborn, statsmodels e scipy. O objetivo dos scripts é realizar tarefas como carga de dados, análise exploratória, modelagem de regressão e visualização de resultados.

Este README tem como objetivo guiar você na execução e utilização dos scripts no ambiente Spyder do Anaconda.

### Pré-requisitos
Antes de executar os scripts, é necessário garantir que o ambiente tenha todas as bibliotecas necessárias instaladas.

#### 1. Instalar o Anaconda
Caso você ainda não tenha o Anaconda instalado, baixe a versão adequada para o seu sistema operacional no site oficial do Anaconda.

#### 2. Criar um Ambiente Conda (Opcional)
Se desejar, você pode criar um ambiente isolado para o seu projeto. Para isso, execute o seguinte comando no terminal do Anaconda Prompt:

bash
Copiar código
conda create -n analise_corrupcao python=3.8
conda activate analise_corrupcao
#### 3. Instalar as Bibliotecas Necessárias
Após ativar o ambiente, instale as bibliotecas necessárias com o comando abaixo:

bash
Copiar código
conda install pandas numpy matplotlib seaborn statsmodels scikit-learn scipy plotly
pip install playsound pingouin emojis statstests
### Como Executar os Scripts no Spyder
Abrir o Spyder:

Abra o Spyder através do Anaconda Navigator ou pelo terminal do Anaconda Prompt digitando spyder.
Carregar os Scripts:

Abra o Spyder e carregue os scripts através do menu File -> Open ou usando o atalho Ctrl + O.
Executar os Scripts:

No Spyder, você pode executar os scripts linha por linha utilizando o botão Run ou utilizando o atalho F5 para executar o script inteiro.
Verificar as Saídas:

As saídas serão exibidas na Console do Spyder. Para visualizações gráficas, os gráficos serão exibidos em uma janela separada ou diretamente na janela de gráficos do Spyder, dependendo das configurações.

## Estrutura dos Diretórios
plaintext
Copiar código
└── seu_projeto/

    ├── bebes.csv             # Arquivo de dados de bebês
    
    ├── corrupcao.csv         # Arquivo de dados sobre corrupção
    
    ├── analise_corrupcao.py  # Script 1: Análise de Corrupção
    
    ├── analise_bebes.py      # Script 2: Análise de Bebês
    
    ├── EXEMPLO3.html         # Gráfico interativo gerado pelo Script 1
    
    └── README.md             # Este arquivo
    
## Considerações Finais
Formato de Entrada: Certifique-se de que os arquivos CSV estejam corretamente formatados e no mesmo diretório ou ajuste os caminhos no código.
Saídas: Os gráficos serão exibidos em janelas de visualização ou na interface do Spyder, e os resumos dos modelos serão mostrados na Console.
Gráficos Interativos: O script de análise de corrupção gera gráficos interativos utilizando Plotly, que são salvos em formato HTML e podem ser visualizados diretamente no navegador.
Contribuições
Este repositório está aberto para melhorias. Caso tenha sugestões ou correções, sinta-se à vontade para enviar um pull request.
