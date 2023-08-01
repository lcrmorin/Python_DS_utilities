import pandas as pd, numpy as np
from joblib import Parallel, delayed
from scipy import stats

def pearson_corr(x):
    return np.corrcoef(x.T)

def spearman_corr(x):
    return np.corrcoef(stats.rankdata(x,axis=0).T)

def np_rank_data(l):
    a = np.array(l)
    temp = a.argsort()
    r = np.empty_like(temp)
    r[temp] = np.arange(len(a))
    return r

def groupby_corr_numpy(df, eras, cols, func):
    ids, index = np.unique(df[eras], return_index=True)
    splits = np.split(df[cols].values, index[1:])
    ret = Parallel()(delayed(func)(x) for time_id, x in zip(ids.tolist(), splits))
    ret = pd.concat([pd.DataFrame(r, index=cols, columns=cols) for r in ret], keys=ids)
    ret.index = ret.index.set_names([eras[0], 'features'])
    return ret


if __name__ == "__main__":

    #test if same result
    df1 = pd.DataFrame({'a':[1,1,1,4],'b':[5,6,7,8],'c':[12,1,2,4] , 'g':['1','1','1','1']})
    df2 = pd.DataFrame({'a':[1,1,1,0],'b':[5,6,-1,9],'c':[12,1,2,5] , 'g':['2','2','2','2']})
    df_all = pd.concat([df1,df2],axis=0)

    display(df_all)

    # pd corr v.s. custom spearman
    res1 = np.isclose(df1.corr('spearman').values, spearman_corr(df1.select_dtypes(include=np.number).values)).all()

    # np rank data v.s. custom spearman
    res2 = (np.apply_along_axis(np_rank_data, 0, df.values) == stats.rankdata(df.values,axis=0)-1).all()

    # check is yhe numpy groupby works
    res3 = np.isclose(df_all.groupby('g').corr('spearman').values, groupby_corr_numpy(df_all, 'g', ['a','b','c'], spearman_corr).values).all()

    print(f'custom spearman == pd corr: {res1}\ncustom spearman == np rank spearman: {res2}\npd groupby corr == np/scp groupby corr: {res3}')
