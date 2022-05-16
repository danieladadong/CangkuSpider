import pandas as pd
path ='content.csv'
df = pd.read_csv(path,encoding='utf-8 sig')
for i in df:
    print(df)
