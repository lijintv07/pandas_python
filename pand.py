import pandas as pd
#url = 'https://www.cethalassery.ac.in/index.php/placements/statistics#2017-18'
url = 'https://en.wikipedia.org/wiki/2019_in_film'
df = pd.read_html(url)
#dfs = pd.DataFrame(df)
print(len(df))
print("DF :",len(df))

#print(df[5]['Department'])
#dfs.to_excel('placements.xlsx')
