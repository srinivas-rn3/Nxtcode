'''
In this example:

extract_data():simulates the extraction process. In a real-world scenario, you would read data from various sources such as databases, files (e.g., CSV, Excel), APIs, etc.
transform_data(df):performs some basic transformations on the extracted data. Here, we're adding a column for yearly income and categorizing age into groups.
load_data(df):simulates loading the transformed data into a target database or data warehouse. In this example, it simply prints the transformed data.

You can extend this example by integrating with real data sources, adding more complex transformations, and using a real database
or data warehouse for loading the data. Additionally, libraries like pandas, numpy, and sqlalchemy are commonly used in Python for ETL tasks.
'''

import pandas as pd 
import numpy as np 

## Simulated data extraction
def extract_data():
    data ={
        'id': [1, 2, 3, 4, 5],
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
        'age': [25, 30, 35, 40, 45],
        'salary': [50000, 60000, 70000, 80000, 90000]
    }
    df = pd.DataFrame(data)
    return df 

#Transformation function

def transformation_data(df):
    # Example transformation: Convert salary to yearly income by multiplying by 12
    df['yearly_income'] = df['salary'] * 12
    
     # Example transformation: Create a new column for age group
    df['age_group'] = pd.cut(df['age'],bins=[0,30,40,np.inf],labels=['<30','30-40','>40'])
    
    #Name Upper case
    df['name'] = df['name'].str.upper()
    
    return df 

# load function

def load_data(df):
     # Simulated target database or data warehouse
    # For simplicity, printing the transformed data here
    print("Transformed Data: ")
    print(df)
    
# ETL pipeline
def etl_pipeline():
    # Extract data
    extracted_data = extract_data()
    
    # Transform data
    transformed_data = transformation_data(extracted_data)
    
    # Load Data
    load_etl_data = load_data(transformed_data)

#Execute the ETL pipeline
etl_pipeline()    
####################################
print("----------------------------------------")
'''
pd.cut() is a function provided by the pandas library in Python that is used to segment and sort data values into bins or intervals. 
This function is particularly useful for converting continuous data into categorical data by binning the values into discrete intervals.
'''
print("pandas cut")
# Create a sample DataFrame
data = {
    'values': [10, 15, 20, 25, 30, 35, 40,60]
    }

df = pd.DataFrame(data)

# Define the bins
bins = [0,20,40,60]
lables = ['low','medium','high']

#Cut the data into bins
df['bins'] = pd.cut(df['values'],bins=bins,labels=lables)
print(df)