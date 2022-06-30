import csv
import pandas as pd

df = pd.read_csv("data.csv")

df["mass"] = float(df["mass"])
df["radius"] = float(df["radius"])

df["mass"] = df["mass"] * 0.000954588
df["radius"] = df["radius"] * 0.102763

df = df.dropna(axis='columns')

headers = df.columns
planet_data = df.iloc[0].tolist()

print(planet_data)

with open("sorted.csv", "a+", newline="") as f:
    csv_writer = csv.writer(f)

    csv_writer.writerow(df.columns)
    csv_writer.writerow(planet_data)