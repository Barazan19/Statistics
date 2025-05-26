
# 01 - P-Value Test for Flu Drug Effectiveness

import numpy as np
from scipy.stats import ttest_ind

# Simulate viral count (in 1000s)
np.random.seed(1)
placebo = np.random.normal(loc=8, scale=2, size=20)
drug = np.random.normal(loc=6, scale=2, size=20)

# Perform independent t-test
t_stat, p_val = ttest_ind(drug, placebo)

print(f"T-statistic: {t_stat:.3f}")
print(f"P-value: {p_val:.4f}")

alpha = 0.05
if p_val < alpha:
    print("✅ Statistically significant result: Reject H0")
else:
    print("❌ Not statistically significant: Fail to reject H0")
