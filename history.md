# Prior-period history — TEMPLATE

**Copy this once per owner. Drop it into your Claude Project's knowledge files, alongside the owner
profile. Update it after each month closes.**

---

## Why this file is not optional

**Step 4's variance check cannot run without it.** This was the second defect the dry run found, and
every single run reported it unprompted: a one-month export contains no history, so *"more than 2x
that category's typical amount"* has nothing to compare against.

**Without this file the agent falls back to the absolute review level alone** — a flat dollar
threshold. That catches a $2,840 sewer line. **It does not catch a landscaping bill that quietly
tripled from $145 to $420**, because $420 is under any sensible threshold.

**That is the whole point of the file.** The expensive surprises are caught by the threshold. The
creeping ones are only caught by history.

---

```
PRIOR-PERIOD DATA - Marcus Webb
Last updated: 2026-07-31

MONTHLY TOTALS BY CATEGORY, most recent six closed months

CATEGORY          2026-01   2026-02   2026-03   2026-04   2026-05   2026-06   TYPICAL
Rent collected   4,375.00  4,375.00  4,375.00  4,375.00  4,375.00  4,375.00  4,375.00
Late fees            0.00     75.00     75.00      0.00     75.00     75.00     ~50.00
Management fee     350.00    350.00    350.00    350.00    350.00    350.00    350.00
Maintenance        180.00      0.00    210.00    165.00    305.00    172.00    ~172.00
Landscaping        145.00    145.00    145.00    145.00    145.00    145.00    145.00
Water / sewer      198.60    204.10    212.40    209.80    215.20    212.40    ~208.00
Owner distribution 3,600.00 3,675.00 3,540.00  3,610.00  3,480.00  3,600.00  ~3,584.00

CATEGORIES SEEN BEFORE
  Rent, Late fee, Management fee, Maintenance, Landscaping, Water / sewer,
  Owner distribution

ANYTHING OUTSIDE THAT LIST IS A NEW CATEGORY AND GETS FLAGGED.
```

---

## How to use it

**Paste it with the export**, inside the same `<export_data>` block or immediately after it, whenever
you want the history-based checks to run.

**When you do not paste it**, the agent says so once, in one line, and does not treat its absence as a
flag. That behaviour is deliberate and was added in v2 — an agent that raises "no history supplied"
as a flag every month is training the operator to skim.

**Six months is enough.** Twelve is better if you have it. Fewer than three and the "typical" column
is noise.
