import pandas as pd
import numpy as np
import seaborn as sns

df = pd.DataFrame({'feature':[-1,0,1,12], 'target':[0.0012, 0.021, 0, np.nan]})
col = df.columns

# base fomatting

dict_format =  {'feature': '{}',
           'target': '{0:.2%}'}

dict_color =  {'feature': 'Spectral',
           'target': 'Blues'}

dict_v = {'feature': (-np.abs(df.value1).max(), np.abs(df.value1).max()),
          'target': (None, None)
    }

df_style = df.style

for c in col:
    df_style = df_style.background_gradient(subset=c, cmap=dict_color[c], 
                                            vmin=dict_v[c][0], vmax=dict_v[c][1]).format({c: dict_format[c]})

df_style.applymap(lambda x: 'background: lightgrey' if pd.isnull(x) else '').applymap(lambda x: 'color: transparent' if pd.isnull(x) else '')

# base dependance plot

sns.regplot(x=df[feature], 
            y=df[target], 
            logistic = False,
            x_jitter = 0.1,
            y_jitter = 0.1,
            scatter_kws={'s':1},
            line_kws={"color": "red"}).set_title(f"{target} / {feature}");
