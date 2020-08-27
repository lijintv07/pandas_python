import pandas as pd
import json
#df = pd.DataFrame([1,2,3])
#df.to_json('example.json')
data = [['Axel',32], ['Alice', 26], ['Alex', 45]]
df = pd.DataFrame(data,columns=['Name','Age'])
df.to_json('example.json')
