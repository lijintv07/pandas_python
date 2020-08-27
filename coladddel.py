import pandas as pd
data = [['Axel',32],['Alice',26],['Alex',45]]
df = pd.DataFrame(data,columns=['Name','Age'])
c = pd.DataFrame([1,2,3],columns = ['Example'])
df['Example'] = c['Example']
del df['Example']
print(df)
