#import os
#import pandas as pd

#master_df = pd.DataFrame()

#for file in os.listdir(os.getcwd()):
    #if file.endswith('.csv'):
        #master_df = master_df.append(pd.read_csv(file))

#master_df.to_csv('Master FILE NBA.CSV', index=False)



#import pandas as pd
import glob
import os

#path = r'/Users/gabesfolder/Desktop/NBA CSV' # use your path
#all_files = glob.glob(os.path.join(path , "/*.csv"))

#li = []

#for filename in all_files:
    #df = pd.read_csv(filename, index_col=None, header=0)
    #li.append(df)

#frame = pd.concat(li, axis=0, ignore_index=True)

import os
import pandas as pd

files = []
for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        df = pd.read_csv(files)
        files.append(df)