import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest

np.random.seed(42)

users = 1000

control_click = np.random.binomial(1, 0.22, users//2)
test_click = np.random.binomial(1, 0.28, users//2)

data = pd.DataFrame({
    "group": ["control"]*(users//2) + ["test"]*(users//2),
    "click": np.concatenate([control_click, test_click])
})

ctr = data.groupby("group")["click"].mean()

print("\nClick Through Rate:")
print(ctr)

# Statistical significance test
counts = data.groupby("group")["click"].sum()
nobs = data.groupby("group")["click"].count()

stat, pval = proportions_ztest(counts, nobs)

print("\nZ-test statistic:", stat)
print("P-value:", pval)

# Visualization
ctr.plot(kind="bar")
plt.title("Playlist Click Through Rate Comparison")
plt.ylabel("CTR")
plt.xticks(rotation=0)

plt.savefig("ctr_chart.png")
plt.show()