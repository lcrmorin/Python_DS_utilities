import numpy as np, pandas as pd

Base = pd.Series([1,2,3,1,2,3,1,2])
New = pd.Series([1,2,3,1,2,3])

def PSI_indicator(Base, New, Verbose = False):
    
    Base_counts = Base.value_counts().sort_index()
    New_counts = New.value_counts().sort_index()
    
    Base_props = Base_counts/Base_counts.sum()
    New_props = New_counts/New_counts.sum()
    
    assert (Base_props.index == New_props.index).all()
    
    diff = New_props - Base_props
    var = New_props / Base_props - 1 
    log_rel = np.log(New_props / Base_props)
    PSI = diff * log_rel
    
    res = pd.DataFrame({
    'base count':Base_counts.values,
    'new count':New_counts.values,
    'base prop':Base_props.values,
    'new prop':New_props.values,
    'diff':diff.values,
    'var':var.values,
    'log_rel':log_rel.values, 
    'PSI':PSI.values
    })
    
    
    fmt = {
    'base count':'{:}',
    'new count':'{:}',
    'base prop':'{:.2%}',
    'new prop':'{:.2%}',
    'diff':'{:.2%}',
    'var':'{:.2%}',
    'log_rel':'{:.2%}', 
    'PSI':'{:.2%}'
    }
    
    if Verbose:
        display(res.style.format(fmt))
    
    return np.mean(PSI)

PSI_indicator(Base, New, Verbose = True)
