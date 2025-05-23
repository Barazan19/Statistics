# Sample vs Population Variance

This project demonstrates why we divide by \( n - 1 \) instead of \( n \) when estimating population variance from a sample. Using Python, we simulate sampling from a known population and compare the variance calculations.

## 📂 Contents

- `README.md`: Documentation explaining the concept and results
- `variance_demo.ipynb` / `variance_demo.py`: Python simulation code
- `sample_variance_results.csv`: Results from 100 repeated samples

## 🎯 Objective

To show that:
\[
\frac{1}{n} \sum (x_i - \bar{x})^2 < \frac{1}{n} \sum (x_i - \mu)^2
\]
which explains the need for Bessel's correction:
\[
s^2 = \frac{1}{n - 1} \sum (x_i - \bar{x})^2
\]
so that the sample variance becomes an **unbiased estimator** of the population variance.

## 🧪 Experiment Details

- **Population**: Heights of 15 children from 170 cm to 184 cm (mean = 177.0, variance = 18.67)
- **Samples**: 100 random samples of size 3
- For each sample:
  - Compute sample variance using \( n \)
  - Compute sample variance using \( n - 1 \)

## 📊 Results

| Statistic                          | Value      |
|------------------------------------|------------|
| Sample variance (divided by \( n \))     | ~12.83     |
| Sample variance (divided by \( n - 1 \)) | ~19.25     |
| Population variance                | 18.67      |

### ✅ Conclusion:
- Dividing by \( n \) consistently **underestimates** the population variance.
- Dividing by \( n - 1 \) corrects the bias and provides an accurate estimate.

## 🧠 Key Takeaway

This concept is fundamental in statistics and critical in real-world modeling, including machine learning, where understanding and correctly estimating variance is crucial.

Feel free to reuse or modify this project for your own statistical learning or teaching materials!
