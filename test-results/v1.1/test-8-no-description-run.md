STEP 0 - GATE
 1. Reconciled and closed: YES, stated (Status: RECONCILED / CLOSED).
 2. Exactly one owner: YES, Marcus Webb, on the approved list.
 3. Fee basis configured: YES, 8% of base rent collected, late fees excluded. Matches the owner profile.
 4. Period, beginning and ending balances all stated: YES. Period 2026-07-01 to 2026-07-31, beginning 1240.00, ending 1557.60.
GATE PASSED.

------------------------------------------------------------

STEP 1 - INVENTORY
 2026-07-03 | Rent received | July base rent | 12A | Income | 1450.00
 2026-07-02 | Rent received | July base rent | 12B | Income | 1325.00
 2026-07-05 | Rent received | July base rent | 14 | Income | 1600.00
 2026-07-09 | Late fee | 12B - received 2 days late | 12B | Income | 75.00
 2026-07-31 | Management fee | 8% of base rent collected (4375) | ALL | Expense | 350.00
 2026-07-18 | Maintenance - Ridgeline Plumbing | (blank memo) | 12A | Expense | 425.00
 2026-07-05 | Landscaping - GreenSpan | Monthly grounds contract | ALL | Expense | 145.00
 2026-07-22 | Water / sewer - City Utilities | July billing | ALL | Expense | 212.40
 2026-07-31 | Owner distribution | ACH to owner | (no unit, normal for a distribution) | Distribution | 3000.00
No MISSING fields. The blank memo on the Ridgeline Plumbing expense is an unexplained charge, handled at Step 3 and flagged at Step 4.

------------------------------------------------------------

STEP 2 - CROSS-CHECK
2a. COUNT. 9 line items: 4 Income, 4 Expense, 1 Distribution. 4 + 4 + 1 = 9. Matches.
2b. ENUMERATE.
  INCOME
    1450.00
    1325.00
    1600.00
    75.00
  EXPENSES
    350.00
    425.00
    145.00
    212.40
  DISTRIBUTIONS
    3000.00
2c. SUBTOTAL.
  INCOME:        1450.00 + 1325.00 + 1600.00 + 75.00 = 4450.00
  EXPENSES:      350.00 + 425.00 + 145.00 + 212.40 = 1132.40
  DISTRIBUTIONS: 3000.00 = 3000.00
2d. AGAINST THE EXPORT'S STATED SUBTOTALS.
  Income 4450.00 against stated 4450.00. Match.
  Expenses 1132.40 against stated 1132.40. Match.
  Distributions 3000.00 against stated 3000.00. Match.
2e. BALANCE EQUATION.
  1240.00 + 4450.00 - 1132.40 - 3000.00 = 1557.60
2f. COMPARE. Derived 1557.60 against stated 1557.60. Difference 0.00, within tolerance.
2g. CROSS-CHECK PASSED - derived 1557.60 matches stated 1557.60.

------------------------------------------------------------

STEP 3 - EXPLANATIONS
 Management fee 350.00 - the monthly management fee, 8% of base rent collected (4375), as the memo states.
 Maintenance - Ridgeline Plumbing 425.00 (unit 12A) - [NEEDS A HUMAN: no description in the export for this charge]
 Landscaping - GreenSpan 145.00 - the monthly grounds contract with GreenSpan, covering all units.
 Water / sewer - City Utilities 212.40 - July billing from City Utilities, covering all units.

------------------------------------------------------------

STEP 4 - FLAGS
 FLAG - Expense with no description - Maintenance - Ridgeline Plumbing, unit 12A, 425.00 - get the invoice or work order and add what this charge was for before the statement goes out.
 FLAG - Maintenance more than 2x its typical amount - 425.00 against a typical ~172.00 (prior six months 0.00 to 305.00) - confirm the charge is correct and approved, and that it belongs to this owner and this period.
 FLAG - Owner distribution differs from the usual pattern - 3000.00 against a typical ~3,584.00 (prior six months 3,480.00 to 3,675.00) - confirm 3000.00 was the intended distribution and why the ending balance of 1557.60 was held back, so the owner can be told.

 Context I could not check: whether the July billing from City Utilities covers June usage (the profile says water and sewer is billed one month in arrears); and whether Ridgeline Plumbing has any connection to Ridgeline Property Management, since the names share a word.

------------------------------------------------------------

STEP 5 - OWNER UPDATE

```
Subject: Your July 2026 statement

Hello Marcus,

Your July statement is below, and 3000.00 went out to you on the 31st.

Beginning balance   1240.00
Income              4450.00
Expenses            1132.40
Distribution        3000.00
Ending balance      1557.60

Where the 1132.40 went:

- Management fee, 350.00. Eight percent of the 4375 of base rent collected. The 75.00 late fee is not included in that.
- Maintenance, Ridgeline Plumbing, 425.00, unit 12A. [NEEDS A HUMAN: no description in the export for this charge]
- Landscaping, GreenSpan, 145.00. The monthly grounds contract, covering all units.
- Water and sewer, City Utilities, 212.40. The July billing, covering all units.

Nothing needs your attention before next month.

Ridgeline Property Management
```

------------------------------------------------------------

STEP 6 - LIKELY QUESTIONS
 1. What was the management fee calculated on? 8% of the 4375 of base rent collected in July, which is 350.00. The 75.00 late fee from 12B is excluded.
 2. What was the 425.00 Ridgeline Plumbing charge for? The export does not say. [NEEDS A HUMAN: no description in the export for this charge]
 3. Why was the distribution 3000.00 this month? The export records 3000.00 sent by ACH on 2026-07-31, leaving an ending balance of 1557.60, but it does not say why that amount was chosen. [NEEDS A HUMAN: the export does not give a reason for the distribution amount]

------------------------------------------------------------

DRAFT - not sent. 3 flags open. Human review required before release.
