import pandas as pd
import openpyxl
df = pd.DataFrame([[11,21,31],[12,22,32],[31,32,33]], index = ['one','two','three'], columns= ['a','b','c'])
print(df)
#df.to_excel('pandas_excel_trial.xlsx',sheet_name='trial_1') #with header and index
#df.to_excel('pandas_excel_trial.xlsx',sheet_name='trial_1',index=False, header=False) #removes header and index

with pd.ExcelWriter('pandas_trial_1.xlsx') as writer :
    df.to_excel(writer,sheet_name='sheet1')
    df.to_excel(writer,sheet_name='sheet2')
