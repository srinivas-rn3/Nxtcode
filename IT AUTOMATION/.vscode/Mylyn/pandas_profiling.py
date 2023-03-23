'''
Pandas Profiling in Python
The pandas_profiling library in Python include a method named as ProfileReport() which 
generate a basic report on the input DataFrame. 

The report consist of the following:

DataFrame overview,
Each attribute on which DataFrame is defined,
Correlations between attributes (Pearson Correlation and Spearman Correlation), and
A sample of DataFrame.
'''
import pandas as pd
import pandas_profiling as pp


data1 = pd.read_csv(r'C:\Users\srini\OneDrive\Documents\Titanic_Data\train.csv')

train_data = pd.DataFrame(data1)
print(train_data)
profile = pp.ydata_profiling(data1)
profile.to_file(r"C:\Users\srini\OneDrive\Documents\Titanic_Data\output.html")