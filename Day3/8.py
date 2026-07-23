# The tail() method can also be used on a Pandas Series to retrieve the last few elements.
# This is useful when we're working with a single column of data and want to quickly inspect its contents.
#  
import pandas as pd
data = pd.read_csv(r"D:\Basic-Python\Day3\nba.csv")
salary = data['Salary']
print("Last 5 Salaries:")
print(salary.tail())