import pandas as pd
import csv

#assign spreadsheet filename to file
file = 'ms_teams.csv'
file2 = 'ms_teams_upload.csv'

# load excel file
df = pd.read_csv(file)
df2 = pd.read_csv(file2)

frames = [df, df2]

data = pd.concat(frames)

data.drop_duplicates(subset="input", keep="first", inplace=True)

data.sort_values("output", inplace=True)

data.to_csv("ms_teams_updated.csv", index=False)
        