# Test Execution Results — Student Marks and Grade Calculator

The program was executed using Python for all ten test cases. Each screenshot file below is a terminal-style SVG capture showing the supplied inputs and the output produced by the run.

## Results

| Test ID | Input marks | Expected result | Actual result | Status |
|---|---|---|---|---|
| TC-01 | 90, 92, 88, 95, 85 | Grade A | Grade A | PASS |
| TC-02 | 80, 80, 80, 80, 80 | Grade B | Grade B | PASS |
| TC-03 | 70, 75, 80, 65, 60 | Grade C | Grade C | PASS |
| TC-04 | 60, 60, 60, 60, 60 | Grade D | Grade D | PASS |
| TC-05 | 40, 40, 40, 40, 40 | Grade E | Grade E | PASS |
| TC-06 | 30, 35, 25, 40, 20 | Grade F | Grade F | PASS |
| TC-07 | 100, 100, 100, 100, 100 | Grade A | Grade A | PASS |
| TC-08 | 0, 0, 0, 0, 0 | Grade F | Grade F | PASS |
| TC-09 | 90, 85, -1, 70, 60 | Invalid marks message | Invalid marks message | PASS |
| TC-10 | 90, 85, 101, 70, 60 | Invalid marks message | Invalid marks message | PASS |

**Summary: 10 passed, 0 failed.**

## Screenshots

- [TC-01 — Grade A](test_screenshots/TC-01.svg)
- [TC-02 — Grade B](test_screenshots/TC-02.svg)
- [TC-03 — Grade C](test_screenshots/TC-03.svg)
- [TC-04 — Grade D](test_screenshots/TC-04.svg)
- [TC-05 — Grade E](test_screenshots/TC-05.svg)
- [TC-06 — Grade F](test_screenshots/TC-06.svg)
- [TC-07 — Maximum marks](test_screenshots/TC-07.svg)
- [TC-08 — Zero marks](test_screenshots/TC-08.svg)
- [TC-09 — Invalid negative mark](test_screenshots/TC-09.svg)
- [TC-10 — Invalid mark above 100](test_screenshots/TC-10.svg)

## Important note
These are generated terminal-output screenshots based on actual local Python subprocess executions, not photographs or captures of a physical computer screen. The test result table records the observed output from those executions.
