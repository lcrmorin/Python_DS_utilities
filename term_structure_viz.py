# Dataviz
import seaborn as sns
import matplotlib.pyplot as plt

def viz_targets(data, sample=0.01):
    sns.pairplot(data.dropna().sample(frac=sample),
                 kind='reg',
                 plot_kws={'x_jitter':0.02, 
                           'y_jitter':0.02, 
                           'line_kws':{"color": "red"}, 
                           'scatter_kws':{"s": 1}},
                 diag_kind='kde'
                );
    plt.show();
    
viz_targets(all_data[targets])
