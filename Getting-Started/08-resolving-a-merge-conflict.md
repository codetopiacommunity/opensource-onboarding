# Resolving a Merge Conflict

At some point, two people edit the same line in the same file. Git
cannot decide which version to keep, so it stops and asks you to
choose. This is a merge conflict.

It looks scary the first time. It is not. This guide walks you through
a conflict from start to finish using a setup that produces a real one
every time, for every learner, without any timing or coordination with
other people.

---
## What you will do in this guide

- Understand what a merge conflict is and why it happens
- Make a change that is designed to collide with a prepared change
- Trigger the conflict by merging the two together
- Read what Git puts in the file to show you the conflict
- Resolve it and finish the merge

---
## How the exercise works

The practice repo has a permanent branch called
`simulated-upstream-change`. It contains one commit that edits a
specific line in `docs/conflict-practice.md`.

> [!NOTE]
> This branch must exist on your fork for the exercise to work. Since
> it is a branch on the original `codetopiacommunity/open-source-practice`
> repo, it will be present in your fork as long as you forked the repo
> after it was added. If you run `git fetch origin` in Step 4 and do
> not see `simulated-upstream-change` listed, post in the
> <a href="https://discord.gg/md6e2fmfEw" target="_blank" rel="noopener noreferrer">Discord community</a>
> and someone will help you sort it out.

In this guide, you will edit that same line to a different value.
When you then merge the two branches together, Git will see that both
versions changed the same line and will stop and ask you to decide
which one wins.

One important thing to understand before you start: in this exercise
you will use `git fetch origin` and `git merge origin/simulated-upstream-change`,
not `upstream`. That is because `simulated-upstream-change` is a branch
that lives on your fork (`origin`), not on the original repo (`upstream`).
The original repo does not have that branch. The mechanics of fetch and
merge are exactly the same either way. Only the remote name changes
depending on where the branch lives.

---
## Step 1: Sync and create a branch

Navigate to your local clone:

```bash
cd ~/codetopia-community/open-source-practice
```

Sync with the latest from upstream first, as always:

```bash
git checkout main
git fetch upstream
git merge upstream/main
```

Now create a new branch for this exercise:

```bash
git checkout -b practice/merge-conflict
```

What you should see:

```
Switched to a new branch 'practice/merge-conflict'
```

---
## Step 2: Make your change

If you installed VS Code in
[guide 02](./02-installing-and-configuring-git.md), open the file with
that, on any operating system:

```bash
code docs/conflict-practice.md
```

Otherwise use the editor your computer came with. Open
`docs/conflict-practice.md`:

### Windows (Git Bash)

```bash
notepad docs/conflict-practice.md
```

<!-- IMAGE: conflict-practice.md open in Notepad on Windows showing the "Favorite programming language: not set yet" line. Target path: images/08-open-conflict-file-windows.png -->

### macOS

```bash
open -e docs/conflict-practice.md
```

<!-- IMAGE: conflict-practice.md open in TextEdit on macOS showing the "Favorite programming language: not set yet" line. Target path: images/08-open-conflict-file-macos.png -->

### Linux

```bash
nano docs/conflict-practice.md
```

<!-- IMAGE: conflict-practice.md open in nano in the Linux terminal showing the "Favorite programming language: not set yet" line. Target path: images/08-open-conflict-file-linux.png -->

Find this line:

```
Favorite programming language: not set yet
```

Change it to anything you like. For example:

```
Favorite programming language: Python
```

Save the file.

---
## Step 3: Commit your change

```bash
git add docs/conflict-practice.md
git commit -m "chore: set favorite programming language"
```

What you should see:

```
[practice/merge-conflict abc1234] chore: set favorite programming language
 1 file changed, 1 insertion(+), 1 deletion(-)
```

---
## Step 4: Fetch the simulated upstream change

Now fetch the branch from your fork that contains the conflicting
change. Remember: this branch lives on `origin` (your fork), not on
`upstream` (the original repo). That is why you use `origin` here.

```bash
git fetch origin
```

What you should see:

```
From github.com:your-username/open-source-practice
 * [new branch]      simulated-upstream-change -> origin/simulated-upstream-change
```

Git has downloaded all branches from your fork, including
`simulated-upstream-change`. It is now available locally as
`origin/simulated-upstream-change`.

---
## Step 5: Merge and trigger the conflict

Now merge the simulated upstream change branch into your current
branch:

```bash
git merge origin/simulated-upstream-change
```

What you should see:

```
Auto-merging docs/conflict-practice.md
CONFLICT (content): Merge conflict in docs/conflict-practice.md
Automatic merge failed; fix conflicts and then commit the result.
```

<!-- IMAGE: Terminal showing the merge conflict output. The CONFLICT line and "Automatic merge failed" message are clearly visible. Target path: images/merge-conflict-output.png -->

This is the conflict. Git has stopped and is waiting for you to
decide what to do. Nothing is broken. This is exactly what is
supposed to happen.

