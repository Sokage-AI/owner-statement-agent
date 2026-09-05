STEP 0 - GATE
 1. Reconciled and closed: YES, stated ("Status: RECONCILED / CLOSED").
 2. Exactly one owner: NO. The export is titled "OWNER STATEMENT - COMBINED",
    covers Properties: 2, and the OWNER column lists two distinct owners across
    its line items - Marcus Webb (2026-07-03, 2026-07-02, 2026-07-31, 2026-07-18)
    and Dana Whitfield (2026-07-05, 2026-07-31, 2026-07-12). This is not a
    single-owner export.
 3. Fee basis configured and matches this owner's agreement: CANNOT DETERMINE.
    The operator config states 8% of base rent collected for the approved
    owner, Marcus Webb. The export shows two different management fee lines -
    350.00 tagged to Marcus Webb and 168.00 tagged to Dana Whitfield - and with
    two owners mixed together there is no single "this owner" to check the
    basis against. Dana Whitfield is also not on the Approved owners list in
    the operator config (Approved owners: Marcus Webb).
 4. Period, beginning balance, ending balance stated: stated for the export as
    a whole (Period 2026-07-01 to 2026-07-31, Beginning balance 1,240.00,
    Ending balance 5,322.00) - but these figures are combined across two
    owners' properties, not a single owner's balance.

GATE FAILED - condition 2 (and consequently condition 3).

This export must be split into one statement per owner before this procedure
can run. I need, for one owner at a time:
 - A single-owner export containing only Marcus Webb's line items, with that
   owner's own beginning balance and ending balance (not a balance shared with
   another owner's property).
 - Confirmation that Dana Whitfield is an approved owner if a statement for
   her is also wanted - she is not currently on the Approved owners list in
   the operator config.

Per the governing rules, running this procedure across more than one owner at
once is prohibited outright (never_list item 11), independent of anything else
found above. No inventory, cross-check, or draft has been produced.

STOPPED - no draft produced. Export covers two owners, not one. Human action required.
