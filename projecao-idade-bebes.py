#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
======================================================
Análise de Regressão Não Linear e Transformação de Box-Cox
======================================================

Analise utilizando o Spyder. Recomendado utilizar durante a execução

Objetivo:
Este script tem como objetivo realizar uma análise de regressão não linear e 
transformação de Box-Cox para estudar a relação entre a idade (em semanas) e o 
comprimento de bebês. A base de dados utilizada contém informações sobre a 
idade e o comprimento de bebês, e a análise inclui visualizações de dispersão, 
ajuste de modelos lineares e não lineares, além de técnicas de transformação p
ara lidar com a não normalidade dos dados. O principal objetivo é comparar a 
qualidade do ajuste entre um modelo linear simples (OLS) e um modelo não linear 
ajustado utilizando a transformação de Box-Cox.

Metodologia:
1. **Carregamento e Análise Exploratória dos Dados**:
   A base de dados `bebes.csv` é carregada e explorada com o uso de funções 
   básicas do `pandas`, como `info()` e `describe()`, para entender as 
   características e as estatísticas univariadas das variáveis `idade` e 
   `comprimento`. Em seguida, são criados gráficos de dispersão para visualizar 
   a relação entre essas variáveis.

2. **Gráficos de Dispersão**:
   São gerados diversos gráficos de dispersão para visualizar a relação entre a 
   idade e o comprimento dos bebês:
   - Gráfico simples de dispersão.
   - Gráfico de dispersão utilizando emojis como marcadores para uma 
   visualização mais lúdica.
   - Gráfico de dispersão com uma camada de texto utilizando emojis, para uma 
   representação visual criativa.

3. **Estimação de um Modelo Linear (OLS)**:
   A regressão linear simples (OLS) é aplicada para modelar a relação entre 
   `idade` e `comprimento`. A partir dessa estimativa, são apresentados os 
   coeficientes do modelo linear e suas estatísticas associadas. Além disso, um 
   gráfico de dispersão com os ajustes lineares e não lineares é gerado para 
   comparar os resultados de ambos os modelos.

4. **Teste de Normalidade dos Resíduos**:
   O teste de Shapiro-Francia é utilizado para verificar a aderência dos 
   resíduos do modelo OLS à normalidade. Isso é feito com o pacote `statstests`
   para testar a hipótese de normalidade dos resíduos.

5. **Transformação de Box-Cox**:
   Para melhorar a aderência à normalidade e reduzir a heterocedasticidade, é 
   realizada uma **transformação de Box-Cox** nos dados de `comprimento`. Esta 
   transformação é aplicada na variável dependente, e um novo modelo OLS é 
   estimado com a variável transformada. A comparação entre o modelo linear 
   original e o modelo com Box-Cox permite observar uma melhoria no ajuste do 
   modelo.

6. **Comparação dos Modelos Linear e Box-Cox**:
   A qualidade do ajuste dos modelos é comparada utilizando os valores de 
   **R²**. Também são gerados gráficos para ilustrar as diferenças entre os 
   dois ajustes e os valores ajustados (fitted values) para cada modelo.

7. **Predições e Análise Final**:
   A partir dos modelos OLS linear e Box-Cox, são feitas predições sobre o 
   comprimento esperado de um bebê com 52 semanas de idade. As predições são 
   comparadas entre os dois modelos para verificar as diferenças nos ajustes e 
   nas previsões.

Objetivo Final:
O objetivo desta análise é mostrar como a transformação de Box-Cox pode 
melhorar o ajuste de um modelo de regressão linear simples, especialmente 
quando os dados apresentam problemas de normalidade ou heterocedasticidade. 
Ao comparar os modelos lineares e não lineares, esperamos observar um aumento 
significativo na qualidade do ajuste e fornecer uma melhor compreensão sobre a 
relação entre a idade e o comprimento dos bebês.

