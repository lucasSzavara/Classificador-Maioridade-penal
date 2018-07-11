# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 18:50:22 2018

author: Lucas dos Santos Rodrigues Szavara
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing as ppc
from sklearn.preprocessing import LabelEncoder


def sinal(u):
    if u < 0:
        return -1
    return 1


perguntas = ['Qual a sua idade? ', 'Qual seu gênero? (M/F) ', 'Você acha a maioridade necessária? (Sim/Não/Não-Sei) ',
             'Você está satisfeito com a maioridade penal no Brasil Atualmente? (Sim/Não/Indiferente) ',
             'Você acredita que no caso de crimes hediondos cometidos por menores deveria haver redução penal? (Sim/Não/Não-Sei) ',
             'Você tem convicção de que a taxa de crimes seria reduzida com a redução da maioridade penal? (Sim/Não/Não-Sei) ',
             'Prender adolescentes agravaria a péssima condição dos presídios? (Sim/Não/Não-Sei) ',
             'Você acredita que um menor, de 13 a 16 anos de idade, já pode discernir os seus atos? (Sim/Não/Não-Sei) ',
             'A idade pode definir a responsabilidade de uma pessoa? (Sim/Não) ',
             'O responsável pelo menor de idade que cometeu um crime pode ser responsabilizado? (Sim/Não/Não-Sei) ',
             'Você é a favor do Brasil adotar a maioridade penal dos EUA (10 anos – juventude, 12 a 16 – adulto)? (Sim/Não/Indiferente) ',
             'Qual a idade que você acha ideal para ser a maioridade penal? ']
base = pd.read_excel("Listadedados.xlsx")
aux = [-1 for i in range(73)]
base['x0'] = pd.Series(aux)
del aux
# %%
base = base[['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8',
             'x9', 'x10', 'x11', 'x12', 'z']]
# %%
previsores = base[['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7',
                   'x8', 'x9', 'x10', 'x11', 'x12']].values
classe = base[['z']].values
labelencoder_previsores = LabelEncoder()
aux_classe = []

for i in classe.__iter__():
    if i[0] == '1B':
        aux_classe.append(-1)
    else:
        aux_classe.append(1)

classe = np.asarray(aux_classe)
del aux_classe

for i in range(2, 12):
    previsores[:, i] = labelencoder_previsores.fit_transform(previsores[:, i])
# %%
previsores = ppc.scale(previsores)
previsores[:, 0] = -1
# %%
pesos = np.random.rand(13)
rate = 0.01
epoca = 0
erro = 'existe'
# %%
while erro != 'inexiste':
    erro = 'inexiste'
    for k in range(30):
        u = pesos.T.dot(previsores[k])
        y = sinal(u)
        if y != classe[k]:
            erro = 'existe'
            pesos = pesos + rate * (classe[k] - y) * previsores[k]
    epoca += 1

aux = [-1]
for pergunta in perguntas:
    aux.append(input(pergunta).strip().capitalize())
teste = pd.DataFrame(aux)
teste = teste.iloc[:, :].values
# %%
del aux
for i in range(2, 12):
    teste[i] = labelencoder_previsores.fit_transform(teste[i])
# %%
u = pesos.T.dot(previsores[k])
y = sinal(u)
if y == -1:
    print('1ºB')
else:
    print('3ºB')
