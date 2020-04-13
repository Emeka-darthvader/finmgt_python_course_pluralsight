import pandas as pd
from pandas import ExcelWriter
import pandas.api.types as ptypes

data = pd.ExcelFile('data/Forecast Anglo.xlsx')
df = data.parse(sheet_name='Sheet1')
#print(df)

#Select from rows #1 - #12 and from columns #1 to end
ndf = df.iloc[1:12,1:]
#print(ndf.values)

#next up is cleaning data, removing those with string, changing commas to
# decimal pints and then those with percentage sign to their equivalent values

#cleanup
nvalues = []

for row in ndf.values:
    nrow = []
    for itm in row:
        if type(itm) == str:
            itm = itm.replace(' ','').replace(',','.')
            if len(itm) == 1 and '-' in itm:
                itm = itm.replace('-','0')
            if '%' in itm:
                itm = float(itm.replace('%',''))/100
            itm = float(itm)
        nrow.append(itm)
    nvalues.append(nrow)   
#print(nvalues)

#save new values to excel file
df.iloc[1:12,1:] = nvalues
writer = ExcelWriter('data/Forecast Anglo 2.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()


