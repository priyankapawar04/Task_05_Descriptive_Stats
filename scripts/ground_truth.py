import pandas as pd

DATA_PATH = "data/player_stats_2013.csv"

df = pd.read_csv(DATA_PATH)

# -----------------------------
# Ground truth: player statistics
# Source: Syracuse University Athletics
# 2013 Women's Lacrosse Cumulative Statistics
# -----------------------------

# Official team totals from the source
TEAM_GAMES = 22
TEAM_GOALS = 332
OPPONENT_GOALS = 188
TEAM_ASSISTS = 138
TEAM_POINTS = 470
TEAM_SHOTS = 700
TEAM_SHOOTING_PCT = 0.474
TEAM_SOG = 533
TEAM_SOG_PCT = 0.761
TEAM_WINS = 18
TEAM_LOSSES = 4

print("=== 2013 Syracuse Women's Lacrosse: Ground Truth ===")
print(f"Games: {TEAM_GAMES}")
print(f"Wins: {TEAM_WINS}")
print(f"Losses: {TEAM_LOSSES}")
print(f"Goals: {TEAM_GOALS}")
print(f"Opponent goals: {OPPONENT_GOALS}")
print(f"Assists: {TEAM_ASSISTS}")
print(f"Points: {TEAM_POINTS}")
print(f"Shots: {TEAM_SHOTS}")
print(f"Shooting percentage: {TEAM_SHOOTING_PCT:.3f}")
print(f"Shots on goal: {TEAM_SOG}")
print(f"SOG percentage: {TEAM_SOG_PCT:.3f}")

avg_goals = TEAM_GOALS / TEAM_GAMES
avg_opp_goals = OPPONENT_GOALS / TEAM_GAMES
avg_margin = (TEAM_GOALS - OPPONENT_GOALS) / TEAM_GAMES

print(f"\nAverage goals per game: {avg_goals:.2f}")
print(f"Average opponent goals per game: {avg_opp_goals:.2f}")
print(f"Average scoring margin: {avg_margin:.2f}")

print("\n=== Player Ground Truth ===")

top_goals = df.loc[df["goals"].idxmax()]
top_assists = df.loc[df["assists"].idxmax()]
top_points = df.loc[df["points"].idxmax()]
top_shots = df.loc[df["shots"].idxmax()]
top_sog = df.loc[df["sog"].idxmax()]

print(f"Most goals: {top_goals['player']} ({int(top_goals['goals'])})")
print(f"Most assists: {top_assists['player']} ({int(top_assists['assists'])})")
print(f"Most points: {top_points['player']} ({int(top_points['points'])})")
print(f"Most shots: {top_shots['player']} ({int(top_shots['shots'])})")
print(f"Most shots on goal: {top_sog['player']} ({int(top_sog['sog'])})")

print("\nTop 10 players by points:")
print(df[["player", "goals", "assists", "points"]]
      .sort_values("points", ascending=False)
      .head(10)
      .to_string(index=False))

# Save a machine-readable answer key
answer_key = {
    "games": TEAM_GAMES,
    "wins": TEAM_WINS,
    "losses": TEAM_LOSSES,
    "goals": TEAM_GOALS,
    "opponent_goals": OPPONENT_GOALS,
    "assists": TEAM_ASSISTS,
    "points": TEAM_POINTS,
    "shots": TEAM_SHOTS,
    "shooting_pct": TEAM_SHOOTING_PCT,
    "sog": TEAM_SOG,
    "sog_pct": TEAM_SOG_PCT,
    "average_goals_per_game": avg_goals,
    "average_opponent_goals_per_game": avg_opp_goals,
    "average_scoring_margin": avg_margin,
    "most_goals_player": top_goals["player"],
    "most_goals": int(top_goals["goals"]),
    "most_assists_player": top_assists["player"],
    "most_assists": int(top_assists["assists"]),
    "most_points_player": top_points["player"],
    "most_points": int(top_points["points"]),
    "most_shots_player": top_shots["player"],
    "most_shots": int(top_shots["shots"]),
    "most_sog_player": top_sog["player"],
    "most_sog": int(top_sog["sog"]),
}

pd.DataFrame([answer_key]).to_csv("results/phase_a_ground_truth.csv", index=False)
print("\nSaved: results/phase_a_ground_truth.csv")
