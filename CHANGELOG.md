# Changelog

## v1.1.0 (2026-10-04)

**New: the owner report.** After a run that produced a draft, send the word `report`. The agent
returns the run as a block of report data. Paste it into `owner-report.html`, which opens in any
browser, and you get a finished owner report: the five figures, every expense with what it was for,
money in, recent distributions, and the owner's likely questions. Add your firm colour and logo once.
Save it as a PDF and send it with your normal process.

- The page loads nothing from the internet and sends nothing. The data stays on your computer.
- The page never calculates. It shows the figures the agent restated, exactly as given.
- Flags and the cross-check line stay on your screen in a review panel. They never print on the
  owner's copy.
- The page will not let you mark a report reviewed while any charge still says `NEEDS A HUMAN`.
- The agent refuses to produce a report after a stop.

**Fixed: the Approved owners setting is now enforced.** Step 0 condition 2 now stops when the owner in
the export is not on the `Approved owners` line. Before this, the setting was never read, so loading
the wrong owner's export produced a confident draft instead of a stop.

**Tightened: no guessing anywhere.** The rule against inferring work from a vendor name now covers the
flags, the update, the likely questions and the report, not only the explanations. A check run found
the likely questions calling an undescribed charge a "plumbing repair". Fixed and rerun.

**What the evidence covers.** The 159-run record in `test-results/` was produced on v1.0. The v1.1 changes
are tests 15 and 16, with eight saved Claude replies in `test-results/v1.1/`. Run them on your own
setup before a live month. Nothing else in
the procedure changed.

## v1.0.0 (2026-09-13)

First public release.
