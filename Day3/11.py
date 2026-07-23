        # In this example, we will sort the DataFrame by the "Age" column and then use tail() to preview the oldest players.
        # This shows how tail() can be used in combination with sorting to inspect specific records.
import pandas as pd
    
data = pd.read_csv(r"D:\Basic-Python\Day3\nba.csv")
sorted_data = data.sort_values(by='Age', ascending=False)
bottom_sorted = sorted_data.tail()
print("Last 5 Rows After Sorting by Age:")
print(bottom_sorted)