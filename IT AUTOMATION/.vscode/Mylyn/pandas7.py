#Python Pandas Tutorial (Part 8): Grouping and Aggregating - Analyzing and Exploring Your Data
#https://www.youtube.com/watch?v=txMdrV1Ut64&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=8
import pandas as pd


pd_schema = pd.read_csv(r'C:/Users/rnsri/Stackoverflow/survey_results_schema.csv')
pd_public = pd.read_csv(r'C:/Users/rnsri/Stackoverflow/survey_results_public.csv')

pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)
df_pub = pd.DataFrame(pd_public)
df_schema = pd.DataFrame(pd_schema)