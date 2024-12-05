
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
======================================================
Análise de Regressão Múltipla: Estudo sobre Corrupção
======================================================

Analise utilizando o Spyder. Recomendado utilizar durante a execução

Objetivo:
Este script tem como objetivo realizar uma análise de regressão múltipla para 
estudar a relação entre o Índice de Percepção de Corrupção (CPI) e diferentes 
variáveis explicativas, utilizando abordagens que incluem **ponderação 
arbitrária** e **ajuste não linear**. A análise começa com um modelo de 
regressão simples utilizando uma variável numérica para representar as regiões, 
mas esse modelo incorre em um erro de ponderação. O script corrige esse erro ao 
introduzir variáveis dummies para representar as diferentes regiões geográficas, 
permitindo um modelo de regressão múltipla mais robusto e apropriado. 

Metodologia:
1. **Modelo de Regressão Simples com Ponderação Arbitrária**:
   No primeiro modelo, a variável 'regiao' foi transformada em uma variável 
   numérica (`regiao_numerico`) para representar as diferentes regiões 
   geográficas (América do Sul = 1, Ásia = 2, EUA e Canadá = 3, Europa = 4, 
                Oceania = 5). Essa abordagem de **ponderação arbitrária** é 
   problemática, pois assume que a diferença entre as regiões é de natureza 
   quantitativa, o que não é o caso. Ao tratar regiões distintas como variáveis 
   numéricas, esse modelo gera uma análise imprecisa, como evidenciado pelos 
   resultados da regressão simples, onde a variável `regiao_numerico` apresentou 
   um coeficiente significativo, mas sem considerar corretamente as diferenças 
   regionais de forma qualitativa.

   - **Resultado do Modelo com Ponderação Arbitrária**: A regressão simples 
   apresentou um **R² de 0.411**, indicando que o modelo conseguiu explicar 
   apenas uma parte moderada da variação no CPI. Contudo, o erro reside no fato 
   de tratar as regiões como numéricas, o que pode distorcer a interpretação dos 
   resultados.

2. **Modelo de Regressão Múltipla com Variáveis Dummies**:
   O segundo modelo melhora significativamente a análise utilizando **variáveis 
   dummies**, que são variáveis binárias criadas para representar as regiões de 
   forma adequada. Cada variável dummy captura a presença ou ausência de uma 
   região específica, sem implicar uma relação numérica entre elas. Essa 
   abordagem permite que o modelo entenda a variação do CPI entre diferentes 
   regiões de forma mais precisa e sem as limitações da ponderação arbitrária.

   - **Resultado do Modelo com Dummies**: O modelo de regressão múltipla com 
   dummies apresentou um **R² de 0.603**, indicando que ele explica uma parte 
   maior da variação no CPI em comparação ao modelo simples. A inclusão de 
   variáveis dummies resultou em coeficientes significativos para as regiões, 
   permitindo uma análise mais detalhada e justa das diferenças regionais.

3. **Ajuste Não Linear**:
   Para complementar a análise, foi realizado um **ajuste não linear** sobre os 
   valores ajustados (fitted values) do modelo com dummies, utilizando uma 
   interpolação cúbica (splines). Esse ajuste permite representar de forma mais 
   precisa a relação entre as variáveis explicativas (região) e o CPI, evitando 
   os erros de modelagem que poderiam surgir com a abordagem linear simples. 

   - **Resultado do Ajuste Não Linear**: O gráfico gerado mostra uma curva 
   suavizada que ajusta os valores do CPI para diferentes regiões, evidenciando 
   uma relação mais flexível e realista do que a simples regressão linear, e 
   confirmando a vantagem do modelo com variáveis dummies e o ajuste não linear.

Objetivo Final:
Através desta análise de **regressão múltipla com variáveis dummies e ajuste 
não linear**, espera-se demonstrar que a simples transformação das regiões em 
variáveis numéricas (ponderação arbitrária) leva a resultados distorcidos e 
imprecisos. Ao utilizar variáveis dummies e ajustar os valores do modelo de 
forma não linear, é possível obter uma explicação mais robusta e precisa da 
relação entre o CPI e as regiões geográficas. Esta análise fornece uma visão 
detalhada e confiável sobre como as percepções de corrupção variam entre as 
diferentes partes do mundo.

