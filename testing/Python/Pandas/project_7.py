import pandas as pd
import numpy as np
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()
df['col2'].unique()
df['col2'].nunique()
df['col2'].value_counts()
#Select from DataFrame using criteria from multiple columns
newdf = df[(df['col1']>2) & (df['col2']==444)]
print(newdf)
def times2(x):
    return x*2
df['col1'].apply(times2)
df['col3'].apply(len)
df['col1'].sum()
del df['col1']
print(df)
print(df.columns)
print(df.index)
print(df)
print(df.sort_values(by='col2')) #inplace=False by default
df.isnull()
# Drop rows with NaN Values
df.dropna()

df = pd.DataFrame({'col1':[1,2,3,np.nan],
                   'col2':[np.nan,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
df.head()
print(df.fillna('FILL'))
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print(df)
print(df.pivot_table(values='D',index=['A', 'B'],columns=['C']))

