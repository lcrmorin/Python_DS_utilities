import pandas as pd, numpy as np
from collections import defaultdict
import seaborn as sns

# base dataframe formatting
df = pd.DataFrame({'feature':[-1,0,1,12],'target':[0.0012, 0.021, 0, np.nan]})
col = df.columns

dict_format =  defaultdict(lambda: "{:.0}")
dict_format.update({'target': '{:.2%}'})

dict_color =  defaultdict(lambda: 'Blues')
dict_color.update({'feature': 'Spectral'})

dict_v =  defaultdict(lambda: (None, None))
dict_v.update({'feature': (-np.abs(df.feature).max(), np.abs(df.feature).max())})

df_style = df.style

for c in col:
    df_style = df_style.background_gradient(subset=c, cmap=dict_color[c], 
                                            vmin=dict_v[c][0], vmax=dict_v[c][1])
  
df_style.format(dict_format).applymap(lambda x: 'background: lightgrey; color: transparent' if pd.isnull(x) else '')

# base dependance plot

sns.regplot(x=df[feature], 
            y=df[target], 
            logistic = False,
            x_jitter = 0.1,
            y_jitter = 0.1,
            scatter_kws={'s':1},
            line_kws={"color": "red"}).set_title(f"{target} / {feature}");
