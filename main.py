from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
import preprocessing
import numpy as np
import plots.pie as pie

data = preprocessing.process()

dispXSpending = data.groupby(
    [data['SO_DISPOSITIVO']])['VALOR_PRODUTOS']

info = dispXSpending.sum()

#pie.plot(info)

########################################
single = [[0 for _ in range(7)] for _ in range(24)]
for index, row in data.iterrows():
    single[row['HORA_PEDIDO']][row['DIA_PEDIDO']] += 1

df = DataFrame(single, index=range(0, 24, 1), columns=range(0, 7, 1))

sns.heatmap(df, cmap=plt.get_cmap('gray_r'))

plt.ylabel("Hora")
plt.xlabel("Dia (Segunda=0)")
plt.title("Momentos com mais pedidos")
# plt.figure()

########################################

# Momentos com mais valores nas vendas
mean = [[0 for _ in range(7)] for _ in range(24)]
for index, row in data.iterrows():
    mean[row['HORA_PEDIDO']][row['DIA_PEDIDO']] += row['VALOR_PRODUTOS']

for i in range(24):
    for j in range(7):
        if single[i][j] != 0:
            mean[i][j] /= single[i][j]

df = DataFrame(mean, index=range(0, 24, 1), columns=range(0, 7, 1))


sns.heatmap(df, cmap=plt.get_cmap('gray_r'))
plt.ylabel("Hora")
plt.xlabel("Dia (Segunda=0)")
plt.title("Horarios que as pessoas gastam mais")
plt.figure()

########################################################
feedbackXSO = data.groupby(
    [data['SO_DISPOSITIVO']])['FEEDBACK']

fsoCount = feedbackXSO.count()
fsoSum = feedbackXSO.sum()

names = fsoSum.index
ind = np.arange(len(names))

plt.bar(ind, fsoSum/fsoCount, 1)

plt.xticks(ind, fsoSum.index)
plt.title("Porcentagem de feedback por plataforma")
plt.figure()

##########################################################
loc = data.groupby([data['BAIRRO_USUARIO']])['PRIMEIRO_PEDIDO']
locSum = loc.sum()
newbies = 0
for row in locSum:
    newbies += row

locSum = locSum.nlargest(5)

names = []
for i in locSum.index:
    names.append(unicode(i, 'utf-8'))
ind = np.arange(len(names))

plt.xticks(ind, names)
plt.title("Bairros com maior crescimento de usuarios")
plt.bar(ind, locSum/newbies, 1)
plt.show()

