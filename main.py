from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
import preprocessing
import plots.pie as pie

data = preprocessing.process()

dispXSpending = data.groupby(
    [data['SO_DISPOSITIVO']])['VALOR_PRODUTOS']

info = dispXSpending.sum()

# pie.plot(info)


########################################
n = [[0 for _ in range(7)] for _ in range(24)]
for index, row in data.iterrows():
    n[row['HORA_PEDIDO']][row['DIA_PEDIDO']] += 1

df = DataFrame(n, index=range(0, 24, 1), columns=range(0, 7, 1))

# _r reverses the normal order of the color map 'RdYlGn'
sns.heatmap(df, cmap=plt.get_cmap('gray_r'))

plt.ylabel("Hora")
plt.xlabel("Dia (Segunda=0)")
plt.title("Momentos com mais pedidos")
plt.show()

########################################

# Momentos com mais valores nas vendas
n = [[0 for _ in range(7)] for _ in range(24)]
for index, row in data.iterrows():
    n[row['HORA_PEDIDO']][row['DIA_PEDIDO']] += row['VALOR_PRODUTOS']

df = DataFrame(n, index=range(0, 24, 1), columns=range(0, 7, 1))

# _r reverses the normal order of the color map 'RdYlGn'
sns.heatmap(df, cmap=plt.get_cmap('gray_r'))

plt.show()