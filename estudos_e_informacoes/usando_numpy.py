'''
NumPy -
links:
https://medium.com/ensina-ai/entendendo-a-biblioteca-numpy-4858fde63355
http://www.estruturas.ufpr.br/disciplinas/pos-graduacao/introducao-a-computacao-cientifica-com-python/introducao-python/2-1-o-objeto-array-do-numpy/

    O que  numpy??

O NumPy é uma poderosa biblioteca Python que é usada principalmente para realizar cálculos em
Arrays Multidimensionais. O NumPy fornece um grande conjunto de funções e operações de biblioteca que
ajudam os programadores a executar facilmente cálculos numéricos. Esses tipos de cálculos numéricos
são amplamente utilizados em tarefas como:

-- Exemplos  em modelos de machine learning

Ao escrever algoritmos de Machine Learning, supõe-se que se realize vários cálculos numéricos em Array.
Por exemplo, multiplicação de Arrays, transposição, adição, etc. O NumPy fornece uma excelente biblioteca
para cálculos fáceis (em termos de escrita de código) e rápidos (em termos de velocidade).
Os Arrays NumPy são usados para armazenar os dados de treinamento, bem como os parâmetros
dos modelos de Machine Learning.

--Numpy para tarefas matematicas
NumPy é bastante útil para executar várias tarefas matemáticas como integração numérica,
diferenciação, interpolação, extrapolação e muitas outras. O NumPy possui também funções incorporadas
para álgebra linear e geração de números aleatórios. É uma biblioteca que pode ser usada em conjuto do SciPy
e Mat-plotlib.Substituindo o MATLAB quando se trata de tarefas matemáticas.


        -O que são arrays em Numpy?
A estrutura de dados mais importante que o NumPy fornece é um objeto poderoso,
um tipo de Array, chamada ndarray. O objeto ndarray consiste em um segmento unidimensional
contíguo da memória do computador, combinado com um esquema de indexação que mapeia cada item para
um local no bloco de memória.

'''

#Exemplos

import numpy as np
lista = [1, 2, 3, 4, 5]
np.array([1, 2, 3])
print(np)

#Com mais dimensões
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np.array(matriz)

#usando no jupyter
#criação de vetores e arrays

#Unidimensionais:

'''
import numpy as np
a = np.array([0, 1, 2, 3])
a
a.ndim
a.shape
len(a)'''

#Bidimensionais:

'''
b = np.array([[0, 1, 2], [3, 4, 5]])    # 2 x 3 array
b
b.ndim
b.shape
len(b)
'''

#Tridimensionais:
'''
c = np.array([[[1], [2]], [[3], [4]]])
c
c.shape
'''

#Espaçados igualmentes

'''
import numpy as np

a = np.arange(10) # 0 .. n-1
a
b = np.arange(1, 9, 2) # início, fim (exclusive), passo
b
'''

# por número de pontos

'''
c = np.linspace(0, 1, 6)   # início, fim, número de pontos
c
d = np.linspace(0, 1, 5, endpoint=False)
d
'''

#Matrizes comuns:

'''
a = np.ones((3, 3))  # lembrete: (3, 3) é uma tupla
a
b = np.zeros((2, 2))
b
c = np.eye(3)
c
d = np.diag(np.array([1, 2, 3, 4]))
d
'''

# Números aleatórios:

'''
a = np.random.rand(4)       # uniforme em [0, 1]
a
b = np.random.randn(4)      # Gaussiana
b

np.random.seed(1234)        # Definindo um início
'''

#Tipos básicos de dados

'''

EXEMPLO 1

a = np.array([1, 2, 3])
a.dtype
dtype('int64')

b = np.array([1., 2., 3.])
b.dtype


2
c = np.array([1, 2, 3], dtype=float)
c.dtype

3
a = np.ones((3, 3))
a.dtype

4- mais complexos 
d = np.array([1+2j, 3+4j, 5+6*1j])
d.dtype

5 - booleano
e = np.array([True, False, False, True])
e.dtype

6-strings
f = np.array(['Bonjour', 'Hello', 'Olá',])
f.dtype



'''