# One-Way ANOVA Analysis

This README outlines the process and calculations for performing a one-way ANOVA to test the differences in mean scores across three groups (A, B, C).

## 1. Problem Statement
We aim to determine if there are significant differences in the mean scores among three groups (A, B, and C).

## 2. Hypotheses
- **Null Hypothesis (H0):** All group means are equal (μA = μB = μC).
- **Alternative Hypothesis (H1):** At least one group mean is different.

## 3. Data
### Group Scores
| Group  | Scores                     | Mean (X̄j)  |
|--------|----------------------------|-------------|
| A      | 65, 70, 75, 72, 68, 73, 67 | 70          |
| B      | 85, 78, 80, 90, 88, 82, 87 | 84.29       |
| C      | 50, 55, 60, 58, 62, 53     | 56.33       |

### Overall Mean (X̄):
Overall Mean = (65 + 70 + 75 + ... + 53) / 20 = 67.6

## 4. ANOVA Calculations

### Total Sum of Squares (SST)
SST = Σ(Xi - X̄)² = 5945.2

### Between-Group Sum of Squares (SSB)
SSB = Σ nj (X̄j - X̄)²  
- Group A: SSB_A = 40.32  
- Group B: SSB_B = 1940.26  
- Group C: SSB_C = 761.34  
SSB = 40.32 + 1940.26 + 761.34 = 2741.92

### Within-Group Sum of Squares (SSW)
SSW = Σ Σ (Xij - X̄j)²  
- Group A: SSW_A = 64  
- Group B: SSW_B = 204.86  
- Group C: SSW_C = 198.67  
SSW = 64 + 204.86 + 198.67 = 467.53

## 5. Degrees of Freedom
- Total: DF_total = N - 1 = 19  
- Between Groups: DF_between = k - 1 = 2  
- Within Groups: DF_within = N - k = 17  

## 6. Mean Squares
- Between Groups: MSB = SSB / DF_between = 1370.96  
- Within Groups: MSW = SSW / DF_within = 27.50  

## 7. F-Statistic
F = MSB / MSW = 1370.96 / 27.50 = 49.85

## 8. P-Value
Using an F-distribution table with DF_between = 2 and DF_within = 17:  
p ≈ 4.5 × 10^(-9)

## 9. Conclusion
Since p < 0.05, we reject the null hypothesis.  
**Interpretation:** At least one group has a significantly different mean score.
