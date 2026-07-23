    # We can also use the tail() method to preview specific columns of our dataset.
    #  This example focuses on previewing just the "Name" and "Salary" columns.
    #  
import pandas as pd
data = pd.read_csv(r"D:\Basic-Python\Day3\nba.csv")
salary_name = data[['Name', 'Salary']].tail()
print("Last 5 Rows of Name and Salary Columns:")
print(salary_name)