Autor: Pedro Medeiros
Data: 04 de dezembro
======================================================
"""
# In[0.1]:
"""
Instalação das bibliotecas necessárias
"""
!pip install pandas
!pip install numpy
!pip install -U seaborn
!pip install matplotlib
!pip install plotly
!pip install scipy
!pip install statsmodels
!pip install scikit-learn
!pip install playsound
!pip install pingouin
!pip install emojis
!pip install statstests

# In[1.1]:
"""
Importação de bibliotecas e módulos
"""

# Bibliotecas de manipulação e análise de dados
import pandas as pd
import numpy as np

# Bibliotecas para análise estatística
import statsmodels.api as sm
from sklearn.preprocessing import LabelEncoder

# Bibliotecas para visualização de dados
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from scipy import interpolate

# Outras bibliotecas úteis para visualização de dados
import webbrowser

# In[2.1]:
"""
Leitura e inspeção do dataset de corrupção
"""
# Carregando o dataset
df_corrupcao = pd.read_csv('corrupcao.csv', delimiter=',', encoding='utf-8')

# Exibindo as primeiras linhas do dataframe
df_corrupcao.head()

# Exibindo as informações gerais sobre o dataset (tipos de dados e valores nulos)
df_corrupcao.info()

# Exibindo as estatísticas descritivas do dataset
df_corrupcao.describe()

# Exibindo estatísticas descritivas por região
df_corrupcao.groupby('regiao').describe()

# In[3.1]:
"""
Tabela de frequências da variável 'regiao'
"""
# Gerando a contagem de frequências e a distribuição percentual da variável 'regiao'
contagem = df_corrupcao['regiao'].value_counts(dropna=False)
percent = df_corrupcao['regiao'].value_counts(dropna=False, normalize=True)

# Exibindo as contagens e percentuais
pd.concat([contagem, percent], axis=1, keys=['contagem', '%'], sort=False)

# In[3.2]:
"""
Conversão da variável 'regiao' para dados numéricos
Este processo é utilizado para ilustrar a problemática de ponderação arbitrária.
"""
label_encoder = LabelEncoder()

# Convertendo a variável categórica 'regiao' para numérica
df_corrupcao['regiao_numerico'] = label_encoder.fit_transform(df_corrupcao['regiao'])
df_corrupcao['regiao_numerico'] = df_corrupcao['regiao_numerico'] + 1

# Exibindo as primeiras linhas após a conversão
df_corrupcao.head(10)

# In[3.3]:
"""
Modelando com a variável 'regiao_numerico' de forma incorreta, com ponderação 
arbitrária
"""
# Estimando o modelo de regressão (uso incorreto da variável 'regiao_numerico')
modelo_corrupcao_errado = sm.OLS.from_formula("cpi ~ regiao_numerico", df_corrupcao).fit()

# Exibindo o resumo do modelo estimado
modelo_corrupcao_errado.summary()

# In[3.4]:
"""
Visualização dos valores ajustados do modelo incorreto
"""
# Criando o gráfico com o ajuste incorreto
plt.figure(figsize=(15,10))
ax = sns.regplot(
    data=df_corrupcao,
    x="regiao_numerico", y="cpi",
    scatter_kws={"s": 200, "color": "darkorange", "alpha": 0.5},
    line_kws={"color": "indigo"}
)

# Função para adicionar anotações ao gráfico
def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        offset = 0
        while ax.texts:
            overlapping = False
            for text in ax.texts:
                overlapping |= text.get_position()[0] == (point['x'] + 0.05) and text.get_position()[1] == (point['y'] - 0.05 + offset)
            if overlapping:
                offset += 0.15
            else:
                break
        ax.annotate(str(point['val']) + " " + str(point['y']),
                    (point['x'] + 0.05, point['y'] - 0.05 + offset),
                    fontsize=11)

# Adicionando título e rótulos ao gráfico
plt.title('Resultado da Ponderação Arbitrária', fontsize=20)
plt.xlabel('Região', fontsize=17)
plt.ylabel('Corruption Perception Index', fontsize=17)
plt.xticks(range(1, 6, 1), fontsize=14)
plt.yticks(range(0, 11, 1), fontsize=14)

# Adicionando as anotações dos países e CPI
label_point(x=df_corrupcao['regiao_numerico'], y=df_corrupcao['cpi'], val=df_corrupcao['pais'], ax=plt.gca())

# Exibindo o gráfico
plt.show()

# In[3.5]:
"""
Dummizando a variável 'regiao'
Este processo transforma a variável 'regiao' em variáveis binárias (dummies), 
removendo a categoria de referência.
"""
# Realizando a dummização da variável 'regiao'
df_corrupcao_dummies = pd.get_dummies(df_corrupcao, columns=['regiao'], dtype=int, drop_first=True)

# Exibindo o dataframe com as variáveis dummies
df_corrupcao_dummies.head()

# In[3.6]:
"""
Estimando o modelo de regressão múltipla com variáveis dummies
"""
# Estimando o modelo de regressão múltipla utilizando as dummies
modelo_corrupcao_dummies = sm.OLS.from_formula("cpi ~ regiao_Asia + regiao_EUA_e_Canada + regiao_Europa + regiao_Oceania", df_corrupcao_dummies).fit()

# Exibindo o resumo do modelo estimado com variáveis dummies
modelo_corrupcao_dummies.summary()

# In[3.7]:
"""
Outro método de estimação usando as variáveis dummies
"""
# Gerando a fórmula do modelo a partir das colunas dummies
lista_colunas = list(df_corrupcao_dummies.drop(columns=['cpi', 'pais', 'regiao_numerico']).columns)
formula_dummies_modelo = ' + '.join(lista_colunas)
formula_dummies_modelo = "cpi ~ " + formula_dummies_modelo

# Exibindo a fórmula do modelo
print("Fórmula utilizada:", formula_dummies_modelo)

# Estimando o modelo com as dummies
modelo_corrupcao_dummies = sm.OLS.from_formula(formula_dummies_modelo, df_corrupcao_dummies).fit()

# Exibindo o resumo do modelo estimado
modelo_corrupcao_dummies.summary()

# In[3.8]:
"""
Visualização do modelo ajustado com variáveis dummies
"""
# Adicionando os valores ajustados (fitted) ao dataframe
df_corrupcao_dummies['fitted'] = modelo_corrupcao_dummies.fittedvalues

# In[3.9]:
"""
Gráfico do ajuste do modelo com variáveis dummies
"""
# Preparando os dados para o gráfico
df2 = df_corrupcao_dummies[['regiao_numerico', 'fitted']].groupby(['regiao_numerico']).median().reset_index()
x = df2['regiao_numerico']
y = df2['fitted']

# Realizando a interpolação
tck = interpolate.splrep(x, y, k=2)
xnew = np.arange(1, 5, 0.1)
ynew = interpolate.splev(xnew, tck, der=0)

# Criando o gráfico
plt.figure(figsize=(15, 10))
plt.scatter(df_corrupcao_dummies['regiao_numerico'], df_corrupcao_dummies['cpi'], color='darkorange', s=200, alpha=0.5)
plt.scatter(df_corrupcao_dummies['regiao_numerico'], df_corrupcao_dummies['fitted'], color='limegreen', s=240)
plt.plot(xnew, ynew, color='indigo', linewidth=2.5)

# Título e rótulos
plt.title('Ajuste Não Linear do Modelo com Variáveis Dummy', fontsize=20)
plt.xlabel('Região', fontsize=17)
plt.ylabel('Corruption Perception Index', fontsize=17)
plt.xticks(range(1, 6, 1), fontsize=14)
plt.yticks(range(0, 11, 1), fontsize=14)

# Exibindo as anotações
label_point(x=df_corrupcao_dummies['regiao_numerico'], y=df_corrupcao_dummies['cpi'], val=df_corrupcao_dummies['pais'], ax=plt.gca())

# Exibindo o gráfico
plt.show()

# In[3.10]:
"""
Gerando o gráfico interativo com Plotly e salvando-o em um arquivo HTML
"""
# Criando o gráfico interativo com Plotly
fig = go.Figure()

# Adicionando os pontos reais (CPI)
fig.add_trace(go.Scatter(
    x=df_corrupcao_dummies['regiao_numerico'],
    y=df_corrupcao_dummies['cpi'],
    mode='markers',
    name='CPI',
    marker=dict(color='darkorange', size=14, opacity=0.5)
))

# Adicionando os pontos ajustados (fitted)
fig.add_trace(go.Scatter(
    x=df_corrupcao_dummies['regiao_numerico'],
    y=df_corrupcao_dummies['fitted'],
    mode='markers',
    name='Fitted',
    marker=dict(color='limegreen', size=17)
))

# Adicionando a linha de interpolação
fig.add_trace(go.Scatter(
    x=xnew,
    y=ynew,
    mode='lines',
    name='Interpolated',
    line=dict(color='indigo', width=3.5)
))

# Personalizando o layout do gráfico
fig.update_layout(
    title={
        'text': 'Ajuste Não Linear do Modelo com Variáveis Dummy',
        'font': {'size': 20, 'color': 'black', 'family': 'Arial'},
        'x': 0.5,
        'y': 0.95,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis=dict(title='Região'),
    yaxis=dict(title='Corruption Perception Index'),
    xaxis_tickvals=list(range(1, 6)),
    yaxis_tickvals=list(range(0, 11)),
    xaxis_tickfont=dict(size=14),
    yaxis_tickfont=dict(size=14),
    template='plotly_white'
)

# Adicionando anotações com o nome do país e o valor do CPI
for i in range(len(df_corrupcao_dummies)):
    fig.add_annotation(
        x=df_corrupcao_dummies['regiao_numerico'][i],
        y=df_corrupcao_dummies['cpi'][i],
        text=str(df_corrupcao_dummies['pais'][i]) + ' ' + str(df_corrupcao_dummies['cpi'][i]),
        showarrow=False,
        font=dict(size=11, color='black'),
        xshift=50,
        yshift=0,
        textangle=0
    )

# Atualizando a aparência das anotações
fig.update_annotations(dict(xref="x", yref="y"))
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')

# Salvando o gráfico em formato HTML
fig.write_html('EXEMPLO3.html')

# Abrindo o gráfico HTML no navegador
webbrowser.open('EXEMPLO3.html')

# In[3.11]:
"""
Este código finaliza a análise e visualização do modelo de regressão com variáveis 
dummies. O gráfico interativo gerado foi salvo em formato HTML e aberto no navegador.
O objetivo foi visualizar de maneira clara o ajuste do modelo, mostrando a
relação entre as regiões e o índice de percepção de corrupção (CPI).
"""

# Imprimindo os resultados dos modelos
print("\n--- Resultados do Modelo de Regressão Simples (Erro com Ponderação Arbitrária) ---")
print(modelo_corrupcao_errado.summary())

print("\n--- Resultados do Modelo de Regressão com Variáveis Dummies ---")
print(modelo_corrupcao_dummies.summary())

# Imprimindo os valores ajustados (fitted values) para verificação da qualidade do modelo
print("\n--- Valores Ajustados (Fitted Values) do Modelo com Dummies ---")
print(df_corrupcao_dummies[['regiao_numerico', 'cpi', 'fitted']].head())

# In[4.10]: Análise dos Resultados

"""
--- Resultados do Modelo de Regressão Simples (Erro com Ponderação Arbitrária) ---
O modelo de regressão simples foi realizado utilizando a variável 'regiao_numerico', que representa
as diferentes regiões do mundo com valores numéricos atribuídos arbitrariamente. O modelo apresentou 
um **R-squared de 0.411**, indicando que apenas **41.1%** da variação do Índice de Percepção de Corrupção 
(CPI) é explicada pela variável 'regiao_numerico'. Esse valor é relativamente baixo, sugerindo que o modelo 
não é capaz de explicar completamente as variações observadas nos dados. Além disso, a ponderação arbitrária 
das regiões pode ter introduzido viés no modelo, já que a relação entre as regiões e o CPI não pode ser 
representada por uma escala numérica linear.

