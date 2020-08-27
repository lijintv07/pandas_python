import pandas as pd
data = [['Axel',32],['Alice',26],['Alex',45]]
df = pd.DataFrame(data,columns=['Name','Age'])
user = pd.DataFrame([['Vivian',33]],columns=['Name','Age'])
df = df.append(user)
df=df.drop(0)
print(df)
