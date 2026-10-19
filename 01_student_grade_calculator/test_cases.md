# Test Cases — Student Marks and Grade Calculator

## Purpose
These test cases verify that the program calculates the total, percentage, and grade for five subject marks, and rejects a mark outside the valid range.

## Grade rules used by this program
- A: percentage >= 90
- B: percentage >= 80 and < 90
- C: percentage >= 70 and < 80
- D: percentage >= 60 and < 70
- E: percentage >= 40 and < 60
- F: percentage < 40

These are sample assignment rules. Replace them if your faculty provides different grade boundaries.

## Test cases

| Test ID | Input marks (five subjects) | Expected total | Expected percentage | Expected result |
|---|---|---:|---:|---|
| TC-01 | 90, 92, 88, 95, 85 | 450 / 500 | 90.00% | Grade A |
| TC-02 | 80, 80, 80, 80, 80 | 400 / 500 | 80.00% | Grade B |
| TC-03 | 70, 75, 80, 65, 60 | 350 / 500 | 70.00% | Grade C |
| TC-04 | 60, 60, 60, 60, 60 | 300 / 500 | 60.00% | Grade D |
| TC-05 | 40, 40, 40, 40, 40 | 200 / 500 | 40.00% | Grade E |
| TC-06 | 30, 35, 25, 40, 20 | 150 / 500 | 30.00% | Grade F |
| TC-07 | 100, 100, 100, 100, 100 | 500 / 500 | 100.00% | Grade A |
| TC-08 | 0, 0, 0, 0, 0 | 0 / 500 | 0.00% | Grade F |
| TC-09 | 90, 85, -1, 70, 60 | Not calculated | Not calculated | Display invalid marks message and stop |
| TC-10 | 90, 85, 101, 70, 60 | Not calculated | Not calculated | Display invalid marks message and stop |

## How to execute
1. Open a terminal in this folder.
2. Run `python main.py` (or `python3 main.py`).
3. Enter each test case's marks when prompted.
4. Compare the program output with the expected result above.
5. Record the actual result and mark each test as Pass or Fail for your submission.

## Test execution record

| Test ID | Actual result | Status (Pass/Fail) | Notes |
|---|---|---|---|
| TC-01 | To be filled after running | Pending | |
| TC-02 | To be filled after running | Pending | |
| TC-03 | To be filled after running | Pending | |
| TC-04 | To be filled after running | Pending | |
| TC-05 | To be filled after running | Pending | |
| TC-06 | To be filled after running | Pending | |
| TC-07 | To be filled after running | Pending | |
| TC-08 | To be filled after running | Pending | |
| TC-09 | To be filled after running | Pending | |
| TC-10 | To be filled after running | Pending | |
