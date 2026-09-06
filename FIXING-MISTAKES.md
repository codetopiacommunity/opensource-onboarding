# Fixing Mistakes

**You cannot break this.** Read that again, because it is the single
most useful thing to know when you are starting out.

Git was built by people who make mistakes, for people who make
mistakes. Almost everything you can do is reversible, and the few
things that are not are clearly flagged in this page. Nothing you do on
your own computer affects anybody else until you deliberately push it,
and even then it can be fixed.

You do not need to read this page in order. Find the heading that
matches what happened, do that, and carry on.

> [!TIP]
> Before fixing anything, run `git status`. It tells you what state you
> are in, and it very often tells you the exact command to get out. It
> is completely safe: it only looks, it never changes anything.

---
## First, two words that keep coming up

**Staged** means you have run `git add` on a file, putting it in line
to be included in your next commit. Think of putting something in a box
before sealing it.

**Committed** means you have run `git commit`, sealing the box. The
snapshot is now saved in your project's history on your computer.

Most of the fixes below are about stepping back one of those stages.

---
## I changed a file and want to undo it

You edited something, you do not like it, and you have **not** run
`git add` or `git commit` yet.

To throw away your changes to one file:

```bash
git restore docs/about.md
```

Replace `docs/about.md` with the path to your file. The file goes back
to how it looked at your last commit.

What you should see: nothing at all. Git does this silently. Run
`git status` afterwards and the file will no longer be listed as
changed.

> [!IMPORTANT]
> This one genuinely cannot be undone. Those edits were never saved
> anywhere, so Git has nothing to bring back. Only run it when you are
> sure you want the changes gone.

---
## I ran `git add` on the wrong file

You staged something you did not mean to. Nothing is lost, you just
want it out of the box before sealing it.

```bash
git restore --staged notes.txt
```

What you should see: nothing printed. Run `git status` and the file
moves from "Changes to be committed" back down to "Changes not staged
for commit". **Your edits are still there.** This only changes whether
the file is queued for the next commit.

---
## I typed the wrong commit message

You committed, and the message has a typo or does not describe what you
did. As long as you have **not pushed yet**, replace it:

```bash
git commit --amend -m "docs: fix the typo in the about page"
```

What you should see: the commit reappears with your new message and the
same changes. `--amend` means "redo the last commit instead of making a
new one".

---
## I forgot to include a file in my commit

Same fix. Stage the missing file, then amend:

```bash
git add docs/resources.md
git commit --amend --no-edit
```

`--no-edit` means "keep the message I already wrote". The file joins
the previous commit as though you had never forgotten it.

---
## I committed to `main` and should have used a branch

Very common, and completely fixable. Your commit is safe the whole
time.

First, make a branch containing the work you just did:

```bash
git checkout -b fix/my-change
```

Your commit is now on `fix/my-change`, where it belongs. But it is
still sitting on `main` as well, so move `main` back to match GitHub:

```bash
git checkout main
git reset --hard origin/main
git checkout fix/my-change
```

What you should see: you end up on your new branch with your work
intact, and `main` clean again.

> [!IMPORTANT]
> `git reset --hard` throws away uncommitted changes on the branch you
> run it on. In the steps above that is exactly what you want, because
> your work is safely on the new branch by then. Do not run it at other
> times without understanding that.

---
## I want to see what I actually changed

Not a mistake, but it is what you should do before panicking.

```bash
git status
```

Shows which files changed and whether they are staged.

```bash
git diff
```

Shows the changes themselves, line by line. Lines starting with `-`
were removed, lines starting with `+` were added.

Press `q` to get back to your prompt if the output fills the screen.

---
## I deleted a file by accident

If you have not committed the deletion:

```bash
git restore deleted-file.md
```

The file comes straight back, exactly as it was at your last commit.

---
## I started a merge and it went wrong

If you are in the middle of a merge conflict and want out entirely:

```bash
git merge --abort
```

What you should see: nothing printed, and everything back exactly as
it was before you ran `git merge`. This is completely safe, and it
exists for precisely this moment. Merge conflicts are covered in
[Resolving a Merge Conflict](./Getting-Started/08-resolving-a-merge-conflict.md).

---
## I already pushed something wrong

If the wrong thing is on GitHub, on **your own branch in your own
fork**, and nobody else is using that branch, fix it locally using the
sections above and then push again with:

```bash
git push --force-with-lease origin your-branch-name
```

This rewrites what is on GitHub to match your computer.
`--force-with-lease` is the careful version: it refuses if somebody
else has pushed to that branch in the meantime.

> [!IMPORTANT]
> Never do this on a branch other people are working on, and never on
> `main` of a shared project. Rewriting history that others have
> already downloaded creates a real mess for them. On your own branch,
> before anyone has reviewed it, it is fine.

If you have pushed something that should never be public, such as a
password or a key, force pushing is **not** enough on its own. Treat
the secret as compromised and change it immediately. Anyone could
already have copied it.

---
## I am completely lost

Take a breath. This is normal, and there is a way back.

**Step 1.** Run `git status` and read it slowly. It describes the
situation and often names the command out of it.

**Step 2.** If you are mid-merge, run `git merge --abort`.

**Step 3.** If you just want your files back to the last commit, and
you accept losing uncommitted edits:

```bash
git checkout main
git reset --hard origin/main
```

**Step 4.** The last resort, and it is a completely legitimate one:
delete the whole folder and clone it again from your fork. You lose
only work that was never pushed. Nobody will know, nobody will care,
and experienced developers do this too.

```bash
cd ~/codetopia-community
rm -rf open-source-practice
git clone git@github.com:your-username/open-source-practice.git
```

Replace `your-username` with your actual GitHub username.

> [!IMPORTANT]
> `rm -rf` deletes a folder and everything in it, permanently and
> without asking. Check twice that the folder name is right before
> pressing Enter. There is no recycle bin for this.

---
## Quick reference

| What happened | What to run |
|---|---|
| Changed a file, want it back | `git restore <file>` |
| Staged the wrong file | `git restore --staged <file>` |
| Wrong commit message | `git commit --amend -m "new message"` |
| Forgot a file in the commit | `git add <file>` then `git commit --amend --no-edit` |
| Committed to `main` by mistake | `git checkout -b <branch>`, then reset `main` |
| Merge went wrong | `git merge --abort` |
| Want to see what changed | `git status`, then `git diff` |
| Totally lost | `git status`, then re-clone if needed |

---
## Still stuck?

Ask in
<a href="https://github.com/codetopiacommunity/opensource-onboarding/discussions/categories/q-a" target="_blank" rel="noopener noreferrer">GitHub Discussions</a>
using the **Q&A** category. Your question turns up in the community
Discord by itself, so people see it there without you having to ask
twice, and replies come back on the discussion.

Paste the output of `git status` when you ask. It tells whoever is
helping you almost everything they need to know.

[Getting Help](./HELP.md) covers asking well, and the
[Glossary](./GLOSSARY.md) explains any word here you have not met.
