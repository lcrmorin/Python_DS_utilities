import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from pandas.core.base import PandasObject

def better_describe(df, values_list=[np.inf,-np.inf]):
    
    df_describe = df.describe(include='all')
    df_describe.loc['dtype'] = df.dtypes
    df_describe.loc['unique_count'] = df.nunique()
    df_describe.loc['nan_count'] = df.isna().sum()
    
    df_describe.loc['constant_diff'] = np.nan
    for c in df.columns:
        if is_numeric_dtype(df[c]):
            diffs = np.diff(np.unique(df[c]))
            min_diffs = min(diffs)
            if all([i.is_integer() for i in (diffs/min_diffs)]):
                df_describe.loc['constant_diff',c] = min_diffs
    
    for value in values_list:
        df_describe.loc[f'{str(value)}_count'] = (df == value).sum()

    order = ['dtype','count','unique_count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max', 'constant_diff', 'nan_count'] + [f'{str(value)}_count' for value in values_list]
        
    return df_describe.loc[order]

PandasObject.better_describe = better_describe
