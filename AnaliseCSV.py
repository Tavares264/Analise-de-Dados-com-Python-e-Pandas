import pandas as pd

df = pd.read_csv("./datasets/Gapminder.csv", delimiter=';')

print(df.head())

print('===============================================================================================')

df = df.rename(columns={"country":"Pais", "continent": "continente", "year":"Ano", "lifeExp":"Expectativa de vida", "pop":"Pop Total", "gdpPercap": "PIB"})

print(df.head(10))

print('===============================================================================================')

print(df.shape)

print('===============================================================================================')

print(df.columns)

print('===============================================================================================')

print(df.dtypes)

print('===============================================================================================')

print(df.tail(15))

print('===============================================================================================')

print(df.describe())

print('===============================================================================================')

df["continente"].unique()

print('===============================================================================================')

Oceania = df.loc[df["continente"] == "Oceania"]
print(Oceania.head())

print('===============================================================================================')

print(Oceania["continente"].unique())

print('===============================================================================================')

print(df.groupby("continente")["Pais"].nunique())

print('===============================================================================================')

print(df.groupby("Ano")["Expectativa de vida"].mean())

print('===============================================================================================')

print(df["PIB"].mean())

print('===============================================================================================')

print(df["PIB"].sum())