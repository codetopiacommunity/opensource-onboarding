# Your First Commit

Git is installed and knows who you are. Time to actually use it.

In this guide you make your first commit. A commit is a saved snapshot
of your work, and it is the basic unit of everything in open source.
Every contribution you will ever make, to any project, is built out of
commits. By the end of this guide you will have made one, seen it in
the history with your own name on it, and understood every step that
got it there.

---
## What you will do in this guide

- Create a practice folder and initialize Git in it
- Create a file and check what Git thinks of it
- Stage the file
- Make your first commit and see it in the history

---
## Step 1: Go to your Codetopia Community folder

You created this folder in the first guide. Go back into it:

```bash
cd ~/codetopia-community
```

What you should see: your prompt changes to show you are inside the
folder:

```
yourname@computer:~/codetopia-community$
```

> [!TIP]
> If you get "No such file or directory," you may have named the
> folder differently earlier. Run `ls ~` to see all folders in your
> home directory and find the right name.

---
## Step 2: Create a practice folder

Create a small folder to practice Git in:

```bash
mkdir practice
cd practice
pwd
```

What you should see:

```
/home/yourname/codetopia-community/practice
```

---
## Step 3: Initialize Git

This tells Git to start tracking everything inside this folder.

```bash
git init
```

What you should see:

```
Initialized empty Git repository in /home/yourname/codetopia-community/practice/.git/
```

What it means: Git created a hidden folder called `.git` inside your
practice folder. That folder is where Git stores the full history of
your changes. You will never need to touch it directly.

> [!TIP]
> You only run `git init` once per project. If you run it again by
> mistake, nothing breaks, but you do not need to.

---
## Step 4: Create a file

Now create a simple text file to work with:

```bash
echo "Hello, Git!" > hello.txt
```

What you should see: nothing. The file was created silently.

Confirm it exists:

```bash
ls
```

What you should see:

```
hello.txt
```

What it means: `echo` prints text, and `>` sends that text into a file.
You just created a file from the terminal without opening any editor.

---
## Step 5: Check the status

This is one of the most useful Git commands. It tells you what Git is
aware of and what state your files are in.

```bash
git status
```

What you should see:

```
Untracked files:
  hello.txt
```

What it means: Git can see `hello.txt` exists but is not tracking it
yet. It is Git saying "I see this file, but you have not told me to
care about it."

> [!TIP]
> Run `git status` often. It is your way of asking Git "what is going
> on right now?" You can never break anything by running it.

---
## Step 6: Stage the file

Staging means telling Git which changes you want to include in your
next save. Think of it as putting items into a box before sealing it.

```bash
git add hello.txt
```

What you should see: nothing. Silence means it worked.

Now run `git status` again:

```bash
git status
```

What you should see:

```
Changes to be committed:
  new file: hello.txt
```

What it means: `hello.txt` is now staged. It is in the box, ready to be
saved.

> [!TIP]
> You can stage all changed files at once with `git add .`, the dot
> means "everything in this folder." For now, practice staging files
> one at a time so you understand what you are saving.

---
## Step 7: Make your first commit

A commit is the actual save. You seal the box, label it, and Git
stores it permanently in the history.

```bash
git commit -m "my first commit"
```

What you should see:

```
[main (root-commit) abc1234] my first commit
 1 file changed, 1 insertion(+)
 create mode 100644 hello.txt
```

What it means: your change is saved. The `-m` flag lets you attach a
message to the commit. Always write a short, clear message describing
what you changed and why.

Now see your commit in the history:

```bash
git log
```

What you should see:

```
commit abc1234...
Author: Your Name <your@email.com>
Date:   Mon Jan 01 00:00:00 2024

    my first commit
```

<!-- IMAGE: Terminal showing git log output with one commit entry, author name, date, and commit message visible. Target path: images/git-log-output.png -->

That is your work. Saved. Tracked. Yours. Every commit you ever make
will show up here.

> [!TIP]
> Press `q` to exit the `git log` view and return to your prompt.

---
## Quick reference: Git commands you learned

| Command | What it does |
|---|---|
| `git init` | Start tracking a folder with Git |
| `git status` | See what Git is tracking |
| `git add filename` | Stage a file for commit |
| `git add .` | Stage all changed files |
| `git commit -m "message"` | Save your staged changes |
| `git log` | See your commit history |

---
## Stuck?

**`fatal: not a git repository`.**
You are not inside the folder you ran `git init` in. Run `pwd` to check
where you are, `cd ~/codetopia-community/practice` to get back, and
`ls -a` to confirm a `.git` folder is listed.

**`git commit` opened a full screen editor you cannot escape.**
You left off the `-m "message"` part, so Git opened an editor to ask
for one. Press `Esc`, then type `:q!` and press Enter. Then run the
commit again with `-m "my first commit"`.

**Git says `Author identity unknown` or asks who you are.**
You skipped step 2 of guide 02. Set your name and email, then commit
again.

**`git log` will not give you your prompt back.**
Press `q` to quit. Git shows long output in a viewer you exit with `q`.

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

Next, you create a GitHub account, push your work online, and the rest
of the world can see it for the first time.

🔗 [GitHub Account and SSH](./04-github-account-and-ssh.md)
