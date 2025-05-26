
# 02 - Statistical Power Calculation

import numpy as np
from statsmodels.stats.power import TTestIndPower

# Simulated data
np.random.seed(1)
placebo = np.random.normal(loc=8, scale=2, size=20)
drug = np.random.normal(loc=6, scale=2, size=20)

# Calculate effect size
pooled_std = np.std(np.concatenate([placebo, drug]))
effect_size = (np.mean(placebo) - np.mean(drug)) / pooled_std

# Power analysis
analysis = TTestIndPower()
power = analysis.solve_power(effect_size=effect_size, nobs1=20, alpha=0.05)

print(f"Effect size: {effect_size:.3f}")
print(f"Statistical Power: {power:.3f}")
