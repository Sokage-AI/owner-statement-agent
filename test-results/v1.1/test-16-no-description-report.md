OWNER REPORT DATA - paste this into owner-report.html

```json
{
  "schema": "sokage-owner-report-1",
  "owner": "Marcus Webb",
  "period": "2026-07-01 to 2026-07-31",
  "period_label": "July 2026",
  "subject": "Your July 2026 statement",
  "summary": "Your July statement is below, and 3000.00 went out to you on the 31st.",
  "cross_check": "CROSS-CHECK PASSED - derived 1557.60 matches stated 1557.60.",
  "figures": {
    "beginning": "1240.00",
    "income": "4450.00",
    "expenses": "1132.40",
    "distributions": "3000.00",
    "ending": "1557.60"
  },
  "income": [
    {"date": "2026-07-03", "description": "Rent received", "memo": "July base rent", "unit": "12A", "amount": "1450.00"},
    {"date": "2026-07-02", "description": "Rent received", "memo": "July base rent", "unit": "12B", "amount": "1325.00"},
    {"date": "2026-07-05", "description": "Rent received", "memo": "July base rent", "unit": "14", "amount": "1600.00"},
    {"date": "2026-07-09", "description": "Late fee", "memo": "12B - received 2 days late", "unit": "12B", "amount": "75.00"}
  ],
  "expenses": [
    {"date": "2026-07-31", "description": "Management fee", "explanation": "the monthly management fee, 8% of base rent collected (4375), as the memo states.", "unit": "ALL", "amount": "350.00"},
    {"date": "2026-07-18", "description": "Maintenance - Ridgeline Plumbing", "explanation": "[NEEDS A HUMAN: no description in the export for this charge]", "unit": "12A", "amount": "425.00"},
    {"date": "2026-07-05", "description": "Landscaping - GreenSpan", "explanation": "the monthly grounds contract with GreenSpan, covering all units.", "unit": "ALL", "amount": "145.00"},
    {"date": "2026-07-22", "description": "Water / sewer - City Utilities", "explanation": "July billing from City Utilities, covering all units.", "unit": "ALL", "amount": "212.40"}
  ],
  "distributions": [
    {"date": "2026-07-31", "description": "Owner distribution", "amount": "3000.00"}
  ],
  "flags": [
    "FLAG - Expense with no description - Maintenance - Ridgeline Plumbing, unit 12A, 425.00 - get the invoice or work order and add what this charge was for before the statement goes out.",
    "FLAG - Maintenance more than 2x its typical amount - 425.00 against a typical ~172.00 (prior six months 0.00 to 305.00) - confirm the charge is correct and approved, and that it belongs to this owner and this period.",
    "FLAG - Owner distribution differs from the usual pattern - 3000.00 against a typical ~3,584.00 (prior six months 3,480.00 to 3,675.00) - confirm 3000.00 was the intended distribution and why the ending balance of 1557.60 was held back, so the owner can be told."
  ],
  "attention_next_month": "Nothing needs your attention before next month.",
  "questions": [
    {"question": "What was the management fee calculated on?", "answer": "8% of the 4375 of base rent collected in July, which is 350.00. The 75.00 late fee from 12B is excluded."},
    {"question": "What was the 425.00 Ridgeline Plumbing charge for?", "answer": "The export does not say. [NEEDS A HUMAN: no description in the export for this charge]"},
    {"question": "Why was the distribution 3000.00 this month?", "answer": "The export records 3000.00 sent by ACH on 2026-07-31, leaving an ending balance of 1557.60, but it does not say why that amount was chosen. [NEEDS A HUMAN: the export does not give a reason for the distribution amount]"}
  ],
  "distribution_history": [
    {"period": "2026-01", "amount": "3,600.00"},
    {"period": "2026-02", "amount": "3,675.00"},
    {"period": "2026-03", "amount": "3,540.00"},
    {"period": "2026-04", "amount": "3,610.00"},
    {"period": "2026-05", "amount": "3,480.00"},
    {"period": "2026-06", "amount": "3,600.00"}
  ],
  "sign_off": "Ridgeline Property Management",
  "handoff": "DRAFT - not sent. 3 flags open. Human review required before release."
}
```

DRAFT - not sent. 3 flags open. Human review required before release.