Resultados importantes:
- O coeficiente de 'regiao_numerico' foi **1.4483**, indicando que, a cada aumento unitário na variável 
'regiao_numerico', o CPI aumenta em **1.4483 unidades**.
- O valor de p associado ao coeficiente da variável 'regiao_numerico' foi **0.000**, indicando que este 
coeficiente é estatisticamente significativo.

Conclusão:
A análise mostra que o modelo de regressão simples com 'regiao_numerico' não é adequado para descrever a 
relação entre as regiões e o CPI. Isso se deve ao fato de que tratamos uma variável qualitativa como numérica, 
o que pode gerar interpretações distorcidas e conclusões erradas.

---

--- Resultados do Modelo de Regressão com Variáveis Dummies ---
O modelo com variáveis dummies foi estimado para considerar as diferentes regiões de forma independente, 
tratando cada uma delas como uma variável binária. Com a América do Sul como categoria de referência, 
os coeficientes das variáveis dummies indicaram diferenças significativas na percepção de corrupção entre 
as regiões. O modelo com dummies apresentou **R-squared de 0.603**, o que significa que agora o modelo explica 
**60.3%** da variação no CPI, uma melhoria significativa em relação ao modelo anterior. Isso sugere que 
o modelo com dummies é mais adequado para descrever a relação entre as regiões e o CPI.

