
# 04 - FDR Correction for Multiple Virus Tests

import numpy as np
from statsmodels.stats.multitest import multipletests

# Simulate multiple p-values
np.random.seed(0)
p_values = np.random.rand(10) * 0.1  # 10 small p-values

# Apply Benjamini-Hochberg correction
rejected, pvals_corrected, _, _ = multipletests(p_values, alpha=0.05, method='fdr_bh')

print("Original p-values:", p_values)
print("FDR-corrected p-values:", pvals_corrected)
print("Reject null hypothesis:", rejected)
