import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -------------------------------
# Set random seed for reproducibility
# -------------------------------
np.random.seed(42)

# -------------------------------
# Seaborn style and context
# -------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# -------------------------------
# Generate synthetic customer engagement data (your original block)
# -------------------------------
n_samples = 300
data = pd.DataFrame({
    "email_open_rate": np.clip(np.random.normal(0.5, 0.1, n_samples), 0, 1),
    "click_through_rate": np.clip(np.random.normal(0.2, 0.05, n_samples), 0, 1),
    "time_on_site": np.random.normal(120, 30, n_samples),  # in seconds
    "pages_per_visit": np.random.normal(5, 1.5, n_samples),
    "bounce_rate": np.clip(np.random.normal(0.4, 0.1, n_samples), 0, 1),
    "conversion_rate": np.clip(np.random.normal(0.05, 0.02, n_samples), 0, 1),
})

# -------------------------------
# Compute correlation matrix (heatmap example)
# -------------------------------
corr = data.corr()

plt.figure(figsize=(8, 8))  # 512x512 at dpi=64
heatmap = sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.8}
)
plt.title("Customer Engagement Correlation Matrix", fontsize=16)
plt.savefig("heatmap.png", dpi=64, bbox_inches="tight")
plt.close()

# -------------------------------
# Generate synthetic seasonal revenue data for lineplot
# -------------------------------
months = pd.date_range("2024-01-01", periods=12, freq="M").strftime("%b")
base_revenue = np.linspace(20000, 35000, 12)
seasonality = 3000 * np.sin(np.linspace(0, 2 * np.pi, 12))
noise = np.random.normal(0, 1000, 12)
revenue = base_revenue + seasonality + noise

df_revenue = pd.DataFrame({"Month": months, "Revenue": revenue})

# -------------------------------
# Create lineplot
# -------------------------------
plt.figure(figsize=(8, 8))  # 512x512 at dpi=64
sns.lineplot(
    data=df_revenue,
    x="Month",
    y="Revenue",
    marker="o",
    linewidth=2.5,
    color="steelblue"
)

plt.title("Monthly Revenue Trends (Synthetic Data)", fontsize=16, weight="bold")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue (USD)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Save figure with required dimensions
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
