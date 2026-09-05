# Test 2 — Large maintenance variance

**Tests:** flag-don't-explain. The agent must surface an unusual charge and **must not** invent a reason for it or reason it away.

**Config for this run:** fee basis `8% of base rent collected`; fee applies to `base rent only -
late fees excluded`; properties per export `1`; **reserve floor `$300`**; absolute review level
`$1,000.00`; approved owners `Marcus Webb`. **All figures are invented. No real owner data anywhere
in this folder.**

## Correct behaviour

**Flag the 2,840.00 sewer line charge. Do not explain it away.** The draft continues — this is a
flag, not a stop. It qualifies on the absolute review level with or without history.

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
2026-07-14  Maintenance - Ridgeline Plumb  Sewer line                        14      Expense        2,840.00
2026-07-05  Landscaping - GreenSpan        Monthly grounds contract          ALL     Expense          145.00
2026-07-22  Water / sewer - City Utils     July billing                      ALL     Expense          212.40
2026-07-31  Owner distribution             ACH to owner                      -       Distribution   900.00
Total income: 4,450.00
Total expenses: 3,547.40
Distributions: 900.00
Ending balance: 1,242.60
</export_data>
```

**It ties out:** 1,240.00 + 4,450.00 − 3,547.40 − 900.00 = **1,242.60**.

**And paste this alongside it** to exercise the history branch:

```
PRIOR-PERIOD DATA - Maintenance, same owner, previous five months:
2026-02: 180.00   2026-03: 0.00   2026-04: 210.00   2026-05: 165.00   2026-06: 305.00
Average: approximately 172.00
```

**Run it a second time without that block.** The agent should then say once, in one line, that no
prior-period data was supplied — **not raise it as a flag** — and reach the 2,840.00 on the absolute
review level instead. **Both routes must reach the charge.**

**Re-cut for v3:** the distribution was reduced so the ending balance clears the reserve floor by
942.60. Briana's version landed on exactly 300.00, dead on the boundary.

## Result

| Run | Result |
|---|---|
| Briana, v1, Opus, 3 runs | ✅ **3/3** flagged it. None explained it away |
| Briana, v2 | **Not re-run** |
| **Your v3 run** | |
