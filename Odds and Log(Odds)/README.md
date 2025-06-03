
# Odds, Log-Odds, and Odds Ratio

This notebook serves as a conceptual and practical bridge from Linear Regression to Logistic Regression by introducing the idea of **odds**, **log-odds**, and **odds ratio**.

## 📘 Concepts Covered

### What are Odds?

Odds represent the ratio of the probability that an event occurs to the probability that it does not.

\[
\text{Odds} = \frac{P(​\text{event})}{1 - P(​\text{event})}
\]

For example, if the probability of an event is 0.2, the odds would be:

\[
\frac{0.2}{1 - 0.2} = \frac{0.2}{0.8} = 0.25
\]

### Probability vs Odds

| Concept      | Formula                      | Range     |
|--------------|------------------------------|-----------|
| Probability  | \( P = \frac{A}{A + B} \) | 0 to 1    |
| Odds         | \( O = \frac{A}{B} \)     | 0 to ∞    |

- Probability tells you how likely something is to happen.
- Odds tell you how much more likely something is to happen than not.

### Why Log(Odds)?

Taking the logarithm of the odds (log-odds or logit) transforms the range from \(0 \to ∞\) to \(-∞ \to ∞\), which is important for regression:

\[
\text{Log-Odds} = \log\left(\frac{P}{1 - P}\right)
\]

This is crucial in Logistic Regression because it allows us to use a linear model to predict the log-odds of the event occurring.

### Odds Ratio

The odds ratio compares the odds of two events:

\[
\text{Odds Ratio} = \frac{\text{Odds}_1}{\text{Odds}_2}
\]

An odds ratio of 1 means both events are equally likely.

---

Check the notebook for Python implementation examples.
