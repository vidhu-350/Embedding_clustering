import pandas as pd
import os

INPUT_FOLDER = "data/cleaned"
OUTPUT_FOLDER = "data/weekly"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for file in sorted(os.listdir(INPUT_FOLDER)):
    if not file.endswith(".csv"):
        continue

    print(f"Processing {file}...")

    filepath = os.path.join(INPUT_FOLDER, file)
    df = pd.read_csv(filepath)

    df["time"] = pd.to_datetime(df["bidirectional_first_seen_ms"], unit="ms", errors="coerce")
    df = df.dropna(subset=["time"])

    df["year"] = df["time"].dt.isocalendar().year
    df["week"] = df["time"].dt.isocalendar().week

    for (year, week), group in df.groupby(["year", "week"]):
        output_file = f"weekly_{year}_W{int(week):02d}.csv"
        output_path = os.path.join(OUTPUT_FOLDER, output_file)

        group.drop(columns=["time", "year", "week"]).to_csv(
            output_path,
            mode="a",
            header=not os.path.exists(output_path),
            index=False
        )

print("Weekly snapshot creation completed.")