Resultados importantes:
- O coeficiente de 'regiao_Asia' foi **-1.8506**, indicando que a percepção de corrupção na Ásia é 
média **1.85 unidades** inferior à da América do Sul, com p = **0.045** (significativo).
- O coeficiente de 'regiao_EUA_e_Canada' foi **3.8200**, indicando que a percepção de corrupção nos 
EUA e Canadá é **3.82 unidades** superior à da América do Sul, com p = **0.013** (significativo).
- O coeficiente de 'regiao_Europa' foi **2.0783**, indicando que a percepção de corrupção na Europa é 
**2.08 unidades** superior à da América do Sul, com p = **0.021** (significativo).
- O coeficiente de 'regiao_Oceania' foi **4.8200**, indicando que a percepção de corrupção na Oceania 
é **4.82 unidades** superior à da América do Sul, com p = **0.002** (significativo).

Conclusão:
O modelo com variáveis dummies mostrou uma explicação consideravelmente melhorada da variação no CPI 
(60.3% de explicação). A dummização das variáveis regionais permite que cada região tenha um efeito 
específico e independente sobre o CPI, sem a imposição de uma relação linear arbitrária. Com base nos 
resultados, podemos concluir que a **Oceania** e os **EUA/Canadá** apresentam percepções significativamente 
menores de corrupção em comparação à América do Sul, enquanto **Ásia** e **Europa** têm percepções mais altas 
de corrupção.

