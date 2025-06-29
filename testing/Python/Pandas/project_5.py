import numpy as np
import pandas as pd

df = pd.DataFrame({'A':[1,2,np.nan],
			'B': [5, np.nan, np.nan],
			'C': [1,2,3]
			})
print(df.dropna())
print(df.fillna(value=df['A'].mean()))
