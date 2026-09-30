---
name: axl-verbs
description: Translate a vague design request ("make it more polished", "typeset this", "delight") into concrete measurable checks, or report that the word has no measurable definition. Use before acting on any subjective UI instruction.
---

# axl-verbs

Run this first when the user gives a vague design verb.

```
python3 axl/skills/axl-verbs/scripts/verbs.py "make it more polished"
python3 axl/skills/axl-verbs/scripts/verbs.py --list
```

Read the result:
- `tool-backed`: the word has a definition made of checks. The script prints each check, its command and its pass criteria. Run them with axl-evaluate; offer axl-correct for the fixable ones.
- `undefined`: no source we checked gives this word a measurable meaning. Say so. Ask which property should change and by how much. Do not invent a definition.
- `unknown`: the request holds no dictionary word. Ask for a concrete target.

The "Stays subjective" line names what remains a matter of judgment; tell the user that part is theirs.
The definitions come from `axl/data/definitions.json` (a snapshot is in `references/verbs.json`). Each check cites a claim id and a re-runnable receipt.