---

--- Valores Ajustados (Fitted Values) do Modelo com Dummies ---

Os valores ajustados (fitted values) fornecem uma estimativa do CPI com base nos valores das variáveis 
explicativas no modelo. Para verificar a adequação do modelo, apresentamos os seguintes valores ajustados 
para algumas observações:

   regiao_numerico  cpi    fitted
0                1  3.9  4.180000
1                5  8.7  9.000000
2                4  7.9  6.258333
3                4  7.1  6.258333
4                1  4.0  4.180000

Os valores ajustados são consistentes com as expectativas. Por exemplo:
- Para a **região 1 (América do Sul)**, o valor ajustado do CPI é **4.18**, que é exatamente o valor do 
intercepto, como esperado.
- Para a **região 5 (Oceania)**, o valor ajustado do CPI é **9.00**, refletindo a maior percepção de 
corrupção nesta região.

Conclusão Final:
O modelo de regressão múltipla com variáveis dummies foi substancialmente mais eficaz do que o modelo simples. 
Com um **R-squared de 0.603**, o modelo mostrou-se capaz de explicar a maior parte da variação no CPI, 
considerando as diferenças regionais. As percepções de corrupção variam de maneira significativa entre as 
regiões, com as regiões como Oceania e EUA/Canadá apresentando menores percepções de corrupção e a 
Ásia e Europa mostrando percepções mais elevadas. Para melhorar ainda mais a explicação do modelo, seria 
interessante analisar os resíduos e explorar possíveis transformações adicionais de variáveis ou a inclusão 
de novas variáveis explicativas.
"""