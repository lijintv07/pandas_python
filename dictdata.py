import pandas as pd
d = {'one':[1,2,3],'two':[2,3,4],'three':[3,4,5]}
df = pd.DataFrame(d)
df = pd.DataFrame(d, index=['first','second','third'])
print(df)
