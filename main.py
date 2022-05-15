import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df1 = pd.read_csv("spl1.csv")  # данные по длине спор гриба
df2 = pd.read_csv("spb.csv")  # данные по ширине спор гриба 

df12 = pd.DataFrame(data={
    'df1': df1['experiments'],
    'df2': df2['experiments'],
})


d1 = df12['df1']
d2 = df12['df2']

print(stats.kstest(d1, 'norm', (d1.mean(), d1.std()), N=5000))
print(stats.kstest(d2, 'norm', (d2.mean(), d2.std()), N=5000))

