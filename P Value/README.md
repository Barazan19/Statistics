
# 🧪 Flu Drug Statistical Analysis

This repository walks through a complete statistical analysis pipeline for testing a new flu drug, using a StatQuest-inspired narrative.

## Sections

1. **P-Value Test** – Determine if the new drug significantly reduces viral count.
2. **Statistical Power** – Understand the strength of the test in detecting a real effect.
3. **Power Analysis** – Calculate the required sample size to design a powerful experiment.
4. **FDR Correction** – Control false discoveries when testing the drug against multiple viruses.

Each section is supported by Python code and practical simulation.

---
# P-Value and Hypothesis Testing

This folder explores the concept of **p-values** in the context of hypothesis testing, a foundational element in statistical inference and widely used in data science, machine learning, and research.

---

## 📌 What You'll Learn

- The definition of a p-value
- How p-values are used in hypothesis testing
- The difference between null and alternative hypotheses
- How to interpret p-values
- Python code examples to calculate and visualize p-values

---

## 🧠 Summary

- **P-value** is the probability of observing data as extreme as what was actually observed, under the assumption that the null hypothesis is true.
- A small p-value (typically ≤ 0.05) indicates strong evidence **against** the null hypothesis.
- A large p-value suggests **weak evidence** against the null, meaning we fail to reject it.
- P-values **do not** tell us the probability that the null hypothesis is true.

---

## 🔬 Hypothesis Testing Steps

1. **Formulate Hypotheses:**
   - Null hypothesis ($H_0$): usually states there is no effect or difference.
   - Alternative hypothesis ($H_1$): what we want to prove.

2. **Choose Significance Level (α):**
   - Common choices are 0.05, 0.01, or 0.10.

3. **Compute the Test Statistic & P-value:**
   - Use statistical tests like t-test, z-test, etc.

4. **Make Decision:**
   - If p-value < α, reject $H_0$.
   - If p-value ≥ α, fail to reject $H_0$.

---

## 📊 Notebook Contents

The included Jupyter notebook demonstrates:
- Basic simulation of null hypothesis scenarios
- Visual intuition behind p-values
- How to calculate p-values using `scipy.stats`
- Practical interpretation with annotated plots

---

## 💻 Requirements

To run the notebook, install the following Python packages:

```bash
pip install numpy pandas matplotlib scipy seaborn


Created by @barazan19
