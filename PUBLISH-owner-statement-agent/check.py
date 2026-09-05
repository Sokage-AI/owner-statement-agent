#!/usr/bin/env python3
"""
check.py - independently re-add an owner statement export.

The agent explains the statement. This checks the arithmetic, deterministically,
with no model involved at all. Run both. If they disagree, trust this one.

Why it exists: the agent performs exactly one calculation on the owner's money,
and that single calculation is the whole safety case. A language model doing
arithmetic is probably right. A seven-line script doing arithmetic is right.

No dependencies. No network. No API key. Nothing leaves your machine.

Usage:
    python3 check.py statement.txt
    cat statement.txt | python3 check.py
    python3 check.py statement.txt --json

Exit codes:
    0  the statement ties out
    1  it does not tie out, or a required figure is missing
    2  the file could not be parsed
"""

import sys
import re
import json

TOLERANCE = 0.02          # a rounding cent is not a mismatch
CATEGORIES = ("Income", "Expense", "Distribution")


def money(text):
    """'1,240.00' or '(45.00)' or '-45.00' -> float."""
    t = text.strip().replace(",", "").replace("$", "")
    if t.startswith("(") and t.endswith(")"):
        t = "-" + t[1:-1]
    return float(t)


def find_owners(body):
    """Every distinct owner named in the export.

    Two forms in the wild: the name in the header, or an OWNER column with a
    different name on each row. The second is the dangerous one - a combined
    export whose header says nothing about how many owners are inside it.
    """
    names = set()

    for hit in re.findall(r"OWNER STATEMENT\s*[-\u2014,]\s*([^\n(,]+)", body):
        name = hit.strip()
        # a placeholder header tells us nothing; the rows do
        if name.upper() not in ("COMBINED", "ALL", "ALL OWNERS", "MULTIPLE", "SUMMARY"):
            names.add(name)

    # an OWNER column, located by its position among 2+ space separated headers
    col = None
    for line in body.splitlines():
        cells = re.split(r",|\s{2,}", line.strip())
        upper = [c.upper() for c in cells]
        if col is None:
            if "OWNER" in upper and "AMOUNT" in upper and "CATEGORY" in upper:
                col = upper.index("OWNER")
            continue
        if len(cells) > col and re.search(r"[\d,]+\.\d{2}\s*$", line):
            value = cells[col].strip()
            if value and value not in ("-", "\u2014", "ALL"):
                names.add(value)

    return sorted(names)


def parse(raw):
    """Pull the line items and the stated figures out of an export."""
    body = raw
    m = re.search(r"<export_data>(.*?)</export_data>", raw, re.S)
    if m:
        body = m.group(1)

    rows = []
    for line in body.splitlines():
        # Two shapes in the wild: a CSV straight out of the accounting system,
        # or the whitespace-aligned text you get from pasting one. Both end the
        # same way - category, then amount.
        stripped = line.rstrip().rstrip(",")
        hit = re.search(
            r"\b(%s)\b\s*[,\s]\s*(\(?-?\$?[\d,]+\.\d{2}\)?)\s*$" % "|".join(CATEGORIES),
            stripped,
        )
        if hit:
            rows.append(
                {
                    "category": hit.group(1),
                    "amount": money(hit.group(2)),
                    "text": " ".join(line.split())[:70],
                }
            )

    def stated(label):
        # "Beginning balance: 1,240.00" and "Beginning balance,1240.00" both count
        hit = re.search(
            r"%s\s*[:,]?\s*(\(?-?\$?[\d,]+\.\d{2}\)?)" % label, body, re.I
        )
        return money(hit.group(1)) if hit else None

    return {
        "rows": rows,
        "beginning": stated("Beginning balance"),
        "ending": stated("Ending balance"),
        "stated_income": stated("Total income"),
        "stated_expenses": stated("Total expenses"),
        "stated_distributions": stated("Distributions"),
        "owners": find_owners(body),
        "reconciled": bool(re.search(r"RECONCILED\s*/\s*CLOSED", body, re.I)),
    }


