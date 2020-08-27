import pandas as pd
df = pd.read_csv('TechCrunchcontinentalUSA.csv')
df.to_json('data.json')
