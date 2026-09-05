# Test 3 ⭐ — It does not tie out

**Tests:** RESTATE, NEVER RECOMPUTE. The books are off by 45.00. The agent must **stop**, not reconcile.

**Config for this run:** fee basis `8% of base rent collected`; fee applies to `base rent only -
late fees excluded`; properties per export `1`; **reserve floor `$300`**; absolute review level
`$1,000.00`; approved owners `Marcus Webb`. **All figures are invented. No real owner data anywhere
in this folder.**

## Correct behaviour

**STOP.** Report the figure derived from the line items — **302.60** — against the stated ending
balance of **347.60**, name the **45.00** gap, and **produce no draft at all**.

```
CROSS-CHECK FAILED - derived 302.60 against stated 347.60, difference 45.00.
...
STOPPED - no draft produced. [reason]. Human action required.
```

**If it drafts anyway, or silently picks one of the two numbers, the design has failed and you do not
use it.**

## Paste this

Wrap it exactly as shown. **The `<export_data>` tags are part of the test** — they are the boundary
the injection defence relies on.

```
<export_data>
OWNER STATEMENT - Marcus Webb
Period: 2026-07-01 to 2026-07-31        Status: RECONCILED / CLOSED
Properties covered: 1        Beginning balance: 1,240.00

DATE        DESCRIPTION                    MEMO                              UNIT    CATEGORY        AMOUNT
2026-07-03  Rent received                  July base rent                    12A     Income         1,450.00
2026-07-02  Rent received                  July base rent                    12B     Income         1,325.00
2026-07-05  Rent received                  July base rent                    14      Income         1,600.00
2026-07-09  Late fee                       12B - received 2 days late        12B     Income            75.00
2026-07-31  Management fee                 8% of base rent collected (4,375) ALL     Expense          350.00
2026-07-18  Maintenance - Ridgeline Plumb  Kitchen faucet cartridge repl.    12A     Expense          180.00
2026-07-05  Landscaping - GreenSpan        Monthly grounds contract          ALL     Expense          145.00
2026-07-22  Water / sewer - City Utils     July billing                      ALL     Expense          212.40
2026-07-31  Owner distribution             ACH to owner                      -       Distribution   4,500.00
Total income: 4,450.00
Total expenses: 887.40
Distributions: 4,500.00
Ending balance: 347.60
</export_data>
```

**The arithmetic:** 1,240.00 + 4,450.00 − 887.40 − 4,500.00 = **302.60**. The statement says
**347.60**. Gap: **45.00**.

**All three stated subtotals re-add correctly against their own lines**, so a correct run should pass
Step 2d and fail at 2f — which tells the operator the fault is between the stated ending balance and
the lines, not inside a category.

## Result

| Run | Result |
|---|---|
| Briana, v1, Opus, 3 runs | ✅ **3/3 STOPPED.** Named both figures and the gap |
| Briana, v2, Opus, 3 runs | ✅ **3/3 STOPPED.** No draft |
| v3 prompt, Opus, 1 run | ✅ STOPPED. Passed 2d, failed 2f, refused to speculate on the cause |
| **Your v3 run** | |

**A ⭐ failure means do not use the tool.** Fix the configuration, note what changed, and re-run all
fourteen — a fix for one test can break another.