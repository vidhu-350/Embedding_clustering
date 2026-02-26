import pandas as pd
import glob
import os
import matplotlib.pyplot as plt

# Load weekly edge files
weekly_files = sorted(glob.glob("graphs/weekly_*_edges.csv"))

weeks = []
edge_counts = []
unique_ips = []
unique_ports = []
max_weights = []

for file in weekly_files:
    df = pd.read_csv(file)
    
    week_name = os.path.basename(file).replace("_edges.csv","")
    
    weeks.append(week_name)
    edge_counts.append(len(df))
    unique_ips.append(df["src"].nunique())
    unique_ports.append(df["dst"].nunique())
    max_weights.append(df["weight"].max())

stats_df = pd.DataFrame({
    "Week": weeks,
    "Edges": edge_counts,
    "Unique_IPs": unique_ips,
    "Unique_Ports": unique_ports,
    "Max_Weight": max_weights
})

stats_df = stats_df.sort_values("Week")

# ------------------------------
# 1. Weekly Edge Volume
# ------------------------------
plt.figure(figsize=(12,6))
plt.plot(stats_df["Week"], stats_df["Edges"], linewidth=2)
plt.xticks(rotation=90)
plt.title("Weekly Edge Volume (Attack Activity)")
plt.ylabel("Number of IP→PORT Edges")
plt.xlabel("Week")
plt.tight_layout()
plt.savefig("weekly_edge_volume.png", dpi=300)
plt.close()

# ------------------------------
# 2. Weekly Unique IP Count
# ------------------------------
plt.figure(figsize=(12,6))
plt.plot(stats_df["Week"], stats_df["Unique_IPs"], linewidth=2)
plt.xticks(rotation=90)
plt.title("Weekly Unique Attacker IP Count")
plt.ylabel("Unique IPs")
plt.xlabel("Week")
plt.tight_layout()
plt.savefig("weekly_unique_ips.png", dpi=300)
plt.close()

# ------------------------------
# 3. Weekly Unique Port Diversity
# ------------------------------
plt.figure(figsize=(12,6))
plt.plot(stats_df["Week"], stats_df["Unique_Ports"], linewidth=2)
plt.xticks(rotation=90)
plt.title("Weekly Target Port Diversity")
plt.ylabel("Unique Ports")
plt.xlabel("Week")
plt.tight_layout()
plt.savefig("weekly_unique_ports.png", dpi=300)
plt.close()

# ------------------------------
# 4. Weekly Maximum Edge Weight
# ------------------------------
plt.figure(figsize=(12,6))
plt.plot(stats_df["Week"], stats_df["Max_Weight"], linewidth=2)
plt.yscale('log')
plt.xticks(rotation=90)
plt.title("Weekly Maximum Edge Weight (Scanner Intensity)")
plt.ylabel("Max Weight (log scale)")
plt.xlabel("Week")
plt.tight_layout()
plt.savefig("weekly_max_weight.png", dpi=300)
plt.close()

print("Saved 4 separate figures:")
print(" - weekly_edge_volume.png")
print(" - weekly_unique_ips.png")
print(" - weekly_unique_ports.png")
print(" - weekly_max_weight.png")
