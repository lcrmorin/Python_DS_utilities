import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from pandas.core.base import PandasObject

data_int = pd.read_csv('/kaggle/input/icr-integer-data/train_integerized.csv')

def better_describe(df):
    
    df_describe = df.describe()
    df_describe.loc['dtype'] = data_int.dtypes
    df_describe.loc['unique_count'] = df.nunique()
    df_describe.loc['nan_count'] = df.isna().sum()
    
    df_describe.loc['constant_diff'] = np.nan
    for c in df.columns:
        if is_numeric_dtype(df[c]):
            diffs = np.diff(np.unique(df[c]))
            min_diffs = min(diffs)
            if all([i.is_integer() for i in (diffs/min_diffs)]):
                df_describe.loc['constant_diff',c] = min_diffs
    
    for value in [np.inf,-np.inf]:
        df_describe.loc[f'{str(value)}_count'] = (data_int == value).sum()

    order = ['dtype','count','unique_count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max', 'constant_diff', 'nan_count', 'inf_count','-inf_count']
        
    return df_describe.loc[order]

PandasObject.better_describe = better_describe

data_int.better_describe()
