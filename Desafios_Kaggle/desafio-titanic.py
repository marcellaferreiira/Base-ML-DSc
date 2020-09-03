'''

Desafio - titanic

linguagem-Python
competição-Titanic


OBS: passos para resolver os desafios
1º Passo - Escolha a sua linguagem
2º Passo - Encontre uma competição
3º Passo - Compreenda o dataset
4º Passo - Aprenda com a comunidade

ABORDAGEM RÁPIDA SOBRE MACHINE LEARNING
Machine Learning é um método de aprendizado de máquina que automatiza a construção de modelos analíticos.
Baseia-se em ensinar máquinas através de modelos de algoritmos.

Pode ser divididos em três modelos de aplicação:
Aprendizagem supervisionada;
Aprendizagem não supervisionada;
Aprendizagem por reforço.

Exemplo no caso do Titanic

SUPERVISIONADO

Com modelos supervisionados,é possível prever quais passageiros tem mais chances de sobreviver.
O modelo toma como base algumas variáveis, como, classe, sexo, idade, número de filhos e etc.

NÃO-SUPERVSIONADO

Com a aprendizagem não supervisionados, temos pouca ideia do resultado.
Nesse contexto, utilizamos estruturas de dados que não sabemos realmente o efeito das variáveis.


REVISÃO SOBRE ALGORITMOS DE APRENDIZADO:

Algoritmos de aprendizado
Existem diversos algoritmos de Machine Learning.

Regressão Linear: É a melhor forma de descrever a relação entre duas variáveis.
Tem como objetivo traçar um valor que não é possível estimar inicialmente.
Faz parte do aprendizado supervisionado. O objetivo da regressão linear é encontrar a
equação que ajuste a melhor linha para modelar os dados;

Clustering: Conhecido também como análise de agrupamento, consiste em agrupar cada ponto
do conjunto de dados em um grupo específico. Os dados que são agrupados juntos compartilham
uma semelhança entre si. Clustering é um exemplo de método de aprendizado não supervisionado;

q-learning: É o método mais popular de aprendizado por reforço. Permite estabelecer uma política de
ações de forma interativa e mostrar qual comportamento tomar em determinadas circunstâncias.

ETAPAS NO PROCESSO

Conhecendo nossos dados- Conhecer as colun as do dataset

Configurações iniciais- importar as bibliotecas necessárias

fazer o download do dataset ( df = pd.read_csv('dataset')



'''

# fazendo a importação das bibliotecas necessárias

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
% matplotlib
inline

# Fazer o download do dataset

df = pd.read_csv('dataset')

# verificando as amostras do dataset - ANÁLISE EXPLORATORIA

df.sample()

df.head()

df.columns

list(df.columns)

df.shape

df['coluna'].value_counts

# Verificar os tipos de dados nas colunas (quantitativos ou qualitativas)
# qualitataivas - nominal, ordinal
# quantitativas- discreta, contínua

# retirando colunas que não são necessarias

df.drop('coluna', axis=1, inplace=True)

# Verificar se tem valores faltantes

df.isna().any()  # retorna valores booleanos

df.isna().sum()  # retorna a soma dos valores faltantes

# MODOS DE LIMPAR OS VALORES FALTANTES
'''
- FAZENDO UM DROP DE TODOS OS VALORES FALTANTES
- TROCAR OS VALORES FALTANTES PELA MÉDIA OU MÉDIANA 

em ambos os casos vai depender da quantidade de dados e da quantidade de dados dos valores faltantes
'''

# Modos de limpar os dados faltantes

# descartando as linhas que tem poucos valores faltantes
df.dropna(axis=0, subset=['director_name', 'num_critic_for_reviews', inplace = True]

# substituir valores faltantes por uma variavel
df['content_rating'].fillna('R', inplace=True)

# substituindo os valores faltantes pela mediana dos valores
df['aspect_ratio'].fillna(df['aspect_ratio'].median(), inplace=True)

# outra forma de fazer
# Criando uma instancia Imputer para substituir os valores faltantes pela média
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="median")

# <h4>A mediana apenas pode ser aplicada em valores numéricos, portanto,
# temos que separar do dataset as colunas que não são numéricas.

list(treino.columns)
['PassengerId',
 'Survived',
 'Pclass',
 'Sex',
 'Age',
 'SibSp',
 'Parch',
 'Fare',
 'Embarked']
list(teste.columns)
['PassengerId', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
# criando uma nova tabela retirando as colunas não numericas - sexo e embarque
treino_numerico = treino.drop(['Sex', 'Embarked'], axis=1)
, axis = 1
teste_numerico = teste.drop(['Sex', 'Embarked'], axis=1)
# Agora, nós podemos aplicar o método fit() .
# A função fit () calcula os valores desses parâmetros
# parte da preparação do imputer
func = imputer.fit(treino_numerico)
print(func)
SimpleImputer(strategy='median')
# Como já temos o Imputer preparado, podemos preencher os valores que estão nulos.
treino_nao_nulo = imputer.transform(treino_numerico)

# fazendo a mesma coisa para o teste
imputer.fit(teste_numerico)
teste_nao_nulo = imputer.transform(teste_numerico)
# imputer.transform() devolve um array NumPy com as colunas modificadas.

'''
Temos que transformar isso em um DataFrame, criando assim uma variavel para alocar esse novo dataframe
df_treino = pd.DataFrame(treino_nao_nulo, columns= treino_numerico.columns)
D
df_teste = pd.DataFrame(teste_nao_nulo, columns = teste_numerico.columns)
Podemos verificar novamente se temos algum valor nulo no dataset de treino.
df_treino.columns
Index(['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare'], dtype='object')
es numericos 
#conferindo as colunas do dataframe, e está apenas com as colunas de valores numericos 
df_treino.head()
PassengerId	Survived	Pclass	Age	SibSp	Parch	Fare
0	1.0	0.0	3.0	22.0	1.0	0.0	7.2500
1	2.0	1.0	1.0	38.0	1.0	0.0	71.2833
2	3.0	1.0	3.0	26.0	0.0	0.0	7.9250
3	4.0	1.0	1.0	35.0	1.0	0.0	53.1000
4	5.0	0.0	3.0	35.0	0.0	0.0	8.0500
ino.shape
#conferindo a quantidade de dados 
df_treino.shape
(891, 7)
#conferindo os dados nulos
df_treino.isna().sum()
PassengerId    0
Survived       0
Pclass         0
Age            0
SibSp          0
Parch          0
Fare           0
dtype: int64
## Manipulando valores categóricos
​
Acima, nós removemos as colunas Sex e Embarked, pois são valores categóricos, consequentemente não é possível calcular a sua mediana.A maioria dos algoritmos de Machine Learning preferem trabalhar com valores numéricos. Em vista disso, vamos converter os valores categóricos em numéricos utilizando a técnica One Hot Encoding.
​
'''
# Será necessário selecionar as colunas categóricas. - sex, embarked
treino_gato = treino[['Sex', 'Embarked']]
treino_gato.head()

teste_gato = teste[['Sex', 'Embarked']]
teste_gato.head()