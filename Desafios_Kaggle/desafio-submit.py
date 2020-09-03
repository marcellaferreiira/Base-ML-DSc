'''Modo para colocar arquivos .csv no Pycharm usando Python'''

import csv

with open('Documentos/titanic//submissin.csv', 'rb') as ficheiro:
    reader = csv.reader(ficheiro)
    for linha in reader:
            print(linha)
