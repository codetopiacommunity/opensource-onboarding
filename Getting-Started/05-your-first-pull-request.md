# Your First Pull Request

You forked the practice repository, cloned it, and set up both your
`origin` and `upstream` remotes. Now you make a real change and submit
it for review.

A pull request (PR) is how you propose changes to a repo. Instead of
editing the original directly, you make changes on your fork and say
"here is what I changed, can you review and merge it?" A maintainer
reviews your changes, gives feedback, and either merges them or asks
you to fix something first.

This is how all open source contribution works. In this guide, you do
it for the first time.

---
## What you will do in this guide

- Sync your fork with the latest changes from upstream
- Create a new branch for your change
- Add your name to the contributors list
- Push your branch to your fork
- Open a pull request

---
## Step 1: Go to your cloned repo

Open your terminal and navigate to the repo you cloned in the previous
guide:

```bash
cd ~/codetopia-community/open-source-practice
```

Confirm you are in the right place:

```bash
ls
```

You should see files like `README.md`, `CONTRIBUTORS.md`, and a `docs/`
folder.

> [!TIP]
> If you get "No such file or directory," you may have cloned the repo
> into a different location. Run `ls ~/codetopia-community` to find it.

---
## Step 2: Sync with upstream before starting

Before you make any change, always pull the latest version of the
project from `upstream` first. This ensures you are working from the
most current state, not a version that has already fallen behind.

```bash
git checkout main
git fetch upstream
git merge upstream/main
```

What each command does:

- `git checkout main`: switch to the main branch. You should already
  be on it right after cloning, but running this as a habit means you
  will never accidentally start work on the wrong branch.
- `git fetch upstream`: download any new commits from the original repo
  without changing your files yet
- `git merge upstream/main`: apply those new commits to your local main

What you should see:

```
Already up to date.
```

Or a list of files that were updated. Either way, you are now starting
from the latest version.

Then push the updated state to your fork so it is current too:

```bash
git push origin main
```

<!-- IMAGE: Terminal showing the sync sequence output: git checkout main, git fetch upstream (with "From github.com:..." line), git merge upstream/main ("Already up to date."), git push origin main ("Everything up-to-date"). Target path: images/sync-upstream-output.png -->

> [!TIP]
> This three-step sync (fetch, merge, push) is something you will do
> every time before starting any new piece of work. Build the habit now.

---
## Step 3: Check your current branch

A branch is a separate version of the repo where you can make changes
safely without affecting the main codebase. Think of it as a draft.
You write your changes in the draft, and only once they are reviewed
and approved do they get added to the main version.

Check what branch you are on:

```bash
git branch
```

What you should see:

```
* main
```

The `*` shows your current branch. You should never make changes
directly on `main`. Always create a new branch for your work.

---
## Step 4: Create a new branch

Before you create the branch, a quick note on naming. Branch names
follow a convention: a short prefix describing the type of change,
a forward slash, then a brief description using hyphens. Like this:

```
type/short-description
```

The prefixes you will use most often:

| Prefix | When to use it |
|---|---|
| `feat/` | Adding something new |
| `fix/` | Fixing a bug or error |
| `docs/` | Documentation changes |
| `chore/` | Maintenance, config, or housekeeping |

For this change -- adding your name to a list -- `docs/` fits. But
since this is your very first branch and it is just about you, a
plain descriptive name like `add-my-name` is also fine and clear.

Create the branch:

```bash
git checkout -b add-my-name
```

What you should see:

```
Switched to a new branch 'add-my-name'
```

What it means: Git created a new branch called `add-my-name` and
switched you to it. Any changes you make now are isolated to this
branch. They will not touch `main` at all.

Confirm with:

```bash
git branch
```

What you should see:

```
* add-my-name
  main
```

The `*` is now on `add-my-name`. You are ready to make changes.

> [!TIP]
> Branch names should be short and descriptive. Use hyphens instead of
> spaces. `add-my-name` is good. `my new branch` will cause errors.

---
## Step 5: Add yourself to CONTRIBUTORS.md

Open `CONTRIBUTORS.md` in a text editor:

### Windows (Git Bash)

```bash
notepad CONTRIBUTORS.md
```

<!-- IMAGE: CONTRIBUTORS.md open in Notepad on Windows. Target path: images/05-open-contributors-windows.png -->

### macOS

```bash
open -e CONTRIBUTORS.md
```

<!-- IMAGE: CONTRIBUTORS.md open in TextEdit on macOS. Target path: images/05-open-contributors-macos.png -->

### Linux

```bash
nano CONTRIBUTORS.md
```

<!-- IMAGE: CONTRIBUTORS.md open in nano in the Linux terminal. Target path: images/05-open-contributors-linux.png -->

You will see a short list with one entry already in it. Add your name
at the bottom, using the same format:

```
- [Your Name](https://github.com/your-username)
```

Replace `Your Name` with your display name and `your-username` with
your actual GitHub username. For example:

```
- [Jane Doe](https://github.com/janedoe)
```

Save the file.

<!-- IMAGE: CONTRIBUTORS.md open in a text editor. The existing Codetopia Community entry is visible and a new line has been added at the bottom in the format "- [Jane Doe](https://github.com/janedoe)". Target path: images/contributors-md-edit.png -->

