import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -------------------------------
# Generate synthetic seasonal revenue data
# -------------------------------
np.random.seed(42)

months = pd.date_range("2024-01-01", periods=12, freq="M").strftime("%b")
base_revenue = np.linspace(20000, 35000, 12)  # gradual upward trend
seasonality = 3000 * np.sin(np.linspace(0, 2 * np.pi, 12))  # seasonal effect
noise = np.random.normal(0, 1000, 12)  # random business fluctuations

revenue = base_revenue + seasonality + noise
df = pd.DataFrame({"Month": months, "Revenue": revenue})

# -------------------------------
# Seaborn Visualization
# -------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")  # presentation-ready font sizes

plt.figure(figsize=(6, 6))  # 512x512 pixels at dpi=64

ax = sns.lineplot(
    data=df,
    x="Month",
    y="Revenue",
    marker="o",
    linewidth=2.5,
    palette="deep",
    color="steelblue"
)

# Titles and labels
plt.title("Monthly Revenue Trends (Synthetic Data)", fontsize=16, weight="bold")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue (USD)", fontsize=12)

# Rotate x-axis labels for readability
plt.xticks(rotation=45)

# Tight layout for better spacing
plt.tight_layout()

# -------------------------------
# Save output
# -------------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")  # 8 in * 64 dpi = 512 px
plt.close()
