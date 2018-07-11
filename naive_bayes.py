# %%
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder       # , OneHotEncoder
# from sklearn.preprocessing import StandardScaler
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
base = pd.read_excel('Listadedados.xlsx')
# %%
previsores = base.iloc[:, 0:12].values
classe = base.iloc[:, 12].values
# %%
a = list(base.iloc[:,2:4].values)
b = list(base.iloc[:,12].values)
c = []
for i in a:
    c.append(list(i))
c.append(b)
# %%
aux3 = 0
aux1 = 0
k = 0
for i in range(len(c)):
    if c[i][1] == 'Indiferente':
        k += 1
        if c[-1][i] == '3B':
            aux3 += 1
        elif c[-1][i] == '1B':
            aux1 += 1
        else:
            print(c[-1][i])
# %%
labelencoder_previsores = LabelEncoder()
for i in range(1, 11):
    previsores[:, i] = labelencoder_previsores.fit_transform(previsores[:, i])

# %%
"""
onehotencoder = OneHotEncoder(categorical_features=[1, 2, 3, 4, 5,
                                                    6, 7, 8, 9, 10])
previsores = onehotencoder.fit_transform(previsores).toarray()
"""
# %%
"""
labelencoder_classe = LabelEncoder()
classe = labelencoder_classe.fit_transform(classe)
"""
# %%
"""
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)
"""
# %%
aux = []
for pergunta in perguntas:
    aux.append(input(pergunta).strip().capitalize())
teste = pd.DataFrame(aux)
teste = teste.iloc[:, :].values
# %%
for i in range(1, 11):
    teste[i] = labelencoder_previsores.fit_transform(teste[i])
classificador = GaussianNB()
classificador.fit(previsores, classe)
previsao = classificador.predict(teste.T)
print(f'A sala dessa pessoa provavelmente é {previsao[0]}')
