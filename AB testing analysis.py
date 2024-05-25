import numpy as np
from scipy import stats

# Generate sample data for A and B groups (conversion rates)
np.random.seed(0)  # for reproducibility
sample_size = 1000  # number of samples in each group

# Group A (control group) - current design
conversion_rate_a = 0.10  # conversion rate for Group A
group_a = np.random.binomial(n=1, p=conversion_rate_a, size=sample_size)

# Group B (experimental group) - new design
conversion_rate_b = 0.12  # conversion rate for Group B (slightly higher)
group_b = np.random.binomial(n=1, p=conversion_rate_b, size=sample_size)

# Perform two-sample t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b)

# Print results
print("Group A (Control): Mean Conversion Rate =", np.mean(group_a))
print("Group B (Experimental): Mean Conversion Rate =", np.mean(group_b))
print("T-statistic =", t_stat)
print("P-value =", p_value)

# Interpret results
if p_value < 0.05:
    print("The difference in conversion rates between Group A and Group B is statistically significant.")
    if np.mean(group_b) > np.mean(group_a):
        print("The new design (Group B) has a higher conversion rate than the current design (Group A).")
    else:
        print("The new design (Group B) has a lower conversion rate than the current design (Group A).")
else:
    print("The difference in conversion rates between Group A and Group B is not statistically significant.")
    print("Further testing or analysis may be required to draw conclusive insights.")