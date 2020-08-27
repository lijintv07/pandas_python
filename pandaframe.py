import pandas as pd
#data = [1,2,3]
#df = pd.DataFrame(data)
#print(df)

data = [['Axel',32],['Alice',26],['Alex',45]]
df = pd.DataFrame(data,columns = ['Name','Age'])
print(df['Name'])
