
# 03 - Power Analysis: Required Sample Size

from statsmodels.stats.power import TTestIndPower

analysis = TTestIndPower()
sample_size = analysis.solve_power(effect_size=0.8, alpha=0.05, power=0.8, alternative='two-sided')

print(f"Required sample size per group for 80% power: {sample_size:.2f}")
