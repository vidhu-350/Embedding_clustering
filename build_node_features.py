import pandas as pd
import numpy as np
import pickle
from collections import defaultdict
from pathlib import Path
import math

EDGE_FILE = "graphs/global_edges.csv"

with open("features/node_index.pkl", "rb") as f:
    node_index = pickle.load(f)

num_nodes = len(node_index)

degree = np.zeros(num_nodes)
weighted_degree = np.zeros(num_nodes)

df = pd.read_csv(EDGE_FILE)

for src, dst, weight in zip(df["src"], df["dst"], df["weight"]):
    src_idx = node_index[src]
    dst_idx = node_index[dst]

    degree[src_idx] += 1
    degree[dst_idx] += 1

    weighted_degree[src_idx] += weight
    weighted_degree[dst_idx] += weight

# log transform weighted degree
log_weighted_degree = np.log1p(weighted_degree)

# node type feature
node_type = np.zeros(num_nodes)
for node, idx in node_index.items():
    if node.startswith("PORT_"):
        node_type[idx] = 1

# stack features
X = np.vstack([
    degree,
    log_weighted_degree,
    node_type
]).T

np.save("features/node_features.npy", X)

print("Feature matrix shape:", X.shape)
print("Saved node_features.npy")