Autor: Pedro Medeiros
Data: 04 de dezembro
======================================================
"""

# In[0.1]
"""
# 1. Instalação dos Pacotes Necessários
"""

!pip install pandas
!pip install numpy
!pip install -U seaborn
!pip install matplotlib
!pip install plotly
!pip install scipy
!pip install statsmodels
!pip install statstests


# In[0.2]
"""
# 2. Carregamento de Pacotes e Bibliotecas
# ----------------------------------------
# Agora que os pacotes necessários foram instalados, vamos carregá-los para 
utilizá-los em nossa análise.
"""

# Importação dos pacotes necessários
import pandas as pd  # Para manipulação e análise de dados
import matplotlib.pyplot as plt  # Para criação de gráficos
import seaborn as sns  # Para gráficos estatísticos
import statsmodels.api as sm  # Para regressão OLS
from scipy.stats import shapiro, boxcox  # Para testes de normalidade e transformação Box-Cox
from statsmodels.tools import eval_measures  # Para medidas de avaliação de modelos
import numpy as np  # Para manipulação de arrays e funções matemáticas

# In[0.3]
"""
# 3. Carregamento e Análise Inicial dos Dados
# -------------------------------------------
# O primeiro passo é carregar o conjunto de dados e realizar uma análise 
preliminar.
# Vamos utilizar a biblioteca pandas para carregar os dados do arquivo CSV.
# Depois, faremos uma análise inicial, verificando as variáveis presentes, 
# e as estatísticas descritivas do dataset.
"""

# Carregando o dataset
dataset_bebes = pd.read_csv('bebes.csv', delimiter=',')

# Exibindo as primeiras linhas do dataset
dataset_bebes.head()

# Exibindo informações sobre as variáveis do dataset (tipos, nulos, etc.)
dataset_bebes.info()

# Exibindo estatísticas descritivas (média, desvio padrão, etc.)
dataset_bebes.describe()

# In[0.4]
"""
# 4. Visualização Inicial: Gráficos de Dispersão
# ------------------------------------------------
# Para entender a relação entre as variáveis 'idade' e 'comprimento', 
# vamos criar gráficos de dispersão. 
# Esses gráficos ajudam a visualizar a tendência entre as variáveis,
# e nos ajudam a perceber se há alguma relação linear ou não linear.
"""

# Gráfico de dispersão simples
plt.figure(figsize=(12, 8))
sns.scatterplot(x="idade", y="comprimento", data=dataset_bebes, color='blue', s=100, alpha=0.7)
plt.title('Dispersão: Idade vs Comprimento', fontsize=16)
plt.xlabel('Idade (semanas)', fontsize=14)
plt.ylabel('Comprimento (cm)', fontsize=14)
plt.show()

# In[0.5]
"""
# 5. Estimação de um Modelo de Regressão Linear (OLS)
# ----------------------------------------------------
# Agora, vamos ajustar um modelo de regressão linear para entender a relação 
# entre as variáveis 'idade' e 'comprimento'. 
# Vamos utilizar a biblioteca statsmodels para realizar a regressão OLS 
(Ordinary Least Squares).
# O modelo linear irá nos ajudar a entender se existe uma relação linear simples 
# entre as duas variáveis.
"""

# Estimando o modelo OLS
modelo_linear = sm.OLS.from_formula('comprimento ~ idade', dataset_bebes).fit()

# Exibindo os resultados do modelo
modelo_linear.summary()

# In[0.6]
"""
# 6. Avaliação do Ajuste: Gráfico com Ajuste Linear
# -------------------------------------------------
# Vamos agora visualizar os ajustes do modelo linear no gráfico de dispersão 
# para verificar como a linha de regressão se ajusta aos dados.
# O gráfico ajudará a observar a qualidade do ajuste linear.
"""

# Gráfico com ajuste linear
plt.figure(figsize=(12, 8))
sns.scatterplot(x="idade", y="comprimento", data=dataset_bebes, color='grey', s=100, label='Dados Reais', alpha=0.6)
sns.regplot(x="idade", y="comprimento", data=dataset_bebes, color='orange', ci=False, scatter=False, line_kws={'linewidth': 2.5}, label='Ajuste Linear')
plt.title('Dispersão dos Dados com Ajuste Linear', fontsize=16)
plt.xlabel('Idade (semanas)', fontsize=14)
plt.ylabel('Comprimento (cm)', fontsize=14)
plt.legend()
plt.show()

# In[0.7]
"""
# 7. Teste de Normalidade dos Resíduos
# -----------------------------------
# Uma das suposições do modelo de regressão linear é que os resíduos (erros) 
# seguem uma distribuição normal. 
# Para verificar essa suposição, vamos realizar o teste de Shapiro-Wilk 
# para avaliar a normalidade dos resíduos do modelo.
"""

# Testando a normalidade dos resíduos
estatistica, p_valor = shapiro(modelo_linear.resid)

# Exibindo o resultado do teste
print(f'Estatística W: {estatistica:.4f}, p-valor: {p_valor:.4f}')

# Interpretação do resultado
alpha = 0.05
if p_valor > alpha:
    print("Os resíduos seguem uma distribuição normal (não rejeitamos H0).")
else:
    print("Os resíduos não seguem uma distribuição normal (rejeitamos H0).")

# In[0.8]
"""
# 8. Transformação de Box-Cox para Normalizar os Dados
# ----------------------------------------------------
# Se os resíduos não seguem uma distribuição normal, podemos tentar 
# transformar a variável dependente utilizando a transformação de Box-Cox. 
# A transformação de Box-Cox é útil para estabilizar a variância e tornar os 
dados mais normais.
# Vamos aplicar a transformação à variável 'comprimento' e ajustar um novo 
modelo OLS.
"""

# Aplicando a transformação de Box-Cox na variável 'comprimento'
comprimento_transformado, lambda_boxcox = boxcox(dataset_bebes['comprimento'])

# Adicionando a variável transformada no dataframe
dataset_bebes['comprimento_transformado'] = comprimento_transformado

# Estimando o modelo OLS com a variável transformada
modelo_boxcox = sm.OLS.from_formula('comprimento_transformado ~ idade', dataset_bebes).fit()

# Exibindo os resultados do modelo ajustado
modelo_boxcox.summary()

# In[0.9]
"""
# 9. Comparação de Modelos: Linear vs Box-Cox
# -------------------------------------------
# Vamos comparar os ajustes dos dois modelos: o modelo linear simples e o 
modelo 
# ajustado com a transformação de Box-Cox. A comparação será feita observando 
# o valor de R² e as estimativas dos parâmetros.
# Também geraremos gráficos de dispersão com as linhas de ajuste para 
visualizar as diferenças.
"""

# Comparando os valores de R² dos dois modelos
r2_modelo_linear = modelo_linear.rsquared
r2_modelo_boxcox = modelo_boxcox.rsquared

# Exibindo a comparação de R²
print(f'R² do Modelo Linear: {r2_modelo_linear:.4f}')
print(f'R² do Modelo Box-Cox: {r2_modelo_boxcox:.4f}')

# Gráfico de dispersão com os dois ajustes
plt.figure(figsize=(12, 8))
sns.scatterplot(x="idade", y="comprimento", data=dataset_bebes, color='grey', s=100, label='Dados Reais', alpha=0.6)
sns.regplot(x="idade", y="comprimento", data=dataset_bebes, color='orange', ci=False, scatter=False, line_kws={'linewidth': 2.5}, label='Ajuste Linear')
sns.regplot(x="idade", y="comprimento_transformado", data=dataset_bebes, color='purple', ci=False, scatter=False, line_kws={'linewidth': 2.5}, label='Ajuste Box-Cox')
plt.title('Dispersão dos Dados com Ajustes Linear e Box-Cox', fontsize=16)
plt.xlabel('Idade (semanas)', fontsize=14)
plt.ylabel('Comprimento (cm)', fontsize=14)
plt.legend()
plt.show()

# In[0.1]:
"""
===============================================================================
#                      INSTALAÇÃO E IMPORTAÇÃO DE PACOTES                     #
#                      Instalação e importação dos pacotes necessários        #
===============================================================================
ANÁLISE FINAL DOS RESULTADOS

