import json
from tennis_batch import questions as tennis_qs
from f1_batch import questions as f1_qs

new_questions = tennis_qs + f1_qs

# Load existing question texts for dedup
with open("existing_questions.txt", "r") as f:
    existing = set(line.strip().lower() for line in f if line.strip())

# Filter out duplicates
filtered = [q for q in new_questions if q["q"].strip().lower() not in existing]

dupes = len(new_questions) - len(filtered)
if dupes:
    print(f"Filtered out {dupes} duplicate(s)")

# Load questions.json
with open("questions.json", "r") as f:
    data = json.load(f)

print(f"Existing questions: {len(data)}")
print(f"Adding: {len(filtered)} (tennis: {sum(1 for q in filtered if q['sport']=='tennis')}, f1: {sum(1 for q in filtered if q['sport']=='f1')})")

# Append and save
data.extend(filtered)

with open("questions.json", "w") as f:
    json.dump(data, f, indent=2)

# Update existing_questions.txt
with open("existing_questions.txt", "a") as f:
    for q in filtered:
        f.write(q["q"].strip().lower() + "\n")

print(f"New total: {len(data)}")
