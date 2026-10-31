# Merge Conflict Notes

## Where the conflict occurred
File: `README.md`, line beginning `**Project status:**`.

## How it was created
After branching `proposal` from `main`, both branches changed the **same original line** independently and committed their changes.

- `main` committed: `**Project status:** Baseline regression ready`
- `proposal` committed: `**Project status:** Proposal finalized for review`

When merging `main` into `proposal` locally with `git merge main --no-ff`, Git stopped with a real **content merge conflict** in `README.md`.

## What the conflict markers showed
```text
<<<<<<< HEAD
**Project status:** Proposal finalized for review
=======
**Project status:** Baseline regression ready
>>>>>>> main
```

## Manual resolution
I opened `README.md`, removed the `<<<<<<<`, `=======`, and `>>>>>>>` markers, and replaced the conflicting line with one statement reflecting both branches:

```text
**Project status:** Proposal reviewed; baseline regression ready
```

I then staged `README.md` and `CONFLICT_NOTES.md` and completed the in-progress merge commit on `proposal`.

## Verification
- `git status` shows a clean working tree.
- `git log --graph --oneline --all` preserves the divergent changes and merge commit.
- The `proposal` branch contains the final `proposal.md` and this conflict report.
- A Pull Request from `proposal` into `main` can now be merged on GitHub without an unresolved conflict.
