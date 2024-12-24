import pandas as pd
from scipy.stats import skew, kurtosis, f_oneway
import matplotlib.pyplot as plt
import seaborn as sns

# Data
data = {
    "Student_ID": range(1, 21),
    "Group": ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B',
              'C', 'C', 'C', 'C', 'C', 'A', 'B', 'C', 'A', 'B'],
    "Score": [65, 70, 75, 72, 68, 85, 78, 80, 90, 88,
              50, 55, 60, 58, 62, 73, 82, 53, 67, 87]
}

df = pd.DataFrame(data)

# Calculate Skewness
skewness = skew(df['Score'])
if skewness > 0:
    print("The distribution is positively skewed.")
elif skewness < 0:
    print("The distribution is negatively skewed.")
else:
    print("The distribution is symmetrical.")

# Calculate Kurtosis
kurt = kurtosis(df['Score'], fisher=False)  # Using fisher=False for traditional Kurtosis

# Stem-and-leaf function
def stem_and_leaf(scores):
    stems = {}
    for score in scores:
        stem, leaf = divmod(score, 10)
        stems.setdefault(stem, []).append(leaf)
    stem_and_leaf_result = []
    for stem, leaves in sorted(stems.items()):
        stem_and_leaf_result.append(f"{stem} | {' '.join(map(str, sorted(leaves)))}")
    return "\n".join(stem_and_leaf_result)

# Extract groups for ANOVA test
group_a = df[df['Group'] == 'A']['Score']
group_b = df[df['Group'] == 'B']['Score']
group_c = df[df['Group'] == 'C']['Score']

# Perform ANOVA test
f_stat, p_value = f_oneway(group_a, group_b, group_c)

# Display results
print("Skewness:", skewness)
print("Kurtosis:", kurt)
print("\nStem-and-Leaf Plot:\n", stem_and_leaf(df['Score']))
print("\nANOVA Test Results:")
print("F-statistic:", f_stat)
print("P-value:", p_value)

# Interpretation of p-value
if p_value < 0.05:
    print("There is a significant difference between groups.")
else:
    print("There is no significant difference between groups.")

# Plotting data
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Dot Plot in the first subplot
axes[0].scatter(df['Student_ID'], df['Score'], color='blue', label='Scores')
axes[0].set_title("Dot Plot of Scores")
axes[0].set_xlabel("Student ID")
axes[0].set_ylabel("Score")
axes[0].grid(True)
axes[0].set_xticks(df['Student_ID'])
axes[0].tick_params(axis='x', rotation=90)  # Rotate x-axis labels for better readability

# **Visual Interpretation of Skewness from Dot Plot**:
# - **Positively Skewed**: If the points cluster on the left side and there is a tail extending to the right, this indicates a positive skew.
# - **Negatively Skewed**: If the points cluster on the right side and there is a tail extending to the left, this indicates a negative skew.
# - **Symmetrical**: If the points are evenly spread around the center, the distribution is symmetrical.

# Box Plot in the second subplot
sns.boxplot(x='Group', y='Score', data=df, ax=axes[1])
axes[1].set_title("Box Plot of Scores by Group")
axes[1].grid(True)

# **Visual Interpretation of Skewness from Box Plot**:
# - **Positively Skewed**: The right side (upper whisker) will be longer than the left side, and the median will be closer to the lower quartile.
# - **Negatively Skewed**: The left side (lower whisker) will be longer than the right side, and the median will be closer to the upper quartile.
# - **Symmetrical**: The whiskers will be of approximately equal length, and the median will be near the center.

# Adjust layout for better visualization
plt.tight_layout()

# Show the plots
plt.show()