def check(d):
    """Re-add everything and report. Returns (report_dict, exit_code)."""
    findings, rows = [], d["rows"]
    if not rows:
        return {"error": "No line items found. Is this an owner statement export?"}, 2

    sums = {c: round(sum(r["amount"] for r in rows if r["category"] == c), 2)
            for c in CATEGORIES}
    counts = {c: sum(1 for r in rows if r["category"] == c) for c in CATEGORIES}

    # the export's own stated subtotals, where it gives them
    for cat, key in (("Income", "stated_income"),
                     ("Expense", "stated_expenses"),
                     ("Distribution", "stated_distributions")):
        if d[key] is not None and abs(d[key] - sums[cat]) > TOLERANCE:
            findings.append(
                "SUBTOTAL MISMATCH in %s: lines add to %,.2f, statement says %,.2f "
                "(difference %,.2f)".replace(",.2f", ".2f")
                % (cat, sums[cat], d[key], d[key] - sums[cat])
            )

    if d["beginning"] is None:
        findings.append("MISSING: no beginning balance stated. Cannot verify.")
    if d["ending"] is None:
        findings.append("MISSING: no ending balance stated. Cannot verify.")

    derived = gap = None
    if d["beginning"] is not None and d["ending"] is not None:
        derived = round(
            d["beginning"] + sums["Income"] - sums["Expense"] - sums["Distribution"], 2
        )
        gap = round(derived - d["ending"], 2)
        if abs(gap) > TOLERANCE:
            findings.append(
                "DOES NOT TIE OUT: lines derive %.2f, statement states %.2f, "
                "difference %.2f" % (derived, d["ending"], gap)
            )

    if len(d["owners"]) > 1:
        findings.append(
            "MORE THAN ONE OWNER in this export: %s. Run one owner at a time."
            % ", ".join(d["owners"])
        )
    if not d["reconciled"]:
        findings.append(
            "NOT MARKED RECONCILED / CLOSED. Do not draft against an open month."
        )

    return {
        "counts": counts,
        "total_lines": len(rows),
        "subtotals": sums,
        "beginning": d["beginning"],
        "derived_ending": derived,
        "stated_ending": d["ending"],
        "difference": gap,
        "ties_out": bool(gap is not None and abs(gap) <= TOLERANCE),
        "findings": findings,
    }, (0 if not findings else 1)


def render(r):
    out = ["", "  LINE ITEMS"]
    out.append("    %d total  |  %d income, %d expense, %d distribution"
               % (r["total_lines"], r["counts"]["Income"],
                  r["counts"]["Expense"], r["counts"]["Distribution"]))
    out += ["", "  SUBTOTALS FROM THE LINES"]
    for c in CATEGORIES:
        out.append("    %-14s %12.2f" % (c, r["subtotals"][c]))
    out += ["", "  BALANCE"]
    if r["beginning"] is not None:
        out.append("    %-14s %12.2f" % ("Beginning", r["beginning"]))
    if r["derived_ending"] is not None:
        out.append("    %-14s %12.2f   <- from the lines"
                   % ("Derived ending", r["derived_ending"]))
    if r["stated_ending"] is not None:
        out.append("    %-14s %12.2f   <- what the statement claims"
                   % ("Stated ending", r["stated_ending"]))
    if r["difference"] is not None:
        out.append("    %-14s %12.2f" % ("Difference", r["difference"]))
    out.append("")
    if not r["findings"]:
        out += ["  RESULT: TIES OUT. Arithmetic is consistent.", ""]
    else:
        out.append("  RESULT: %d PROBLEM%s"
                   % (len(r["findings"]), "" if len(r["findings"]) == 1 else "S"))
        for f in r["findings"]:
            out.append("    - " + f)
        out += ["", "  Do not send anything to the owner until a human resolves these.", ""]
    return "\n".join(out)


def main():
    args = [a for a in sys.argv[1:] if a != "--json"]
    as_json = "--json" in sys.argv[1:]
    try:
        raw = open(args[0]).read() if args else sys.stdin.read()
    except OSError as e:
        print("Could not read that file: %s" % e, file=sys.stderr)
        sys.exit(2)

    report, code = check(parse(raw))
    if "error" in report:
        print(report["error"], file=sys.stderr)
        sys.exit(2)
    print(json.dumps(report, indent=2) if as_json else render(report))
    sys.exit(code)


if __name__ == "__main__":
    main()
