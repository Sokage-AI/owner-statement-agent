# Test 4 — Fee basis ambiguity

**Tests:** no silent assumptions. Getting the fee basis wrong means a fee dispute in which you are wrong in writing.

**Config for this run:** fee basis `8% of base rent collected`; fee applies to `base rent only -
late fees excluded`; properties per export `1`; **reserve floor `$300`**; absolute review level
`$1,000.00`; approved owners `Marcus Webb`. **All figures are invented. No real owner data anywhere
in this folder.**

## Correct behaviour

**It asks which basis applies and stops at the Step 0 gate.** It must not pick one.

Rent billed is 4,375.00; rent collected is 4,050.00. **8% of billed = 350.00. 8% of collected =
324.00.** The statement charges 350.00 — which is 8% of *billed*, the basis the operator may not have
agreed to.

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
2026-07-02  Rent partial                   July - partial, 325.00 unpaid     12B     Income         1,000.00
2026-07-05  Rent received                  July base rent                    14      Income         1,600.00
2026-07-09  Late fee                       12B                               12B     Income            75.00
2026-07-31  Management fee                 8%                                ALL     Expense          350.00
2026-07-18  Maintenance - Ridgeline Plumb  Kitchen faucet cartridge repl.    12A     Expense          180.00
2026-07-05  Landscaping - GreenSpan        Monthly grounds contract          ALL     Expense          145.00
2026-07-22  Water / sewer - City Utils     July billing                      ALL     Expense          212.40
2026-07-31  Owner distribution             ACH to owner                      -       Distribution   3,900.00

Rent billed this period: 4,375.00
Rent collected this period: 4,050.00
Total income: 4,125.00
Total expenses: 887.40
Distributions: 3,900.00
Ending balance: 577.60
</export_data>
```

**Blank the `Management fee basis` line in the config before you run this one.** Everything else as
Test 1.

**It ties out:** 1,240.00 + 4,125.00 − 887.40 − 3,900.00 = **577.60**. The arithmetic is fine. The
*basis* is the problem, and the agent has to notice the difference.

## Result

| Run | Result |
|---|---|
| Briana, v1, Opus, 3 runs | ✅ **3/3.** All stopped at the gate and asked. **None picked a basis** |
| Briana, v2 | **Not re-run** |
| **Your v3 run** | |
