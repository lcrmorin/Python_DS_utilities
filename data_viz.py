import seaborn as sns

# base dependance plot

sns.regplot(x=df[feature], 
            y=df[target], 
            logistic = False,
            x_jitter = 0.1,
            y_jitter = 0.1,
            scatter_kws={'s':1},
            line_kws={"color": "red"}).set_title(f"{target} / {feature}");
