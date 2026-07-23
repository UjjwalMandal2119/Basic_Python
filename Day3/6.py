# Let's see an example: Using tail() on a DataFrame
# We will use the tail() method to retrieve the last few rows of a DataFrame. This provides a quick preview of the dataset’s structure and contents. By default, the method returns and stores the last 5 rows of the DataFrame in a new variable but we can customized this to return any number of rows.
#  
import pandas as pd
data = pd.read_csv(r"D:\Basic-Python\Day3\nba.csv")
print("NBA Dataset (Last 5 Rows):")
print(data.tail())