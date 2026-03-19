#!/bin/bash
cd /Users/gabrieldidario/.openclaw/workspace/nosebleed-trivia
claude --permission-mode bypassPermissions --print 'Replace 740 vague "who won [league] in [year/decade]" questions with engaging player/moment-focused questions.

WORKSPACE: /Users/gabrieldidario/.openclaw/workspace/nosebleed-trivia/

STEP 1 — Find them:
```python
import json, re
with open("questions.json") as f: q = json.load(f)
patterns = [r"19[0-9]0s", r"20[0-9]0s", r"in the \d{4}s", r"won.{0,20}serie a", r"won.{0,20}la liga", r"won.{0,20}bundesliga", r"won.{0,20}premier league", r"won.{0,20}ligue 1", r"won.{0,20}champions league", r"who won the.{0,15}(league|cup|title|championship)"]
to_replace = [i for i,x in enumerate(q) if any(re.search(p, x["q"].lower()) for p in patterns)]
print(len(to_replace))
```

STEP 2 — Write 740 replacement questions. Distribution: soccer=296, baseball=233, basketball=92, golf=78, football=22, f1=11, hockey=7, ufc=1

FORMATS TO USE (never use "who won [league] in [year]"):
A — Player identity clue: "I won 4 Ballon dOr awards in a row from 2009 to 2012. Who am I?"
B — Describe the moment: "This striker scored a hat-trick in the 2022 World Cup final but still ended up on the losing side. Name him."
C — Stat-based: "He hit 73 home runs in 2001, the most ever in a single MLB season. Who was he?"
D — Career achievement: "Known as El Clasico biggest rivalry, this club has won the most La Liga titles all-time. Name them."
E — Comparison: "These two players combined for 40+ combined Ballon dOr nominations but only one of them has won a World Cup. Who won it?"
F — Nickname clue: "Called The Black Panther, this Juventus striker scored 115 Serie A goals in the 1970s. Name him."
G — Context clue: "This manager won the Champions League three times with the same club in the 2010s. Name him."

RULES:
- Historically accurate facts only
- No em dashes
- All 4 choices must be plausible, answer included
- No duplicates vs existing_questions.txt  
- No "who won [league] in [year]" or "which team won [league] in [decade]" phrasing
- Replace like-for-like: soccer vague → soccer good, baseball vague → baseball good

STEP 3 — Write replace_vague.py that:
1. Loads questions.json
2. Finds the 740 vague questions by index
3. Replaces with new questions
4. Deduplicates
5. Saves — must equal 10,000
6. Prints final count

STEP 4 — Run it, verify count, then:
openclaw system event --text "Vague questions replaced — 740 league/decade winner questions upgraded. 10,000 verified." --mode now
