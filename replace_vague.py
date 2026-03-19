#!/usr/bin/env python3
"""Replace vague 'who won [league] in [year/decade]' questions with
player/moment/stat-focused questions. Maintains exactly 10,000 total."""

import json
import re
import sys
from collections import Counter

# ── 1. Load questions ───────────────────────────────────────────────
with open("questions.json") as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} questions from questions.json")

# ── 2. Identify vague questions ─────────────────────────────────────
patterns = [
    r"19[0-9]0s",
    r"20[0-9]0s",
    r"in the \d{4}s",
    r"won.{0,20}serie a",
    r"won.{0,20}la liga",
    r"won.{0,20}bundesliga",
    r"won.{0,20}premier league",
    r"won.{0,20}ligue 1",
    r"won.{0,20}champions league",
    r"who won the.{0,15}(league|cup|title|championship)",
]

vague_indices = [
    i for i, x in enumerate(questions)
    if any(re.search(p, x["q"].lower()) for p in patterns)
]

print(f"Found {len(vague_indices)} vague questions")

# Sport distribution of vague questions
vague_by_sport = Counter(questions[i]["sport"] for i in vague_indices)
print(f"By sport: {dict(vague_by_sport)}")

# ── 3. Load replacement questions ──────────────────────────────────
replacement_files = {
    "soccer": "new_soccer.json",
    "baseball": "new_baseball.json",
    "basketball": "new_basketball.json",
    "golf": "new_golf.json",
    "football": "new_football.json",
    "f1": "new_f1.json",
    "hockey": "new_hockey.json",
    "ufc": "new_ufc.json",
}

replacements_by_sport = {}
for sport, fname in replacement_files.items():
    with open(fname) as f:
        replacements_by_sport[sport] = json.load(f)
    print(f"  {sport}: {len(replacements_by_sport[sport])} replacements loaded")

# Verify counts match
for sport, count in vague_by_sport.items():
    available = len(replacements_by_sport.get(sport, []))
    if available < count:
        print(f"ERROR: {sport} needs {count} but only has {available}")
        sys.exit(1)

# ── 4. Replace like-for-like by sport ──────────────────────────────
sport_cursors = {sport: 0 for sport in replacements_by_sport}

for idx in vague_indices:
    sport = questions[idx]["sport"]
    cursor = sport_cursors[sport]
    questions[idx] = replacements_by_sport[sport][cursor]
    sport_cursors[sport] = cursor + 1

replaced = len(vague_indices)
print(f"\nReplaced {replaced} questions")

# ── 5. Deduplicate against existing_questions.txt ──────────────────
with open("existing_questions.txt") as f:
    existing = set(line.strip() for line in f if line.strip())

new_q_texts = [q["q"] for q in questions]
dupes = [i for i, q in enumerate(new_q_texts) if q in existing]
if dupes:
    print(f"WARNING: {len(dupes)} duplicates found against existing_questions.txt")
    for i in dupes[:10]:
        print(f"  [{i}] {questions[i]['q'][:80]}")
else:
    print("No duplicates against existing_questions.txt")

# Check internal duplicates
internal_dupes = len(new_q_texts) - len(set(new_q_texts))
if internal_dupes:
    print(f"WARNING: {internal_dupes} internal duplicate question texts")
else:
    print("No internal duplicates")

# ── 6. Verify total count ──────────────────────────────────────────
assert len(questions) == 10000, f"Expected 10000, got {len(questions)}"
print(f"\nTotal questions: {len(questions)} (verified)")

# Verify no vague patterns remain in replaced questions
still_vague = [
    i for i in vague_indices
    if any(re.search(p, questions[i]["q"].lower()) for p in patterns)
]
if still_vague:
    print(f"WARNING: {len(still_vague)} replacements still match vague patterns")
else:
    print("All replacements pass vague-pattern check")

# ── 7. Save ────────────────────────────────────────────────────────
with open("questions.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"\nSaved questions.json with {len(questions)} questions")

# Final sport distribution
final_sports = Counter(q["sport"] for q in questions)
print(f"Final sport distribution: {dict(final_sports)}")
