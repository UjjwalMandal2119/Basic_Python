import pandas as pd
data = pd.read_csv(r"D:\Basic-Python\Day3\nba.csv")
series = data["Name"]
bottom = series.tail(n = 7)
print("NBA Dataset (Last 7 Rows):")
print(bottom)