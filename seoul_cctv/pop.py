import pandas as pd

ctx = '../data/'
pop = ctx + 'population_in_Seoul.xls'
csv = ctx + 'CCTV_in_Seoul.csv'
cctv_data = pd.read_csv(csv)
pop_data = pd.read_excel(pop)
print(cctv_data.head())
print(" ")
print(pop_data.head())
