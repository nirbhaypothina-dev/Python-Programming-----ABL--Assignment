# Case 4 - Problem 31: String-Based Examination Answer Evaluation

key = input("Enter 10-question Answer Key (e.g. ABCDABCDAB): ").upper()

students = [
    ("26A01", "Ananya", "ABCDABXXAB"),
    ("26A02", "Kiran", "ABCCABDDAB"),
    ("26A03", "Meena", "ADCDXXCDCB"),
    ("26A04", "Rohit", "DCBAXXXXDC")
]

print("--- Exam Result Evaluation ---")
for st in students:
    roll, name, ans = st
    correct = 0
    wrong = 0
    unanswered = 0

    for i in range(len(key)):
        if ans[i] == "X":
            unanswered = unanswered + 1
        elif ans[i] == key[i]:
            correct = correct + 1
        else:
            wrong = wrong + 1

    marks = (correct * 4) - (wrong * 1)
    if marks >= 16:
        res = "PASS"
    else:
        res = "FAIL"

    print(roll, name, "-> Correct:", correct, "Wrong:", wrong, "Unanswered:", unanswered, "Marks:", marks, "Result:", res)
