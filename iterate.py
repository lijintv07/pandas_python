import pandas as pd
df= pd.DataFrame({'age':[20,32],'state':['NY','CA'],'point':[64,92]},index =['Alice','Bob'])
print(df)
for column_name in df:
    print(type(column_name))
    print(column_name)
    print('------\n')

for column_name, item in df.iteritems():
    print(type(column_name))
    print(column_name)
    print('~~~~~~')

    print(type(item))
    print(item)
    print('------')


for index, row in df.iterrows():
    print(type(index))
    print(index)
    print('~~~~~~')

    print(type(row))
    print(row)
    print('------')


for row in df.itertuples():
    print(type(row))
    print(row)
    print('------')

    print(row[3])
    print(row.point)
    print('------\n')
