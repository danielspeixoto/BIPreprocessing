import pandas as pd
import os


def process():
    if os.path.isfile('aplicativo_preprocessed.csv'):
        return pd.read_csv('aplicativo_preprocessed.csv')

    else:
        # Data gathering
        data = pd.read_csv('aplicativo.csv')

        # Drops DDD
        data.drop('DDD_USUARIO', axis=1, inplace=True)

        # Drops TOTAL_PEDIDO
        data.drop('TOTAL_PEDIDO', axis=1, inplace=True)

        # Makes weekday numerical, where monday starts with 0
        weekdays = {
            'Monday': 0,
            'Tuesday': 1,
            'Wednesday': 2,
            'Thursday': 3,
            'Friday': 4,
            'Saturday': 5,
            'Sunday': 6
        }
        data['DIA_PEDIDO'] = data['DIA_PEDIDO'].apply(lambda day: weekdays[day])

        # Make binary and rename to "Entregue"
        data['STATUS'] = data['STATUS'].apply(lambda status: status == 'Entregue')
        data.rename(columns={'STATUS': 'ENTREGUE'}, inplace=True)

        # Makes binary
        data['PRIMEIRO_PEDIDO'] = data['PRIMEIRO_PEDIDO'].apply(lambda status: status == 'Sim')

        # Finds which orders had a feedback
        data['FEEDBACK'] = data['AVALIACAO'].apply(lambda rating: not pd.isna(rating))

        # Gets DATETIME from DATA and Hora
        data['DATETIME'] = pd.to_datetime(data['DATA_PEDIDO'] + ' ' +  data['HORA_PEDIDO'])

        # Convers DATA_CADASTRO to datetime
        data['DATA_CADASTRO_USUARIO'] = pd.to_datetime(data['DATA_CADASTRO_USUARIO'])

        # Gets Date from DATA_PEDIDO
        data['DATA'] = data['DATA_PEDIDO'].apply(lambda date: date[5:])

        # HORA_PEDIDO does not show minutes anymore
        data['HORA_PEDIDO'] = data['HORA_PEDIDO'].apply(lambda time: time[:3])
        data.drop('DATA_PEDIDO', axis=1, inplace=True)

        # Prints head as it is
        # print(data.head(50).to_string())

        data.to_csv('aplicativo_preprocessed.csv')
        return data