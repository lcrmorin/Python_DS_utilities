import pandas as pd

iter_csv = pd.read_csv('file.csv', iterator=True, chunksize=1000)
df = pd.concat([chunk[chunk['field'] > constant] for chunk in iter_csv])

with open(<file>) as f:
    text = "\n".join([line for line in f if line.split(',')[2] == "Hello"])

df = pd.read_csv(StringIO(text))
