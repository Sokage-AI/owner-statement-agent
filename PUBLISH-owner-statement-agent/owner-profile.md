# Owner profile — TEMPLATE

**Copy this once per owner. Drop it into your Claude Project's knowledge files.**

Why this exists: the dry run's biggest finding was that **most false flags are under-specified
config, not a bad model.** A profile per owner is how you stop re-typing the config every month and
stop the agent asking the same question every month.

**One file per owner. Never combine two owners in one file** — that is the failure with no recovery.

---

```
OWNER PROFILE

Owner name:                Marcus Webb
Properties covered:        1
Units:                     12A, 12B, 14

FEE TERMS
Management fee basis:      8% of base rent COLLECTED, not billed
Fee applies to:            base rent only - late fees, pet rent, application fees excluded
Fee charged on:            last day of the month

THRESHOLDS
Reserve floor:             $300 total for this owner
Absolute review level:     any single expense at or above $1,000.00

KNOWN QUIRKS - things that look wrong every month and are not
  - Unit 12B pays 2 to 3 days late most months. A late fee here is normal, not a variance.
  - Landscaping is a flat monthly contract with GreenSpan. It does not vary by season.
  - Water and sewer is billed one month in arrears by City Utilities.

STANDING QUESTIONS THIS OWNER ASKS
  - Always asks what the management fee was calculated on.
  - Always asks whether a repair was preventable.

SIGN-OFF
  Ridgeline Property Management
```

---

**The KNOWN QUIRKS block is the one that earns its place.** Without it the agent flags unit 12B's late
fee as an anomaly every single month, and by month three the operator stops reading flags. **That is
failure-mode row 8, and it is the only predicted failure that actually happened.**

**Re-check this file quarterly.** Profiles drift. A fee basis that changed and was never updated here
produces a confident wrong number, which is the one output that does real damage.
