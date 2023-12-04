import pandas as pd
import csv

dfs  = []

dfs.append(pd.read_csv(2022-2023_rg.csv))

# Concatenate all data into one DataFrame
big_frame = pd.concat(dfs, ignore_index=True)