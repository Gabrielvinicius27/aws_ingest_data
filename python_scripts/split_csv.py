import pandas as pd
source_path = "./data/Airbnb_Open_Data.csv"
for i,chunk in enumerate(pd.read_csv(source_path, chunksize=300, low_memory=False)):
    chunk.to_csv('./data/chunks/chunk{}.csv'.format(i), index=False)
