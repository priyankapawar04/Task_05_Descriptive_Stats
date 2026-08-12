import csv
import statistics


DATA_FILE = "data/player_stats_2013.csv"


def load_data(file_path):
    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def to_float(value):
    if value == "" or value is None:
        return None
    return float(value)


def main():
    rows = load_data(DATA_FILE)

    print("=== Phase B: Descriptive Analysis ===")
    print(f"Total player records: {len(rows)}")

    print("\n" + "=" * 60)
    print("PLAYER STATISTICS")
    print("=" * 60)

    numeric_columns = [
        "goals",
        "assists",
        "points",
        "shots",
        "shooting_pct",
        "sog",
        "sog_pct",
        "gwg",
        "fpg",
        "fps",
    ]

    for column in numeric_columns:
        values = [
            to_float(row[column])
            for row in rows
            if to_float(row[column]) is not None
        ]

        print("\n" + "-" * 60)
        print(f"Column: {column}")
        print("-" * 60)
        print(f"Count  : {len(values)}")
        print(f"Mean   : {statistics.mean(values):.2f}")
        print(f"Median : {statistics.median(values):.2f}")
        print(f"Minimum: {min(values):.2f}")
        print(f"Maximum: {max(values):.2f}")

    print("\n" + "=" * 60)
    print("TOP PLAYERS")
    print("=" * 60)

    player_metrics = {
        "goals": "Most Goals",
        "assists": "Most Assists",
        "points": "Most Points",
        "shots": "Most Shots",
        "sog": "Most Shots on Goal",
    }

    for column, label in player_metrics.items():
        best_player = max(
            rows,
            key=lambda row: to_float(row[column])
        )

        print(
            f"{label:<22}: "
            f"{best_player['player']} "
            f"({to_float(best_player[column]):.0f})"
        )


if __name__ == "__main__":
    main()
