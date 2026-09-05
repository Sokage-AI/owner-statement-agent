# Test 1 — Clean month (baseline)

**Tests:** that a month with nothing wrong in it produces **zero flags**. A tool that flags a clean month is a tool people stop reading by month three.

**Config for this run:** fee basis `8% of base rent collected`; fee applies to `base rent only -
late fees excluded`; properties per export `1`; **reserve floor `$300`**; absolute review level
`$1,000.00`; approved owners `Marcus Webb`. **All figures are invented. No real owner data anywhere
in this folder.**

## Correct behaviour

A clean draft, **0 flags**, ending exactly:

```
DRAFT - not sent. 0 flags open. Human review required before release.
```

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
2026-07-31  Owner distribution             ACH to owner                      -       Distribution   3,600.00
Total income: 4,450.00
Total expenses: 887.40
Distributions: 3,600.00
Ending balance: 1,202.60
</export_data>
```

**It ties out:** 1,240.00 + 4,450.00 − 887.40 − 3,600.00 = **1,202.60**, which is what the statement says.

**Re-cut for v3.** Briana's original ended at 302.60 against the same $300 reserve floor — **$2.60 of
headroom.** It passed 3/3, but a baseline test decided by $2.60 produces a flake rate at scale that
looks like model instability and is really a fixture bug. **This version has $902.60 of headroom**, so
the only way it flags is a genuine fault.

## Result

| Run | Result |
|---|---|
| Briana, v1, Opus, 3 runs *(302.60 fixture)* | ⚠️ **0/3.** Every run raised 2 flags where zero were correct |
| Briana, v2, Opus, 3 runs *(302.60 fixture)* | ✅ **3/3.** Zero flags |
| v3 prompt, Opus, 1 run *(302.60 fixture)* | ✅ Zero flags. Ruled on both ambiguities explicitly |
| **Your v3 run** | |
