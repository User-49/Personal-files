import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(5,4), index=['a', 'b', 'c', 'd', 'e'], columns=['w', 'x', 'y', 'z'])
df['states'] = ['CO', 'IN', 'fr', 'gg', 'LD']

print(df)
