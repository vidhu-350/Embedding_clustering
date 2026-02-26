import pandas as pd
import pickle
from pathlib import Path

EDGE_FILE = "graphs/global_edges.csv"
OUTPUT_DIR = Path("features")
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(EDGE_FILE)

nodes = set(df["src"]).union(set(df["dst"]))

node_index = {node: idx for idx, node in enumerate(sorted(nodes))}

with open(OUTPUT_DIR / "node_index.pkl", "wb") as f:
    pickle.dump(node_index, f)

print("Total nodes:", len(node_index))
print("Saved node_index.pkl")
