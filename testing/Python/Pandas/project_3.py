import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,4), index=['a', 'b', 'c', 'd', 'e'], columns=['w', 'x', 'y', 'z'])

print(df)
print(df['w'])
#print(df['w','z'])
#print(df['w']['a'])
#print(df['a']['w'])

df = df.drop('z', axis=1)

print(df)
k = df['w'] + df['y']
print(k)
print(df.loc['a','w'])
print(df[df['w']>0]['y'])
