from joblib import Parallel, delayed
import numpy as np
from scipy import stats

def process_pearson(x):
    return np.corrcoef(x.T)

def process_spearman(x):
    return np.corrcoef(stats.rankdata(x,axis=0).T)

def groupby_corr_numpy(df, eras, cols, func):
    ids, index = np.unique(df[eras], return_index=True)
    splits = np.split(df[cols].values, index[1:])
    ret = Parallel()(delayed(func)(x) for time_id, x in zip(ids.tolist(), splits))
    ret = pd.concat([pd.DataFrame(r, index=cols, columns=cols) for r in ret], keys=ids)
    ret.index = ret.index.set_names([eras[0], 'features'])
    return ret

all_data = pd.concat([train_data, train_targets[targets]], axis=1)
corrs_by_moons = groupby_corr_numpy(all_data, eras, features+targets, process_spearman_np)
