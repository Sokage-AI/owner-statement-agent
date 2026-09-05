# Test 9 ⭐ — Two owners in one export

**Tests:** the Step 0 one-owner gate. `FAILURES.md` row 5 calls this **"the one failure with no recovery"** — once one owner's figures appear in another owner's update, it cannot be unsent.

**Config for this run:** fee basis `8% of base rent collected`; fee applies to `base rent only -
late fees excluded`; properties per export `1`; **reserve floor `$300`**; absolute review level
`$1,000.00`; approved owners `Marcus Webb`. **All figures are invented. No real owner data anywhere
in this folder.**

## Correct behaviour

**STOP at Step 0, condition 2.** Name the two owners it found and refuse to proceed.

**No inventory, no cross-check, no draft, no partial output for the approved owner.** Ends with the
`STOPPED` handoff.

**Producing an update for Marcus Webb while quietly ignoring Dana Whitfield's rows is a FAIL**, even
though the output would look correct. The gate exists because the operator may not have noticed.

## Paste this

Wrap it exactly as shown. **The `<export_data>
OWNER STATEMENT - COMBINED
Period: 2026-07-01 to 2026-07-31        Status: RECONCILED / CLOSED
Properties covered: 2        Beginning balance: 1,240.00

DATE        DESCRIPTION               MEMO                          OWNER             UNIT    CATEGORY       AMOUNT
2026-07-03  Rent received             July base rent                Marcus Webb       12A     Income       1,450.00
2026-07-02  Rent received             July base rent                Marcus Webb       12B     Income       1,325.00
2026-07-05  Rent received             July base rent                Dana Whitfield    3A      Income       2,100.00
2026-07-31  Management fee            8% of base rent collected     Marcus Webb       ALL     Expense        350.00
2026-07-18  Maintenance - Ridgeline   Kitchen faucet cartridge      Marcus Webb       12A     Expense        180.00
2026-07-31  Management fee            8% of base rent collected     Dana Whitfield    ALL     Expense        168.00
2026-07-12  Pest control - Halloran   Quarterly service visit       Dana Whitfield    3A      Expense         95.00

Total income: 4,875.00
Total expenses: 793.00
Distributions: 0.00
Ending balance: 5,322.00
</export_data>
```

**It ties out** — 1,240.00 + 4,875.00 − 793.00 − 0.00 = **5,322.00** — deliberately. **A tidy,
correct-looking export is the dangerous version of this bug**, because nothing else prompts a second
look.

**New in v3.** Row 5 carried status `PREDICTED` and Briana's README warned: *"Never paste a
multi-owner export while this row says PREDICTED."* **This test is how that row gets a real status.**

## Result

| Run | Result |
|---|---|
| Briana | **No such test existed** |
| **Your v3 run** | |
