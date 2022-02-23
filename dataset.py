from string import ascii_uppercase
import numpy as np
import pandas as pd

np.random.seed(444)
letters1 = np.random.choice(list(ascii_uppercase), size=1000000, replace=True)
letters2 = np.random.choice(list(ascii_uppercase), size=1000000, replace=True)

df1 = pd.DataFrame(letters1.reshape(100000, 10)).rename(columns=lambda x: 'col' + str(x))
df2 = pd.DataFrame(letters2.reshape(100000, 10)).rename(columns=lambda x: 'col' + str(x))
