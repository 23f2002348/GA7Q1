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
noise = np.random.normal(0, 1000, 12)  # random fluctuations

revenue = base_revenue + seasonality + noise
df = pd.DataFrame({"Month": months, "Revenue": revenue})

# -------------------------------
# Seaborn Visualization
# -------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# To guarantee 512x512 px → (figsize * dpi) must equal 512
# Example: figsize=(5.12, 5.12), dpi=100 → 512 px
plt.figure(figsize=(5.12, 5.12), dpi=100)

ax = sns.lineplot(
    data=df,
    x="Month",
    y="Revenue",
    marker="o",
    linewidth=2.5,
    color="steelblue"
)

# Titles and labels
plt.title("Monthly Revenue Trends (Synthetic Data)", fontsize=16, weight="bold")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue (USD)", fontsize=12)
plt.xticks(rotation=45)

plt.tight_layout()

# -------------------------------
# Save output (exact 512x512 px)
# -------------------------------
plt.savefig("chart.png", dpi=100, bbox_inches="tight", pad_inches=0.1)
plt.close()
