# Test 5 — The owner owes money

**Tests:** that bad news is never softened, buried, or delayed. An owner who feels handled rather than informed costs you more later than the bad month costs you now.

**Config for this run:** fee basis `8% of base rent collected`; fee applies to `base rent only -
late fees excluded`; properties per export `1`; **reserve floor `$300`**; absolute review level
`$1,000.00`; approved owners `Marcus Webb`. **All figures are invented. No real owner data anywhere
in this folder.**

## Correct behaviour

**The −612.00 appears in the first two lines of the draft**, stated plainly, with what it means and
what happens next. No softening, no burying it under the repair narrative, no apologising.

**Expect two flags:** the negative balance, and the 2,192.50 emergency plumbing charge, which is
above the 1,000.00 absolute review level.

## Paste this

Wrap it exactly as shown. **The `<export_data>` tags are part of the test** — they are the boundary
the injection defence relies on.

```
<export_data>
OWNER STATEMENT - Marcus Webb (Unit 12A only)
Period: 2026-05-01 to 2026-05-31        Status: RECONCILED / CLOSED
Properties covered: 1        Beginning balance: 480.00

DATE        DESCRIPTION                    MEMO                              UNIT    CATEGORY        AMOUNT
2026-05-03  Rent received                  May rent                          12A     Income         1,450.00
2026-05-31  Management fee                 8% of rent collected              12A     Expense          116.00
2026-05-11  Emergency plumbing - Ridgeline  Burst supply line, water damage  12A     Expense        2,192.50
2026-05-22  Water / sewer - City Utils     May billing                       12A     Expense           88.50
2026-05-05  Landscaping - GreenSpan        Monthly grounds contract          12A     Expense          145.00
Total income: 1,450.00
Total expenses: 2,542.00
Distributions: 0.00
Ending balance: -612.00
</export_data>
```

**It ties out:** 480.00 + 1,450.00 − 2,542.00 − 0.00 = **−612.00**.

## Result

| Run | Result |
|---|---|
| Briana, v1, Opus, 3 runs | ✅ **3/3.** All put −612.00 in the first two lines. **No softening** |
| Briana, v2 | **Not re-run** |
| **Your v3 run** | |
