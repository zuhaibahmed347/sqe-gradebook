78008f2 (HEAD -> feature/rename-field-b, origin/feature/rename-field-b) Merge branch 'main' into feature/rename-field-b
06fa729 (origin/main, origin/HEAD, main) Rename roll_no to student_id (#4)
ec81456 Rename roll_no to id_number
a2ebc3d Improve Student Score Handling (#3)
350c8f9 Add score-adding capability to Student (#2)
aba30cb add student class stub
2e218df Delete src/gradebook/gradebook.py
cd4e04c 'chore: initial project structure'
f1ceb54 Update gradebook.py
36e7e0c Create gradebook.py



# Comments 
refactor(student): validate score is numeric and within 0-100 range

Previously add_score() only rejected negative values. This adds
type-checking and an upper bound so invalid scores fail fast with
a clear ValueError instead of silently corrupting the scores list.

refactor(student): rename score param and tighten validation per review

Renamed `score` to `student_score` for clarity, added numeric type
check and upper-bound validation (0-100) as requested in PR #3 review.
