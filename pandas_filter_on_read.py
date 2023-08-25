import pandas as pd

iter_csv = pd.read_csv('file.csv', iterator=True, chunksize=1000)
df = pd.concat([chunk[chunk['field'] > constant] for chunk in iter_csv])
