import os
import pandas as pd

dirHome = "./data_v2"
os.chdir(dirHome)

csvList = os.listdir()

colNames = {
            "era20c_1930_99thPercTrends" : 'e99_1930',
            "era20c_1950_99thPercTrends" : 'e99_1950',
            "twcr_1930_99thPercTrends" : 't99_1930',
            "twcr_1950_99thPercTrends" : 't99_1950'
            }

isFirst = True

for csv in csvList:
    print(csv)

    cname = colNames[csv.split('_reg_95CI_modifiedMK_HAC.csv')[0]]

    dat = pd.read_csv(csv)

    dat = dat[dat['regSig']]

    if isFirst:
        dat = dat[['tg', 'lon', 'lat', 'trend_mm_year_reg']]
        dat.columns = ['tg', 'lon', 'lat', cname]
        df = dat.copy()
        isFirst = False
    else:
        dat = dat[['tg', 'lon', 'lat', 'trend_mm_year_reg']]
        dat.columns = ['tg', 'lon', 'lat', cname]

        df = pd.merge(df, dat, on='tg', how='outer')

    print(df)

# remove csv extension
removeExt = lambda x: x.split(".csv")[0]
df['tg'] = pd.DataFrame(list(map(removeExt, df['tg'])))
print(df)

os.chdir("/")
print(os.getcwd())
df.to_csv("allTrends_v2.csv")

