import csv
import matplotlib.pyplot as plt

DATA_FILE = "data/player_stats_2013.csv"
OUTPUT_FILE = "results/murray_vs_treanor_offense.png"


def load_players():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def main():
    rows = load_players()

    selected = {}

    for row in rows:
        player = row["player"]

        if player in ["Murray, Alyssa", "Treanor, Kayla"]:
            selected[player] = row

    metrics = [
        "goals",
        "assists",
        "points",
        "shots",
    ]

    murray_values = [float(selected["Murray, Alyssa"][m]) for m in metrics]
    treanor_values = [float(selected["Treanor, Kayla"][m]) for m in metrics]

    x = range(len(metrics))
    width = 0.35

    plt.figure(figsize=(10, 6))

    plt.bar(
        [i - width / 2 for i in x],
        murray_values,
        width,
        label="Alyssa Murray",
    )

    plt.bar(
        [i + width / 2 for i in x],
        treanor_values,
        width,
        label="Kayla Treanor",
    )

    plt.xticks(list(x), ["Goals", "Assists", "Points", "Shots"])
    plt.ylabel("Count")
    plt.title("Murray vs. Treanor — Offensive Comparison")
    plt.legend()
    plt.tight_layout()

    plt.savefig(OUTPUT_FILE, dpi=200)
    plt.close()

    print(f"Saved visualization to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
