# Task 05 — Descriptive Statistics and LLM Judgment

## Overview

This project analyzes the 2013 Syracuse University Women's Lacrosse player
statistics dataset using descriptive statistics and language-model judgment
questions.

The project has two main phases:

- **Phase A:** Establish factual ground truth from the dataset.
- **Phase B:** Use descriptive statistics to define measurable concepts and
  evaluate language-model judgments and recommendations.

The goal is to compare model responses against independently calculated
statistics and document both correct reasoning and model errors.

---

## Dataset

### Dataset Used

`data/player_stats_2013.csv`

The dataset contains player-level statistics from the 2013 Syracuse University
Women's Lacrosse season.

The dataset contains 36 player records and includes:

- Player number
- Player
- Games played / games started
- Goals
- Assists
- Points
- Shots
- Shooting percentage
- Shots on goal
- Shots-on-goal percentage
- Game-winning goals
- Free-position goals
- Free-position shots

The dataset is kept locally and is excluded from Git using:

```text
data/*.csv

---

# Phase A — Ground Truth

Phase A establishes independently calculated factual statistics from the
dataset.

The ground-truth script is:

`scripts/ground_truth.py`

Run it with:

```bash
python3 scripts/ground_truth.py


````text
Run Phase A:


```bash
python3 scripts/ground_truth.py

---

# Repository Structure

---

# Phase B — Descriptive Analysis

Phase B examines player-level offensive statistics.

The analysis script is:

`scripts/phase_b_analysis.py`

Run it with:

```bash
python3 scripts/phase_b_analysis.py

---

# Phase B — Metric Definition

The qualitative concept selected for Phase B is:

**Most Valuable Offensive Player**

The operational definition is based on total points:

**Points = Goals + Assists**

Total points are used as the primary ranking metric because they capture both
scoring and playmaking contributions.

If players are tied in points, goals are used as the tiebreaker.

The complete metric definition is documented in:

`results/phase_b_metric_definition.md`

---

# Phase B — LLM Judgment Questions

Three judgment questions were evaluated using the player statistics dataset.

## Judgment Question 1 — Most Valuable Offensive Player

The model identified:

**Alyssa Murray — 104 points**

This matches the independently calculated ground truth.

**Verdict: CORRECT**

## Judgment Question 2 — Murray vs. Treanor

The model selected **Alyssa Murray** as the stronger overall offensive
contributor while recognizing that Kayla Treanor was the stronger goal scorer
and higher-volume shooter.

**Verdict: CORRECT / DEFENSIBLE**

The comparison is a judgment because no explicit weighting was assigned to all
seven metrics.

## Judgment Question 3 — Offensive Development Priority

The model recommended:

**Alyssa Murray**

The recommendation emphasized her 104 points, 40 assists, and 54.2% shooting
percentage while acknowledging Treanor's advantages in goals, shots, shots on
goal, and shots-on-goal percentage.

**Verdict: CORRECT / DEFENSIBLE WITH MINOR ERROR**

The model briefly reversed the shots-on-goal percentage comparison before
correcting itself. The underlying dataset shows Treanor at 81.0% and Murray at
76.3%.

This demonstrates why model-generated numerical analysis should be validated
against independently calculated statistics.

---

# Reproduction

The original dataset must be placed at:

data/player_stats_2013.csv

Run Phase A:

python3 scripts/ground_truth.py

Run Phase B:

python3 scripts/phase_b_analysis.py

The dataset is intentionally excluded from GitHub through .gitignore.

---

# Repository Structure

Task_05_Descriptive_Stats/
    data/player_stats_2013.csv
    results/phase_a_ground_truth.csv
    results/phase_a_prompt_log.md
    results/phase_b_analysis.txt
    results/phase_b_metric_definition.md
    results/phase_b_prompt_log.md
    scripts/ground_truth.py
    scripts/phase_b_analysis.py
    .gitignore
    README.md

---

# Reflection

This project demonstrates that language models can perform well on factual
questions when the questions are clearly constrained by a dataset and the
answers can be checked against independently calculated ground truth.

The model correctly identified Alyssa Murray as the player with the highest
total points and correctly reported the relevant statistics in the Murray
versus Treanor comparison.

The judgment questions were more challenging because they required balancing
multiple metrics. The Murray versus Treanor comparison involved trade-offs
between scoring, playmaking, shot volume, and efficiency.

The offensive development question produced a defensible recommendation, but
the model briefly made an incorrect comparison of shots-on-goal percentage
before correcting itself. This shows why numerical claims in model-generated
analysis should be checked against the underlying data.

Overall, the project demonstrates the importance of clear metric definitions,
independent ground truth, structured prompts, and explicit validation of
model responses.

---

# LLM Evaluation Records

Phase A:
results/phase_a_prompt_log.md

Phase B:
results/phase_b_metric_definition.md
results/phase_b_prompt_log.md

These files preserve the prompts, responses, ground-truth comparisons, and
validation notes used during the analysis.
