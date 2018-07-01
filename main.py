import preprocessing
import plots.pie as pie

data = preprocessing.process()

dispXSpending = data.groupby(
    [data['SO_DISPOSITIVO']])['VALOR_PRODUTOS']

info = dispXSpending.sum()

pie.plot(info)
