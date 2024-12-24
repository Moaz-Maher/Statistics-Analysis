# Descriptive and Inferential Statistics

## A. Descriptive Statistics

### 1. Distribution of Data Using Skewness and Kurtosis
- **Skewness:** Measures the asymmetry of the data distribution.
  - Positive skewness: Long tail on the right (mean > median).
  - Negative skewness: Long tail on the left (mean < median).
  - Near-zero skewness: Symmetrical distribution.

- **Kurtosis:** Describes the shape of the distribution tails.
  - Positive kurtosis (leptokurtic): Sharp peak with heavy tails.
  - Negative kurtosis (platykurtic): Flat peak with light tails.
  - Zero kurtosis (mesokurtic): Normal distribution.

**Python Code Example:**
```python
from scipy.stats import skew, kurtosis

# Unified dataset
data = [85, 90, 88, 87, 89, 91, 92, 78, 82, 80, 79, 81, 83, 84, 92, 95, 91, 94, 93, 96]

# Calculate skewness
skewness = skew(data)
print(f"Skewness: {skewness}")

# Calculate kurtosis
kurt = kurtosis(data, fisher=True)  # Fisher=True gives excess kurtosis
print(f"Kurtosis: {kurt}")
```
**Interpretation:**
- If `skewness > 0`: Data is positively skewed.
- If `skewness < 0`: Data is negatively skewed.
- If `kurtosis > 0`: Data has heavy tails (leptokurtic).
- If `kurtosis < 0`: Data has light tails (platykurtic).

### 2. Knowledge of Some Plots

#### i. Dot Plot
- **Definition:** A simple graph showing each data point as a dot along a single axis.
- **Usage:** Visualizes frequency and distribution.
- **Python Code:**
```python
import matplotlib.pyplot as plt

# Unified dataset with at least 20 points
data = [85, 90, 88, 87, 89, 91, 92, 78, 82, 80, 79, 81, 83, 84, 92, 95, 91, 94, 93, 96]
plt.plot(data, [1] * len(data), 'bo')
plt.yticks([])
plt.title("Dot Plot")
plt.show()
```

#### ii. Box Plot
- **Definition:** A visual summary of the data showing minimum, maximum, median, and quartiles.
- **Usage:** Identifies outliers and compares distributions.
- **Python Code:**
```python
import matplotlib.pyplot as plt

# Unified dataset
data = [85, 90, 88, 87, 89, 91, 92, 78, 82, 80, 79, 81, 83, 84, 92, 95, 91, 94, 93, 96]
plt.boxplot(data)
plt.title("Box Plot")
plt.show()
```

#### iii. Stem-and-Leaf Plot
- **Definition:** Splits data into "stems" (leading digits) and "leaves" (trailing digits).
- **Usage:** Organizes data to retain original values.
- **Python Code:**
```python
# Unified dataset
data = [85, 90, 88, 87, 89, 91, 92, 78, 82, 80, 79, 81, 83, 84, 92, 95, 91, 94, 93, 96]
stems = {str(x // 10): [] for x in data}
for num in data:
    stem, leaf = divmod(num, 10)
    stems[str(stem)].append(str(leaf))

for stem, leaves in stems.items():
    print(f"{stem} | {''.join(leaves)}")
```

### 3. How to Define Skewness Type from Graph
- **Symmetrical Distribution:** The graph is mirrored; skewness = 0.
- **Positive Skew:** Right tail is longer; peak shifted left.
- **Negative Skew:** Left tail is longer; peak shifted right.

---

## B. Inferential Statistics

### ANOVA: Analysis of Variances

#### When to Use
- Compares means of three or more groups to determine if there is a significant difference.
- Assumes:
  1. Data is normally distributed.
  2. Variances are equal.
  3. Samples are independent.

#### How to Use It (Laws and Calculation)
1. **Set Hypotheses:**
   - Null hypothesis (H0): All group means are equal.
   - Alternative hypothesis (H1): At least one group mean is different.

2. **Calculate the F-Statistic:**
   - Between-group variance (MSB): Measures variation due to differences between group means.
   - Within-group variance (MSW): Measures variation within each group.
   - Formula: F = MSB / MSW

3. **Compare to Critical Value:**
   - Find the F-critical value based on degrees of freedom and significance level.
   - If F > F-critical, reject H0.

#### Solved Example with Steps
**Example:** Compare test scores of three classes (A, B, C).
- **Data (Unified Dataset):**
  - Class A: [85, 90, 88, 87, 89, 91, 92]
  - Class B: [78, 82, 80, 79, 81, 83, 84]
  - Class C: [92, 95, 91, 94, 93, 96, 97]

**Steps:**
1. **Calculate Group Means:**
   - A: (85 + 90 + 88 + 87 + 89 + 91 + 92) / 7 = 88.86
   - B: (78 + 82 + 80 + 79 + 81 + 83 + 84) / 7 = 81
   - C: (92 + 95 + 91 + 94 + 93 + 96 + 97) / 7 = 94

2. **Calculate Overall Mean:**
   - (85 + 90 + 88 + 87 + 89 + 91 + 92 + 78 + 82 + 80 + 79 + 81 + 83 + 84 + 92 + 95 + 91 + 94 + 93 + 96 + 97) / 21 = 87.95

3. **Calculate MSB and MSW:**
   - Between-group sum of squares (SSB): ∑n(mean_group - mean_total)^2
   - Within-group sum of squares (SSW): Sum of squares within each group.

4. **Compute F-Statistic:**
   - Use SSB, SSW, and their respective degrees of freedom.

5. **Compare F to F-Critical:**
   - If significant, conclude at least one mean is different.

---
This document provides an overview of descriptive and inferential statistics, emphasizing skewness, kurtosis, visualization methods, and ANOVA analysis.

