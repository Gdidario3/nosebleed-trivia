#!/usr/bin/env python3
"""
Load new trivia questions from q_*.py files, deduplicate against existing questions,
and append exactly 2,304 new questions to questions.json to reach 10,000 total.
"""
import json
import os
import sys
import importlib.util

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_JSON = os.path.join(WORKSPACE, "questions.json")
EXISTING_TXT = os.path.join(WORKSPACE, "existing_questions.txt")

# Per-sport targets
TARGETS = {
    "soccer": 302,
    "ufc": 256,
    "olympics": 276,
    "f1": 258,
    "tennis": 253,
    "golf": 249,
    "basketball": 200,
    "football": 170,
    "baseball": 149,
    "hockey": 91,
}
TOTAL_TARGET = 2304

# Source files for each sport
SPORT_FILES = {
    "soccer": "q_soccer.py",
    "ufc": "q_ufc.py",
    "olympics": "q_olympics.py",
    "f1": "q_f1.py",
    "tennis": "q_tennis.py",
    "golf": "q_golf.py",
    "basketball": "q_basketball.py",
    "football": "q_football.py",
    "baseball": "q_baseball.py",
    "hockey": "q_hockey.py",
}


def load_questions_from_py(filepath):
    """Load questions list from a Python file that defines `questions = [...]`."""
    spec = importlib.util.spec_from_file_location("mod", filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.questions


def normalize(text):
    """Normalize question text for dedup comparison."""
    return text.strip().lower()


def main():
    # 1. Load existing questions text for dedup
    existing_set = set()
    if os.path.exists(EXISTING_TXT):
        with open(EXISTING_TXT, "r") as f:
            for line in f:
                existing_set.add(line.strip().lower())
    print(f"Loaded {len(existing_set)} existing question texts for dedup")

    # 2. Load questions.json
    with open(QUESTIONS_JSON, "r") as f:
        current_questions = json.load(f)
    current_count = len(current_questions)
    print(f"Current questions.json count: {current_count}")

    needed = 10000 - current_count
    print(f"Need {needed} more questions to reach 10,000")

    if needed <= 0:
        print("Already at or above 10,000. Nothing to do.")
        return

    # 3. Load all new questions from source files
    all_new = {}
    for sport, filename in SPORT_FILES.items():
        filepath = os.path.join(WORKSPACE, filename)
        if not os.path.exists(filepath):
            print(f"WARNING: {filename} not found, skipping {sport}")
            continue
        qs = load_questions_from_py(filepath)
        all_new[sport] = qs
        print(f"  {sport}: loaded {len(qs)} questions from {filename}")

    # 4. Validate and filter each question
    new_seen = set()  # Track within-batch dedup
    filtered_by_sport = {sport: [] for sport in TARGETS}

    for sport, qs in all_new.items():
        for q in qs:
            # Validate structure
            if not all(k in q for k in ("q", "a", "choices", "sport", "difficulty")):
                continue
            if len(q["choices"]) != 4:
                continue
            if q["a"] not in q["choices"]:
                continue
            if q["difficulty"] not in ("easy", "medium", "hard"):
                continue

            # Normalize and dedup
            norm_q = normalize(q["q"])

            # Skip if matches existing
            if norm_q in existing_set:
                continue

            # Skip if already seen in this batch
            if norm_q in new_seen:
                continue

            new_seen.add(norm_q)
            # Force correct sport tag
            q["sport"] = sport
            filtered_by_sport[sport].append(q)

    # 5. Report filtered counts
    print("\nFiltered counts per sport:")
    total_available = 0
    for sport in TARGETS:
        count = len(filtered_by_sport[sport])
        target = TARGETS[sport]
        status = "OK" if count >= target else f"SHORT by {target - count}"
        print(f"  {sport}: {count} available (target: {target}) [{status}]")
        total_available += count

    print(f"\nTotal available after dedup: {total_available}")
    print(f"Total needed: {needed}")

    # 6. Select exactly the right number per sport
    final_questions = []
    remaining_needed = needed

    for sport in TARGETS:
        target = TARGETS[sport]
        available = filtered_by_sport[sport]

        # Take up to target, or all available if less
        take = min(target, len(available), remaining_needed)
        selected = available[:take]
        final_questions.extend(selected)
        remaining_needed -= take
        print(f"  {sport}: selected {take}/{target}")

    # If we still need more (some sports were short), take extras from sports with surplus
    if remaining_needed > 0:
        print(f"\nNeed {remaining_needed} more from surplus sports...")
        for sport in TARGETS:
            if remaining_needed <= 0:
                break
            target = TARGETS[sport]
            available = filtered_by_sport[sport]
            already_taken = min(target, len(available))
            surplus = available[already_taken:]
            take = min(len(surplus), remaining_needed)
            if take > 0:
                final_questions.extend(surplus[:take])
                remaining_needed -= take
                print(f"  {sport}: took {take} surplus questions")

    print(f"\nFinal new questions to add: {len(final_questions)}")

    # 7. Append to questions.json
    current_questions.extend(final_questions)
    with open(QUESTIONS_JSON, "w") as f:
        json.dump(current_questions, f, indent=2, ensure_ascii=False)

    # 8. Update existing_questions.txt
    with open(EXISTING_TXT, "a") as f:
        for q in final_questions:
            f.write(normalize(q["q"]) + "\n")

    final_count = len(current_questions)
    print(f"\nFinal questions.json count: {final_count}")

    if final_count == 10000:
        print("SUCCESS: Exactly 10,000 questions!")
    elif final_count < 10000:
        print(f"WARNING: Still short by {10000 - final_count} questions")
    else:
        print(f"WARNING: Over by {final_count - 10000} questions")

    # Print sport distribution
    sport_counts = {}
    for q in current_questions:
        s = q.get("sport", "unknown")
        sport_counts[s] = sport_counts.get(s, 0) + 1
    print("\nFinal sport distribution:")
    for sport, count in sorted(sport_counts.items()):
        print(f"  {sport}: {count}")


if __name__ == "__main__":
    main()
