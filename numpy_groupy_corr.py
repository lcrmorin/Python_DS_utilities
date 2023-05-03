from joblib import Parallel, delayed
import numpy as np
from scipy import stats

eras = ['Moon']

def process(x):
    return stats.spearmanr(x).correlation

def groupby_corr_numpy(df, eras, cols = all_features+targets):
    ids, index = np.unique(df[eras], return_index=True)
    splits = np.split(df[cols].values, index[1:])
    ret = Parallel()(delayed(process)(x) for time_id, x in zip(ids.tolist(), splits))
    ret = pd.concat([pd.DataFrame(r, index=cols,columns=cols) for r in ret], keys=ids)
    ret.index = ret.index.set_names([eras[0], 'features'])
    return ret

corrs_by_moons = groupby_corr_numpy(train, eras)
