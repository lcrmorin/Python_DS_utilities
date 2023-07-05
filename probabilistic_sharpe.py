import numpy as np, pandas as pd
from scipy import stats as scipy_stats

# source: https://github.com/rubenbriones/Probabilistic-Sharpe-Ratio

def probabilistic_sharpe_ratio(returns=None, sr_benchmark=0.0, *, sr=None, sr_std=None):
  n = len(returns)
  skew = pd.Series(scipy_stats.skew(returns), index=returns.columns)
  kurtosis = pd.Series(scipy_stats.kurtosis(returns, fisher=False), index=returns.columns)
  sr = returns.mean() / returns.std(ddof=1)
  sr_std = np.sqrt((1 + (0.5 * sr ** 2) - (skew * sr) + (((kurtosis - 3) / 4) * sr ** 2)) / (n - 1))
  psr = scipy_stats.norm.cdf((sr - sr_benchmark) / sr_std)
  return psr

def min_track_record_length(returns=None, sr_benchmark=0.0, prob=0.95, *, n=None, sr=None, sr_std=None):
  n = len(returns)
  skew = pd.Series(scipy_stats.skew(returns), index=returns.columns)
  kurtosis = pd.Series(scipy_stats.kurtosis(returns, fisher=False), index=returns.columns)
  sr = returns.mean() / returns.std(ddof=1)
  sr_std = np.sqrt((1 + (0.5 * sr ** 2) - (skew * sr) + (((kurtosis - 3) / 4) * sr ** 2)) / (n - 1))
  min_trl = 1 + (sr_std ** 2 * (n - 1)) * (scipy_stats.norm.ppf(prob) / (sr - sr_benchmark)) ** 2
  return min_trl
