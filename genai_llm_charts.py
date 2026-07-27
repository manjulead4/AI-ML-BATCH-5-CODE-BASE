"""
GenAI LLM Usage Dataset - Matplotlib Charts
Bar chart, Line chart, Scatter plot, Histogram
"""

import pandas as pd
import matplotlib.pyplot as plt


# Load dataset

CSV_PATH = "/Users/manjunathareddy/Downloads/genai_llm_usage_dataset_1000 2.csv"
df = pd.read_csv(CSV_PATH)

print(df.shape)
print(df.head())
print(df.columns.tolist())

# 1. BAR CHART - Average estimated cost per model

avg_cost_by_model = df.groupby("model_name")["estimated_cost_usd"].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(avg_cost_by_model.index, avg_cost_by_model.values, color="steelblue")
plt.title("Average Estimated Cost (USD) per Model")
plt.xlabel("Model Name")
plt.ylabel("Avg Estimated Cost (USD)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("bar_chart_avg_cost_by_model.png", dpi=150)
plt.show()


# 2. LINE CHART - Average latency vs prompt length (binned)

df["prompt_length_bin"] = pd.cut(df["prompt_length"], bins=20)
latency_by_bin = df.groupby("prompt_length_bin", observed=True)["latency_sec"].mean()
bin_centers = [interval.mid for interval in latency_by_bin.index]

plt.figure(figsize=(10, 6))
plt.plot(bin_centers, latency_by_bin.values, marker="o", color="darkorange")
plt.title("Average Latency vs Prompt Length")
plt.xlabel("Prompt Length (binned midpoint)")
plt.ylabel("Average Latency (sec)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("line_chart_latency_vs_prompt_length.png", dpi=150)
plt.show()


# 3. SCATTER PLOT - Prompt length vs total tokens

plt.figure(figsize=(10, 6))
plt.scatter(
    df["prompt_length"],
    df["total_tokens"],
    c=df["hallucination_flag"],
    cmap="coolwarm",
    alpha=0.6,
    s=20,
)
plt.title("Prompt Length vs Total Tokens (colored by hallucination flag)")
plt.xlabel("Prompt Length")
plt.ylabel("Total Tokens")
plt.colorbar(label="Hallucination Flag (0/1)")
plt.tight_layout()
plt.savefig("scatter_prompt_length_vs_tokens.png", dpi=150)
plt.show()


# 4. HISTOGRAM - Distribution of latency

plt.figure(figsize=(10, 6))
plt.hist(df["latency_sec"], bins=30, color="mediumseagreen", edgecolor="black")
plt.title("Distribution of Latency (sec)")
plt.xlabel("Latency (sec)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram_latency_distribution.png", dpi=150)
plt.show()

print("\nAll charts generated and saved as PNG files in the current directory.")
