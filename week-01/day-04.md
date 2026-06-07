# Day 04 — Your First Pull Request

Welcome back. 👋

Yesterday you forked this repo and cloned it to your machine. Today you make a real change and submit it for review.

A Pull Request (PR) is how you propose changes to a repo. Instead of directly editing the original, you make changes on your fork and say "hey, I made some changes — can you review and merge them?" The repo maintainer reviews your changes, gives feedback, and either merges them or asks you to fix something first.

This is how all open source contribution works. Today you do it for the first time.

---

## What You Will Do Today

- Create a new branch for your change
- Make a real change to the repo
- Push your change to GitHub
- Open a Pull Request

---

## Step 1 — Go to Your Cloned Repo

Open your terminal and navigate to the repo you cloned yesterday:

```bash
cd ~/codetopia-community/open-source-get-started
```

What you should see: your prompt changes to show you are inside the repo folder.

Confirm you are in the right place:

```bash
ls
```

You should see the repo files listed.

> Hint: If you get "No such file or directory", you may have cloned the repo into a different location. Run `ls ~/codetopia-community` to find it.

---

## Step 2 — Check Your Current Branch

A branch is a separate version of the repo where you can make changes safely without affecting the main codebase. Think of it as a draft. You write your changes in the draft, and only when they are reviewed and approved do they get added to the main version.

Check what branch you are currently on:

```bash
git branch
```

What you should see:

```
* main
```

What it means: you are on the `main` branch. The `*` shows your current branch. You should never make changes directly on `main`. Always create a new branch for your work.

---

## Step 3 — Create a New Branch

Create a new branch for your change. Name it after what you are doing:

```bash
git checkout -b add-my-profile
```

What you should see:

```
Switched to a new branch 'add-my-profile'
```

What it means: Git created a new branch called `add-my-profile` and switched you to it. Any changes you make now are isolated to this branch and will not affect `main`.

Run `git branch` again to confirm:

```bash
git branch
```

What you should see:

```
* add-my-profile
  main
```

The `*` is now on `add-my-profile`. You are ready to make changes.

> Hint: Branch names should be short and descriptive. Use hyphens instead of spaces. `add-my-profile` is good. `my new branch` will cause errors.

---

## Step 4 — Make Your Change

Go into the `profiles` folder:

```bash
cd profiles
```

List what is inside:

```bash
ls
```

You will see a file called `template.mdx`. This is the template you will use to create your own profile.

Copy the template and rename it with your GitHub username:

```bash
cp template.mdx your-github-username.mdx
```

Replace `your-github-username` with your actual GitHub username. For example if your username is `johndoe`:

```bash
cp template.mdx johndoe.mdx
```

Now open your new file in a text editor. If you do not have a code editor installed, use this command to open it with the default text editor on your system:

**Windows (Git Bash)**
```bash
notepad johndoe.mdx
```

**Mac**
```bash
open -e johndoe.mdx
```

**Linux**
```bash
nano johndoe.mdx
```

Fill in your details following the template. Save the file when you are done.

> Hint: Do not delete the template file. Only edit your own copy.

---

## Step 5 — Stage and Commit Your Change

Go back to the root of the repo:

```bash
cd ..
```

Check the status to see your change:

```bash
git status
```

What you should see:

```
Changes not staged for commit:
  new file: profiles/johndoe.mdx
```

Stage your file:

```bash
git add profiles/your-github-username.mdx
```

Commit it with a clear message:

```bash
git commit -m "add johndoe profile"
```

Replace `johndoe` with your actual GitHub username.

What you should see:

```
[add-my-profile abc1234] add johndoe profile
 1 file changed, x insertions(+)
```

What it means: your change is saved locally on your branch. Now you need to push it to GitHub.

> Hint: Write your commit message in lowercase and keep it short. Describe what the change does, not what you did. "add johndoe profile" is good. "I added my profile file today" is not.

---

## Step 6 — Push Your Branch to GitHub

Pushing means sending your local commits up to GitHub so they are visible online.

```bash
git push origin add-my-profile
```

What you should see:

```
Enumerating objects...
Counting objects...
To github.com:your-username/open-source-get-started.git
 * [new branch]      add-my-profile -> add-my-profile
```

What it means: your branch is now on GitHub. `origin` refers to your fork on GitHub. You pushed the `add-my-profile` branch up to it.

> Hint: If you get a "Permission denied" error, your SSH connection is not working. Go back to Day 03 Step 2 and check that your SSH key is added to GitHub correctly.

---

## Step 7 — Open a Pull Request

Now go to your fork on GitHub:

```
https://github.com/your-username/open-source-get-started
```

What you should see: a yellow banner at the top saying something like:

```
add-my-profile had recent pushes — Compare and pull request
```

Click **Compare and pull request**.

You will see a form with two fields:

**Title**
Write a clear title for your PR. For example:

```
Add johndoe profile
```

**Description**
The PR template will already be filled in for you. Fill in each section honestly. Do not leave it blank.

When you are done, click **Create pull request**.

What you should see: your PR is now open. It has a number, your title, your description, and your changes listed below.

What it means: you have officially proposed your changes. Now you wait for a review. Seth or a reviewer will look at your PR and either approve it, request changes, or leave comments.

> Hint: Do not close your PR after submitting it. If changes are requested, make them on the same branch, commit, and push again. Your PR will update automatically.

---

## Quick Reference — What You Learned Today

| Term | What it means |
|---|---|
| Branch | A separate version of the repo for making changes safely |
| `git checkout -b name` | Create and switch to a new branch |
| `git push origin branch` | Push your branch to GitHub |
| Pull Request | A proposal to merge your changes into the main repo |

---

## Done? Share Your Update

Drop a message in the WhatsApp group with your PR link:

```
Day 04 ✅
- PR: [link to your pull request]
- Stuck on: [anything blocking you, or "nothing"]
- Next: Day 05
```

---

## What Is Next

Tomorrow you review someone else's PR and leave your first code review.

See you on Day 05.