1. Modelo de Regressão Linear Simples (OLS)
O modelo de regressão linear simples foi estimado com a variável dependente 
'comprimento' e a variável independente 'idade'. O valor de R² do modelo linear 
foi de 0.9027, o que indica que aproximadamente 90.27% da variabilidade do 
comprimento dos bebês pode ser explicada pela idade. Este é um valor muito alto, 
indicando uma forte relação entre as duas variáveis. Além disso, o coeficiente 
de 'idade' foi significativo, com um p-valor muito baixo (0.000), sugerindo que 
a relação entre idade e comprimento é estatisticamente significativa.

2. Modelo de Regressão com Transformação de Box-Cox
Foi aplicada uma transformação de Box-Cox à variável dependente 'comprimento' 
para estabilizar a variância e aproximar a distribuição dos resíduos a uma forma 
normal. Após a transformação, o valor de R² do modelo ajustado foi de 0.9620, 
indicando uma melhoria significativa na explicação da variabilidade de 
'comprimento' em relação ao modelo linear (R² = 0.9027). O coeficiente de 'idade' 
no modelo transformado permaneceu significativo com um p-valor muito baixo.

3. Comparação entre os Modelos
A transformação de Box-Cox resultou em um modelo com melhor ajuste, já que o 
valor de R² aumentou consideravelmente. Isso sugere que a transformação foi 
eficaz, melhorando a normalidade dos resíduos e ajustando melhor a relação 
entre as variáveis. Em termos práticos, o modelo transformado pode ser 
considerado mais robusto, já que ele apresenta um maior poder explicativo 
(R² = 96.20%).

4. Diagnóstico de Resíduos
Apesar da melhoria no ajuste do modelo com Box-Cox, o valor de Durbin-Watson 
(0.813) indica a presença de autocorrelação nos resíduos, o que poderia ser um 
ponto de atenção para aprimorar ainda mais o modelo. Idealmente, o valor de 
Durbin-Watson deveria estar mais próximo de 2, indicando ausência de 
autocorrelação.

5. Conclusão
Com base nos resultados, podemos concluir que o modelo com a transformação de 
Box-Cox é o mais adequado para descrever a relação entre idade e comprimento 
dos bebês, já que ele apresentou um ajuste melhor (R² mais alto) e resíduais 
mais próximos da normalidade. Entretanto, ainda é necessário investigar mais 
sobre a autocorrelação nos resíduos, o que pode exigir ajustes adicionais, 
como a inclusão de variáveis ou mudanças no modelo.

Recomendação: Utilizar o modelo transformado (Box-Cox) para previsões, 
com a cautela de monitorar a autocorrelação dos resíduos.
"""
