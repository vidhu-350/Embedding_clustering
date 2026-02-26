import pandas as pd
from collections import defaultdict
import glob
from pathlib import Path

OUTPUT_FILE = "graphs/global_edges.csv"

edge_weights = defaultdict(int)

files = glob.glob("graphs/weekly_*_edges.csv")

print("Processing", len(files), "weekly edge files")

for file in files:
    print("Reading:", file)
    df = pd.read_csv(file)

    for src, dst, weight in zip(df["src"], df["dst"], df["weight"]):
        edge_weights[(src, dst)] += weight

print("Aggregating complete")

edges = [(src, dst, weight) for (src, dst), weight in edge_weights.items()]

pd.DataFrame(edges, columns=["src", "dst", "weight"]).to_csv(OUTPUT_FILE, index=False)

print("Saved global graph to:", OUTPUT_FILE)
