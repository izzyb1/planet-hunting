# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
x,y = np.loadtxt("DATA/xy.txt",unpack=True)

# %%
for i in range(0,len(x)):
    print(x[i])

# %%
z = []
for i in range(0,len(x)):
    z.append(x[i]*y[i])
    print(z[i])

# %%
plt.plot(x,y)
plt.xlabel("String")

# %%
np.sum(x)
np.mean(x)

