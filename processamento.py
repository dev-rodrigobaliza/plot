import pandas as pd


# leitura dos dados csv
df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")

def getDataHead(n):
    # visualizando as primeiras n linhas
    return df.head(n)

def getDescribe():

    # estatísticas básicas
    return df.describe()

def getInfo():

    # dataframe info
    df.info()

def create_bar():
    ax = df.plot.barh(x='date', y=['temperatura'])
    fig = ax.get_figure()
    ax.set_title("Temperatura por Data");
    return fig