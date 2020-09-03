'''
Capitulo 1

Iniciando a rede de funcionários da ''Empresa Data Sciencester''


'''

# um dict com  id e nome do funcionário na empresa

users = [
    {'id': 0, 'name': 'Hero'},
    {'id': 1, 'name': 'dumn'},
    {'id': 2, 'name': 'Sue'},
    {'id': 3, 'name': 'Chi'},
    {'id': 4, 'name': 'Thor'},
    {'id': 5, 'name': 'Clive'},
    {'id': 6, 'name': 'Hicks'},
    {'id': 7, 'name': 'Deven'},
    {'id': 8, 'name': 'Kate'},
    {'id': 9, 'name': 'klein'},
]
# Ele também fornece dados “amigáveis”, representados por uma lista de pares de IDs:
print(len(users))
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5),
               (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

'''

EX: a tupla (0,1) significa que o usuário de ID 1 tem amizade com ID 2 

'''

# Agora vamos adicionar uma lista de amigo para cada usuário da empresa
# cria uma lista vazia dentro da variável users para cada usuário.. Podemos adiconar os amigos nessa lista vazia
for user in users:
    user['friends'] = []
print(users)

# Então povoamos a nova lisa vazia com os dados de friendship.

for i, j in friendships:  # as duas chaves usadas na variavel friendship
    users[i]['friends'].append(users[j])  # adiciona i como amigo de j
    users[j]['friends'].append(users[i])  # adiciona j como amigo de i
print(users)


# Qual o número médio de conexões?

# 1- Encontra no número total de conexões

def number_of_friends(user):
    '''
    Quantos amigos o usuário tem?
    :param user:
    :return: numero total de amigos utilizando a função len
    '''
    return len(user['friends'])  # tamanho da lista friend_id


total_connections = sum(number_of_friends(user)
                        for user in users)
print(total_connections)  # 24

# Dvividimos pelo numero total da lista, seria algo como total_connections/sum

avg_connections = total_connections / len(users)  # colocar a divisão numa variável para ser usada depois
print(avg_connections)

# As pessoas mais conectadas, são as que possuem o maior numero de amigos, como não há muitos usuários podemos ordena-los como ''muitos amigos'' para ''menos amigos''

# cria uma lista com (user_id, number of friends)
num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]
print(num_friends_by_id)  # numero do id do usuario e qts amigos ele tem

# é ordenado por num_friends do maior para o menor
# ordenado = sorted(num_friends_by_id, key=lambda(user_id, num_friends): num_friends, reverse=True)

'''
Uma maneira de pensar sobre o que nós fizemos é uma maneira de identificar as
pessoas que são, de alguma forma, centrais para a rede. Na verdade, o que
acabamos de computar é uma rede métrica de grau de centralidade.

Primeiro - sugerir um usuário que conheça amigos de amigos: para cada amigo de um usuario, ele itera sobre 
os amigos daquela pessoa, e coleta todos os resultados.. como fazer isso?

'''


def friends_of_friend_ids_bad(user):
    # “foaf” é abreviação de “friend of a friend”
    return [foaf["id"]
            for friend in user["friends"]  # para cada amigo de usuário
            for foaf in friend["friends"]]  # pega cada _their_friends


print(friends_of_friend_ids_bad(users[3]))
'''
Isso inclui o usuário 0 (duas vezes), uma vez que Hero é, de fato, amigo de
ambos os seus amigos. Inclui os usuários 1 e 2, apesar de eles já serem amigos
do Hero. E inclui o usuário 3 duas vezes, já que Chi é alcançável por meio de
dois amigos diferentes:'''
print([friend["id"] for friend in users[0]["friends"]])  # [1, 2]
print([friend["id"] for friend in users[1]["friends"]])  # [0, 2, 3]

from collections import Counter


def not_the_same(user, other_user):
    '''dois usuários não são os mesmos se possuem id diferentes'''
    return user['id'] != other_user['id']


def not_friends(user, other_user):
    '''other_friends não é um amigo se não está em user['friends'];
    isso é, se é not_the_same com todas as pessoas em user['friends']'''
    return all(not_the_same(friend, other_user)
               for friend in user['friends'])


def friends_of_friend_ids(user):
    return Counter(foaf["id"]

                   for friend in user["friends"]  # para cada um dos meus amigos
                   for foaf in friend["friends"]  # que contam *their* amigos
                   if not_the_same(user, foaf)  # que não sejam eu
                   and not_friends(user, foaf))  # e que não são meus amigos


print(friends_of_friend_ids(users[3]))  # Counter({0: 2, 5: 1})

print(friends_of_friend_ids(users[4]))
'''
Explicação
dados: # Counter({0: 2, 5: 1})
        - o numero de ID: 3 é a Chi
- o que sabemos sobre a Chi?
        - Ela possui 2 amigos em comum com Hero(id 0) mas somente um amigo com Clive(id 5)
'''

# Descobrindo interesses em comum a parti de uma lista de interesses compartilhado a parti dos ids
# (user_id, interest)
# alguns usuários não possuem nenhum amigo em comum mas possuem interesses em comum, e como descobrir?

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]
print(interests)


# Contruindo uma função com usuarios basedos no mesmo intresse

def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest

            ]


print(data_scientists_who_like(users[4]))

from collections import defaultdict

# as chaves são interesses, os valores são listas de user_id com interests

user_ids_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_interest[interest].append(user_id)

# as chaves são user_ids, os valores são as listas de interests para aquele user_id

interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

'''
Agora fica fácil descobrir quem possui os maiores interesses em comum com um certo usuário:
    -Itera sobre os interesses do usuário.
    -Para cada interesse, itera sobre os outros usuários com aquele interesse.
    -Mantém a contagem de quantas vezes vemos cada outro usuário.
'''


def most_common_interests_with(user):
    return Counter(interested_user_id
                   for interest in interests_by_user_id[user["id"]]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user["id"])


# SALÁRIOS E EXPERIÊCIA
'''
   Analisando uma lista com salário e experiência, obteremos informações como a experiência influêcia o valor do salário,
   Em um segundo tópico pode análisar a média salaria dos funcionários 

    '''
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# as chaves são os anos, os valores são as listas dos salários para cada ano
salary_by_tenure = defaultdict(list)  # retorno defaultdict(<class 'list'>, {})

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

print(salary_by_tenure)

# as chaves são os anos, cada valor é a média salarial para aquele ano
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

print(average_salary_by_tenure)

# E SE AGRUPAR OS CASOS?
