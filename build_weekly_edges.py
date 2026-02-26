import pandas as pd
from collections import defaultdict
from pathlib import Path
import ipaddress
import sys
import os

INPUT_FILE = sys.argv[1]
OUTPUT_DIR = "graphs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

edge_weights = defaultdict(int)
chunksize = 200000

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except:
        return False

cols = ["src_ip", "dst_port"]

for chunk in pd.read_csv(INPUT_FILE, usecols=cols, chunksize=chunksize):

    chunk = chunk.dropna(subset=["src_ip", "dst_port"])

    for ip, port in zip(chunk["src_ip"], chunk["dst_port"]):

        if not is_valid_ip(ip):
            continue

        try:
            port = int(port)
            if port < 1 or port > 65535:
                continue
        except:
            continue

        src = f"IP_{ip}"
        dst = f"PORT_{port}"

        edge_weights[(src, dst)] += 1


edges = [(src, dst, weight) for (src, dst), weight in edge_weights.items()]

out_path = Path(OUTPUT_DIR) / (Path(INPUT_FILE).stem + "_edges.csv")

pd.DataFrame(edges, columns=["src", "dst", "weight"]).to_csv(out_path, index=False)

print("Saved:", out_path)