---
## Step 6: Understand what Git put in the file

Run `git status`:

```bash
git status
```

What you should see:

```
You have unmerged paths.

Unmerged paths:
  both modified: docs/conflict-practice.md
```

Open `docs/conflict-practice.md`. You will see something like this
inside it:

```
<<<<<<< HEAD
Favorite programming language: Python
=======
Favorite programming language: JavaScript
>>>>>>> origin/simulated-upstream-change
```

<!-- IMAGE: The conflict-practice.md file open in a text editor showing the conflict markers. The <<<<<<< HEAD section, ======= divider, and >>>>>>> origin/simulated-upstream-change section are all visible with both conflicting lines. Target path: images/conflict-markers-in-file.png -->

Git has rewritten the file to show you both versions side by side,
with markers to separate them. Here is what each marker means:

- `<<<<<<< HEAD` marks the start of your version. `HEAD` means "what
  is currently on your branch."
- Everything between `<<<<<<< HEAD` and `=======` is your change.
- Everything between `=======` and `>>>>>>>` is the incoming change
  from the other branch.
- `>>>>>>> origin/simulated-upstream-change` marks the end.

Git is not telling you one version is right and the other is wrong.
It is asking: you both edited this line. Which version should the
file have?

---
## Step 7: Resolve the conflict

Edit the file to remove the conflict markers and keep the version you
want. You have three options:

**Keep your version:**

```
Favorite programming language: Python
```

**Keep the incoming version:**

```
Favorite programming language: JavaScript
```

**Write something new entirely:**

```
Favorite programming language: TypeScript
```

The content does not matter for this exercise. What matters is that
when you are done, all three marker lines (`<<<<<<<`, `=======`,
`>>>>>>>`) are gone and the file looks clean with one normal line
where the conflict was.

Save the file.

<!-- IMAGE: The conflict-practice.md file open in a text editor after resolving. No conflict markers are visible. Only the clean resolved line remains, e.g. "Favorite programming language: Python". Target path: images/conflict-resolved-clean.png -->

---
## Step 8: Finish the merge

Tell Git you have resolved the conflict by staging the file:

```bash
git add docs/conflict-practice.md
```

Complete the merge with a commit:

```bash
git commit -m "chore: resolve merge conflict in conflict-practice"
```

Git may open a text editor for the commit message. If it does, the
default message is fine. Save and close the editor.

What you should see:

```
[practice/merge-conflict abc1234] chore: resolve merge conflict in conflict-practice
```

The conflict is resolved. Your branch now contains both changes,
merged together cleanly.

---
## Step 9: Push your branch

```bash
git push origin practice/merge-conflict
```

You can open a pull request from this branch if you like. It does not
need to be merged for the exercise to count as complete.

---
## Quick reference

| What you see | What it means |
|---|---|
| `CONFLICT (content)` | Two branches edited the same line |
| `<<<<<<< HEAD` | Start of your version |
| `=======` | Divider between your version and the incoming version |
| `>>>>>>>` | End of the incoming version |
| `git add` after resolving | Tells Git the conflict in that file is fixed |
| `git commit` after `git add` | Completes the merge |

---
## Stuck?

**`git merge` said `Already up to date` and no conflict appeared.**
The fetch did not bring the other branch down, or you are on the wrong
branch. Run `git fetch origin` again, check `git status` shows your
practice branch, then merge again.

**You committed while the `<<<<<<<` markers were still in the file.**
Open the file, delete every marker line and the duplicated text, save,
then run `git add` and `git commit` again. Nothing is broken.

**You have lost track of what state the merge is in.**
Run `git status`. During a conflict it names every file still needing
resolution and tells you the next command.

**You want to abandon the merge and start over.**
`git merge --abort` puts everything back the way it was before you
merged. It is safe, and it is there for exactly this.

Think you have broken something? You have not, and
[Fixing Mistakes](../FIXING-MISTAKES.md) shows you how to undo it.

Still stuck, or hit something not listed here? Ask. Both of these are
equally welcome, so use whichever suits you:

- <a href="https://github.com/codetopiacommunity/opensource-onboarding/discussions/categories/q-a" target="_blank" rel="noopener noreferrer">GitHub Discussions</a>,
  if you would rather not use a chat app. It needs nothing but the
  GitHub account this course gives you anyway.
- The <a href="https://discord.gg/md6e2fmfEw" target="_blank" rel="noopener noreferrer">Codetopia Community Discord</a>,
  if you want an answer in minutes. Optional, and free.

[Getting Help](../HELP.md) explains both, and how to ask so you get a
useful answer quickly.

---
## What's next?

The last guide covers keeping your fork in sync over time as the
original project keeps moving, and what to do when a reviewer asks
you to update a pull request you already submitted.

🔗 [Keeping Your Fork in Sync](./09-keeping-your-fork-in-sync.md)
