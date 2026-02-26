import pandas as pd
import glob

files = glob.glob("graphs/*_edges.csv")

total_ips = set()
total_ports = set()
total_edges = 0

for file in files:
    df = pd.read_csv(file)

    total_edges += len(df)
    total_ips.update(df["src"].unique())
    total_ports.update(df["dst"].unique())

    print("File:", file)
    print("Edges:", len(df))
    print("Unique IPs:", df["src"].nunique())
    print("Unique Ports:", df["dst"].nunique())
    print("Max weight:", df["weight"].max())
    print("-" * 40)

print("\n===== GLOBAL STATS =====")
print("Total edge rows:", total_edges)
print("Global unique IPs:", len(total_ips))
print("Global unique ports:", len(total_ports))
