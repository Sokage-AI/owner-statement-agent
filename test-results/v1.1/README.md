# v1.1 checks (2026-10-04)

Eight saved replies from four independent conversations on Claude Opus 5.5, each in a fresh context
with the procedure as Project instructions and the files attached as a member would attach them.

| File | Case | Result |
|---|---|---|
| `test-1-clean-run.md` | Clean month | Draft, 0 flags |
| `test-16-clean-report.md` | `report` after the clean month | Valid report data, same figures |
| `test-8-no-description-run.md` | A charge with no description | `NEEDS A HUMAN`, 3 flags, no guess about the work |
| `test-16-no-description-report.md` | `report` after it | `NEEDS A HUMAN` kept in the report data |
| `test-3-does-not-tie-run.md` | Books 45.00 out | Stop, no draft |
| `test-16-report-after-stop.md` | `report` after the stop | Refused |
| `test-15-owner-not-approved.md` | Owner not on the approved list | Stop at the gate |
| `test-15-other-firm-config.md` | Another firm's settings, Marcus Webb's month | Stop at the gate |

One run before the final wording called the unexplained charge a "plumbing repair" in the likely
questions. The rule against guessing now covers every part of the output, and the rerun above is
clean. That earlier run is not saved here because the prompt that produced it is not the released one.

Four conversations is a smoke test, not a sweep. The 159-run record covers v1.0.
