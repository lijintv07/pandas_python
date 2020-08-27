import pandas as pd
import json
s = ' {"col1":{"row1":1,"row2":2,"row3":3},"col2":{"row1":"x","row2":"y","row3":"z"}}'
df = pd.read_json(s)
print(df)
df.to_excel('json_test.xlsx')
