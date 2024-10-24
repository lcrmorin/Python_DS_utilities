import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_folds(folds, FOLDS_PATH, eras):

    Sizes = {
        "Removed": np.array([folds[f][0] for f in folds]),
        "Train": np.array([folds[f][1] - folds[f][0] for f in folds]),
        "Val": np.array([folds[f][3] - folds[f][2] for f in folds]),
        "Test": np.array([1 for f in folds]),
    }

    Sizes = pd.DataFrame(Sizes)[::-1]
    Sizes.plot.barh(
        stacked=True,
        title="Moons per fold",
        xlabel=eras,
        ylabel="Folds",
        color={"Removed": "grey", "Train": "blue", "Val": "green", "Test": "red"},
    )

    plt.savefig(FOLDS_PATH + f"folds_design.png")
