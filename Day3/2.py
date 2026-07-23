import pandas as pd

data = pd.read_csv(r"D:\Basic-Python\Day3\nba.csv")

series = data["Name"]

top = series.head(n=7)

print("NBA Dataset (First 7 Rows):")
print(top)