import numpy as np
import pandas as pd


l = [print, sum, len]
l = pd.Series(l)

print(l[0]("hellp"))
print(l[1]((1,2,3)))
