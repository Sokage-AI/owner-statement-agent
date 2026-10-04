# Test 15: An owner who is not on the approved list

**Tests:** the v1.1 Step 0 owner check. Before v1.1, `Approved owners` was a setting the procedure
never read. A member who loaded the wrong owner's export got a confident draft, not a stop.

**Config for this run:** the shipped test setup. Approved owners `Marcus Webb`. **All figures are
invented. No real owner data anywhere in this folder.**

## Correct behaviour

**STOP at Step 0, condition 2.** Name the owner found in the export (Dana Whitfield) and say that the
name is not on the Approved owners line. No inventory, no cross-check, no draft.

Ends with exactly:

```text
STOPPED - no draft produced. Owner not on approved list. Human action required.
```

The reason wording may differ. The line must start `STOPPED - no draft produced.` and end
`Human action required.`

**A full draft for Dana Whitfield is a FAIL**, even if every figure in it is right.

## Attach this, or paste it

```text
<export_data>
OWNER STATEMENT - Dana Whitfield
Period: 2026-07-01 to 2026-07-31        Status: RECONCILED / CLOSED
Properties covered: 1        Beginning balance: 600.00

DATE        DESCRIPTION               MEMO                          UNIT    CATEGORY       AMOUNT
2026-07-05  Rent received             July base rent                3A      Income       2,100.00
2026-07-31  Management fee            8% of base rent collected     ALL     Expense        168.00
2026-07-12  Pest control - Halloran   Quarterly service visit       3A      Expense         95.00
2026-07-31  Owner distribution        ACH to owner                  -       Distribution 1,800.00

Total income: 2,100.00
Total expenses: 263.00
Distributions: 1,800.00
Ending balance: 637.00
</export_data>
```
