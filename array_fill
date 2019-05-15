import pandas as pd
df = pd.read_csv('vivid5456.csv', sep=";", names = ['name', 'a', 'b']).fillna(0)
df.a=df.a.apply(lambda x: str(x)[0])
df.b=df.b.apply(lambda x: str(x)[0])
df.groupby(['name', 'a', 'b']).size().to_csv('5456GOTOVO.csv')
