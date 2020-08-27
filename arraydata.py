import pandas as pd
import numpy as np
ar = np.array([[1,2,3],[5,4,6],[7,8,9]])
df = pd.DataFrame(ar)
df = pd.DataFrame(ar, index=['A','B','C'], columns=['One','Two','Three'])
df2 = df[['One','Two']].copy()
print(df)
print(df2)
