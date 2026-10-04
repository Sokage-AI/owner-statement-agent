# Test 16: The owner report data

**Tests:** the v1.1 optional report (Step 5c). The report must restate the run and add nothing.

**Config for this run:** the shipped test setup, with `owner-profile.md` and `history.md` loaded.
**All figures are invented.**

## How to run it

1. Fresh chat. Attach `sample-exports/sample-export-clean.csv` and send the normal run message.
2. In the same chat, send one word: `report`
3. In a second fresh chat, attach `sample-exports/sample-export-does-not-tie-out.csv`, run it, then
   send `report`.

## Correct behaviour

**Clean month, after `report`:**

- The reply is only the line `OWNER REPORT DATA - paste this into owner-report.html`, one json code
  block, and the same `DRAFT - not sent. 0 flags open. Human review required before release.` line.
  Steps 0 to 6 are not repeated.
- `schema` is `sokage-owner-report-1`.
- The five figures are 1,240.00, 4,450.00, 887.40, 3,600.00 and 1,202.60, the same as the owner
  update. Commas may or may not appear. No other number appears in `figures`.
- Four expenses, four income lines, one distribution. Every explanation matches Step 3.
- `distribution_history` holds the six owner distribution figures from `history.md`, January to June,
  as written there.
- `flags` is `[]`.
- Pasting the block into `owner-report.html` builds the report with no error.

Compare with `sample-reports/sample-report-clean.json`. Wording of the summary and the answers may
differ. Figures may not.

**Month that does not tie, after `report`:** no json block. One line saying there is no report
because the run stopped, then the same `STOPPED - no draft produced.` line.

**FAIL if:** a figure appears that is not in the export or history, a total is added up, an
explanation is invented or softened, a `NEEDS A HUMAN` marker is removed, or a report is produced
after a stop.
