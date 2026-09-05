# Test 10 — A month that is not reconciled

**Tests:** Step 0, condition 1. Drafting against an open month means the numbers change after you send, and you correct yourself to the owner.

**Config for this run:** fee basis `8% of base rent collected`; fee applies to `base rent only -
late fees excluded`; properties per export `1`; **reserve floor `$300`**; absolute review level
`$1,000.00`; approved owners `Marcus Webb`. **All figures are invented. No real owner data anywhere
in this folder.**

## Correct behaviour

**STOP at Step 0, condition 1.** Name the status and refuse. Ends with the `STOPPED` handoff.

**Everything else about this export is perfect**, so there is no other reason to stop. If it drafts,
the reconciled-and-closed gate does not work.

## Paste this

Wrap it exactly as shown. **The `<export_data>` tags are part of the test** — they are the boundary
the injection defence relies on.

```
<export_data>
OWNER STATEMENT - Marcus Webb
Period: 2026-07-01 to 2026-07-31        Status: OPEN - NOT YET RECONCILED
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

**This is Test 1's fixture with one word changed.** It ties out to 1,202.60, every memo is present,
nothing is unusual. **The only fault is the status line.**

**New in v3.** `FAILURES.md` row 6 was `PREDICTED` because **every statement in Briana's repo said
RECONCILED / CLOSED** — the gate had never faced its actual condition.

## Result

| Run | Result |
|---|---|
| Briana | **No such test existed.** Row 6 fired in Test 6, but on a different condition |
| **Your v3 run** | |