> [!TIP]
> Only add your own line. Do not change anyone else's entry or any
> other part of the file.

---
## Step 6: Stage and commit your change

Check the status to see what Git has noticed:

```bash
git status
```

What you should see:

```
Changes not staged for commit:
  modified: CONTRIBUTORS.md
```

Stage the file:

```bash
git add CONTRIBUTORS.md
```

Before you commit, a quick note on commit messages. Codetopia
Community follows a standard called Conventional Commits. The format
is:

```
type: short description
```

The description should be lowercase and say what the change does, not
what you did. The types you will use most often:

| Type | When to use it |
|---|---|
| `feat` | Adding something new |
| `fix` | Fixing a bug or error |
| `docs` | Documentation changes |
| `chore` | Maintenance, config, or housekeeping |

For a deeper look at commit conventions and branch naming, see the
[Commit Messages and Branch Naming](https://community.codetopia.org/how-tos/git-and-github/commit-messages-and-branch-naming)
guide in the community how-tos.

Now commit your change. Replace `your-github-username` with your actual GitHub username before running this:

```bash
git commit -m "docs: add your-github-username to contributors"
```

What you should see:

```
[add-my-name abc1234] docs: add your-github-username to contributors
 1 file changed, 1 insertion(+)
```

Your change is saved locally on your branch. Next, you send it to
GitHub.

> [!TIP]
> Write your commit message in lowercase. Describe what the change
> does, not what you did. "docs: add janedoe to contributors" is good.
> "I added my name to the file" is not.

---
## Step 7: Push your branch to your fork

Pushing means sending your local commits up to GitHub so they are
visible online.

```bash
git push origin add-my-name
```

Remember from the previous guide: `origin` is your fork on GitHub.
You are pushing the `add-my-name` branch up to your fork.

What you should see:

```
Enumerating objects...
Counting objects...
To github.com:your-username/open-source-practice.git
 * [new branch]      add-my-name -> add-my-name
```

Your branch is now on GitHub. The original repo (`upstream`) has not
been touched. The change is on your fork only, waiting to be reviewed.

> [!TIP]
> If you get a "Permission denied" error, your SSH connection is not
> working. Go back to the previous guide and check that your SSH key
> is added to GitHub correctly.

---
## Step 8: Open a pull request

Go to your fork on GitHub:

```
https://github.com/your-username/open-source-practice
```

What you should see: a yellow banner at the top saying something like:

```
add-my-name had recent pushes. Compare and pull request
```

<!-- IMAGE: A GitHub fork page showing the yellow "Compare & pull request" banner appearing at the top after a recent push. Target path: images/compare-pull-request-banner.png -->

Click **Compare and pull request**.

You will see a form. Fill it in:

**Title**

```
docs: add janedoe to contributors
```

Replace `janedoe` with your username.

**Description**

One or two sentences saying what you did. For example:

```
Adds my name to CONTRIBUTORS.md as part of the onboarding exercise.
```

<!-- IMAGE: The open pull request form on GitHub. The title field is filled in and the description field has a short explanation. The "Create pull request" button is visible at the bottom. Target path: images/pr-form-filled.png -->

Click **Create pull request**.

What you should see: your PR is now open on the original repo, with
your title, description, and your change listed below.

<!-- IMAGE: An open pull request page on GitHub showing the PR title, description, the "Open" badge, and the files changed section below. Target path: images/pr-open-page.png -->

You have officially proposed your changes to the Codetopia Community
maintainers. Now you wait. A maintainer will review your PR and either
merge it, approve it, or ask you to fix something.

> [!TIP]
> Do not close your PR after submitting it. If a reviewer asks for
> changes, make them on the same branch (`add-my-name`), commit, and
> push again. Your PR updates automatically every time you push to
> that branch.

---
## Quick reference

| Term | What it means |
|---|---|
| Branch | A separate version of the repo for making changes safely |
| `git checkout -b name` | Create and switch to a new branch |
| `git push origin branch` | Push your branch to your fork on GitHub |
| Pull request | A proposal to merge your changes into the original repo |
| `type/description` | Branch naming convention (e.g. `fix/typo-in-about`) |
| `type: description` | Commit message convention (e.g. `fix: correct typo`) |

---
## Stuck?

**`git push` is rejected, or says the remote has work you do not have.**
Your fork has moved on since you branched. Go back to step 2 and sync
with upstream, then push again.

**Git asks for a username and password when you push.**
Your repo is using HTTPS rather than SSH. Run `git remote -v`. If the
address starts with `https://`, re-clone using the `git@github.com:`
address from guide 04.

**`nothing to commit, working tree clean` after you edited the file.**
The change was never saved. Go back to the editor, save, and check
`git status` again. In `nano`, save with `Ctrl+O`, Enter, then `Ctrl+X`.

**There is no "Compare and pull request" banner on your fork.**
Refresh the page. If it still is not there, open the **Branches** tab,
find your branch, and click **New pull request** next to it.

**You cannot find `CONTRIBUTORS.md`.**
Run `pwd`. You must be inside
`~/codetopia-community/open-source-practice`, not the folder above it.

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

Next, you get to see the other side of a pull request: reviewing
someone else's.

🔗 [Reviewing a Pull Request](./06-reviewing-a-pull-request.md)
