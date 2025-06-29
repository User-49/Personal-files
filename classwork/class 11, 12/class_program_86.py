'''import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [2,3,4,5]
plt.plot(x , 'm:' , label='class10')
plt.plot(y , 'g-' , label='class11')
plt.legend()
plt.show()
'''
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 5, 0.1)
y = np.sin(x)
print('x :',x,'\ny :',y)
fig, ax = plt.subplots()
ax.plot(x, y)
