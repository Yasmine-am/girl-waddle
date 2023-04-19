#Data verzamelen doormiddel van een CSV bestand lezen met Python

print("Start CSV read applicatie")

import pandas 

df = pandas.read_csv('pokemon.csv')
print(df["Name"])

for rij in df.iterrows():
    print(rij)

    # Yasmine en Richelle zijn cool & moe.