import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from pandas.core.base import PandasObject

def better_describe(df, values_list=[np.inf,-np.inf], prop=True):
    
    df_describe = df.describe(include='all')
    df_describe.loc['dtype'] = df.dtypes
    
    if prop:
        df_describe.loc['unique'] = np.round(df.nunique()/len(df),3)
        df_describe.loc['nan'] = np.round(df.isna().sum()/len(df),3)
    else:
        df_describe.loc['unique'] = df.nunique()
        df_describe.loc['nan'] = df.isna().sum()
    
    df_describe.loc['constant_diff'] = np.nan
    for c in df.columns:
        if is_numeric_dtype(df[c]):
            diffs = np.diff(np.unique(df[c]))
            min_diffs = min(diffs)
            if all([i.is_integer() for i in (diffs/min_diffs)]):
                df_describe.loc['constant_diff',c] = min_diffs
    
    for value in values_list:
        if prop:
            df_describe.loc[f'{str(value)}'] = np.round((df == value).sum()/len(df),3)
        else:
            df_describe.loc[f'{str(value)}'] = (df == value).sum()
        
    order = ['dtype','count','unique', 'mean', 'std', 'min', '25%', '50%', '75%', 'max', 'constant_diff', 'nan'] + [f'{str(value)}' for value in values_list]
        
    return df_describe.loc[order]

PandasObject.better_describe = better_describe
