# Keeping Your Fork in Sync

You have now used `origin` and `upstream` throughout the previous
guides. This final guide reinforces why that sync habit matters and
what happens when you skip it. It also covers the last practical skill
you need: what to do when a reviewer asks you to update a pull request
you already submitted.

---
## What you will do in this guide

- Understand what happens to your fork over time if you do not sync
- Run the full sync process and understand each step
- Learn how to respond to reviewer feedback without opening a new
  pull request

---
## Why your fork falls behind

When you forked the practice repo, your fork was a perfect copy of
the original at that moment. But the original repo keeps moving.
Other contributors merge pull requests. Maintainers make changes.
New commits land on `upstream/main` every day.

Your fork does not update itself. It just sits there, frozen at the
state it was in when you forked. The longer you go without syncing,
the further behind your fork falls.

This causes a specific problem: when you branch off an outdated
`main` and then submit a pull request, your PR might conflict with
changes that were already merged into the original. Those conflicts
have nothing to do with your actual work. They are just noise created
by not syncing first. Reviewers have to deal with them, and you have
to fix them.

The solution is to sync before you start any new piece of work. You
have been doing this throughout the guides. Here is the full picture
of what that process actually does.

---
## The three places your code lives

When you work on an open source project with a fork, there are three
separate copies of the code:

1. The original repo on GitHub (`upstream`)
2. Your fork on GitHub (`origin`)
3. Your local machine (your working directory)

All three need to be kept in sync. Syncing `upstream` into your local
machine is not enough on its own. Your fork on GitHub also needs to be
updated, because your pull requests come from your fork.

---
## The full sync process

Here is the complete sequence, with an explanation for each step:

```bash
git checkout main
```

Switch to your main branch. You always sync into `main`, not into a
feature branch.

```bash
git fetch upstream
```

Download the latest commits from the original repo. This does not
change any of your files yet. It just downloads the new history and
stores it as `upstream/main` so you can inspect or use it.

```bash
git merge upstream/main
```

Apply those downloaded commits to your local `main`. Your files now
match the original repo's `main`.

```bash
git push origin main
```

Push the updated `main` to your fork on GitHub. Now all three copies
are in sync: the original repo, your local machine, and your fork.

Run this sequence every time before you create a new branch. It takes
ten seconds and saves you from dealing with avoidable conflicts.

---
## What if you already have a branch open?

If you already have a branch in progress and the original repo has
moved forward while you were working, you can bring your branch up
to date by rebasing it onto the latest `main` after syncing.

First sync `main` as shown above. Then switch back to your branch:

```bash
git checkout your-branch-name
```

Rebase your branch onto the updated `main`:

```bash
git rebase main
```

What this does: imagine you started your branch when `main` was at
version 5. While you were working, other people merged their changes
and `main` moved forward to version 8. Rebasing takes your commits
and replays them on top of version 8, as if you had started your
branch from there in the first place. Your changes are the same, but
they now sit on top of the latest version of the project.

If there are conflicts during the rebase, Git will stop and ask you
to resolve them the same way you did in the previous guide.

> [!TIP]
> If you are not comfortable with rebase yet, you can also merge
> `main` into your branch: `git merge main`. The result is the same,
> but rebase keeps the history cleaner.

---
## Iterating on feedback

When a reviewer leaves a comment on your pull request asking you to
change something, you do not close the pull request and open a new
one. You make the fix on the same branch you already pushed.

Here is the flow:

1. Read the reviewer's comment and understand exactly what they are
   asking for. If it is not clear, reply on the pull request and ask.

2. Switch to your branch locally:
   ```bash
   git checkout your-branch-name
   ```

3. Make the change they asked for.

4. Stage and commit it:
   ```bash
   git add the-file-you-changed
   git commit -m "fix: address reviewer feedback"
   ```

5. Push to the same branch:
   ```bash
   git push origin your-branch-name
   ```

Your pull request on GitHub updates automatically. The new commit
appears in the pull request timeline. You can then reply to the
reviewer's comment to let them know the fix is in.

> [!TIP]
> Reviewers check pull requests across many projects and many
> contributors. A short reply like "Fixed in the latest commit, let
> me know if it looks good" saves them time and shows you are paying
> attention.

---
## Quick reference

| Command | What it does |
|---|---|
| `git fetch upstream` | Download new commits from the original repo |
| `git merge upstream/main` | Apply them to your local main |
| `git push origin main` | Update your fork to match |
| `git rebase main` | Replay your branch on top of the updated main |

---
## Stuck?

**`upstream does not appear to be a git repository`.**
The upstream remote is missing on this machine. Add it again following
[guide 04, step 6](./04-github-account-and-ssh.md). Check with
`git remote -v`, which should list both `origin` and `upstream`.

**`git merge upstream/main` says `Already up to date`.**
Not a problem. It means nothing new has been merged upstream since you
last synced.

**A conflict appears while syncing or rebasing.**
Resolve it exactly the way you did in
[guide 08](./08-resolving-a-merge-conflict.md). The markers and the fix
are identical, whatever command produced them.

**`git push origin main` is rejected.**
Your fork's `main` has commits your local one does not, usually from
committing directly on `main` earlier. Ask in the Discord before
force pushing, so you do not lose work.

Still stuck, or hit something not listed here? Ask in
<a href="https://github.com/codetopiacommunity/opensource-onboarding/discussions/categories/q-a" target="_blank" rel="noopener noreferrer">GitHub Discussions</a>
using the **Q&A** category. It needs nothing but the GitHub account
this course gives you anyway, and your question turns up in the
community Discord by itself, so there is nowhere else you need to post.
Replies come back on the discussion.

[Getting Help](../HELP.md) explains both, and how to ask so you get a
useful answer quickly.

---
## What's next?

You now have the whole working loop: fork, branch, commit, pull
request, review, conflict, sync. One piece is left, and it is the one
that starts most people's first contribution to a project they have
never touched before. Writing the issue in the first place.

🔗 [Reporting a Good Issue](./10-reporting-a-good-issue.md)
