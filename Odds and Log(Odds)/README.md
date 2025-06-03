
# Odds, Log-Odds, and Odds Ratio

This notebook serves as a conceptual and practical bridge from Linear Regression to Logistic Regression by introducing the idea of **odds**, **log-odds**, and **odds ratio**.

## 📘 Concepts Covered

### 🧠 What are Odds?

Odds represent the ratio of the probability that an event occurs to the probability that it does not.

If the probability (P) of an event is 0.2, then:

**Odds = P / (1 - P) = 0.2 / 0.8 = 0.25**

That means: for every 1 time it rains, there are 4 times it doesn't.

### 🔁 Probability vs Odds

| Concept      | Formula             | Range     |
|--------------|---------------------|-----------|
| Probability  | P                   | 0 to 1    |
| Odds         | P / (1 - P)         | 0 to ∞    |

- **Probability** tells you how likely something is to happen.
- **Odds** tell you how much more likely something is to happen than not.

### 🧮 Why Log(Odds)?

Taking the logarithm of the odds (log-odds or logit) transforms the range from (0 to ∞) to (-∞ to ∞), which is important for regression:

**Log-Odds = log(P / (1 - P))**

This lets us use linear models to predict classification outcomes in logistic regression.

### ⚖️ Odds Ratio

The odds ratio compares the odds of two events:

**Odds Ratio = Odds_1 / Odds_2**

- An odds ratio of 1 means both events are equally likely.
- An odds ratio > 1 means event 1 is more likely.
- An odds ratio < 1 means event 2 is more likely.
