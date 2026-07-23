# 5. Using head() After Sorting a DataFrame
# Here we will use head() to inspect the first few rows of a DataFrame after sorting it by a specific column.
# This is useful when we want to identify the top records based on a specific criterion like the highest salary or the youngest player.
#  
import pandas as pd
data = pd.read_csv(r"D:\Basic-Python\Day3\nba.csv")
sorted_data = data.sort_values(by='Age', ascending=True)
top_sorted = sorted_data.head()
print("First 5 Rows After Sorting by Age:")
print(top_sorted)