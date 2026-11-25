#!/bin/sh
# Rebuild plugin/ (the Claude directory package) from the root files. Text only: the directory
# refuses scripts and HTML from unverified organizations, so check.py and owner-report.html stay in the repo root.
set -e
cd "$(dirname "$0")"
S=plugin/skills/owner-statement-agent
mkdir -p plugin/.claude-plugin "$S"
cp plugin-src/plugin.json plugin/.claude-plugin/plugin.json
cp plugin-src/icon.png plugin/.claude-plugin/icon.png
cp PROMPT.md NEVER.md FAILURES.md owner-profile.md history.md "$S/"
sed -e 's#`check.py`#`check.py` (in the full repository, https://github.com/Sokage-AI/owner-statement-agent)#g' \
    -e 's#`owner-report.html`#`owner-report.html` (in the full repository, https://github.com/Sokage-AI/owner-statement-agent)#g' \
    SKILL.md > "$S/SKILL.md"
