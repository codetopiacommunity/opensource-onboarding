---
Guide 04 of 12

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
## One rule before you go further: never commit secrets

Everything you commit becomes part of your project's permanent history.
That is the whole point of Git, and it is also the one way to genuinely
hurt yourself with it.

A **secret** is anything that proves you are you, or that unlocks
something. Passwords. API keys, which are long random-looking strings
that let a program use a paid service on your behalf. Access tokens.
Private SSH keys. Bank or payment details. Someone else's personal
information.

**Never put any of those in a file you commit.**

Here is why it matters more than it first appears. Deleting a secret
later does not remove it. Git keeps every version of every file
forever, so the secret is still sitting in the history where anyone can
read it. And once you have pushed to GitHub, it is public: there are
programs that do nothing but scan public repositories for keys, and
they find them within minutes.

> [!IMPORTANT]
> If you ever do commit a secret, deleting it in a new commit is not
> enough. Treat it as compromised. Go to whatever service it belongs
> to and cancel it, then create a new one. Do this first, before
> tidying up the repository. Everyone senior has done this once.

### How to keep a secret out by accident-proofing it

Sometimes a project genuinely needs a file full of passwords to run on
your machine. The answer is to keep the file and tell Git to ignore it.

Create a file called `.gitignore` in the project folder. The leading
dot is part of the name. Inside, list the things Git should pretend it
cannot see, one per line:

```
.env
secrets.txt
```

Git will now leave those files alone: they will not appear in
`git status`, and `git add` will skip them. The `.gitignore` file
itself does get committed, so everyone working on the project shares
the same list.

> [!NOTE]
> `.env` is the name most projects use for the file holding their
> secrets. If you see one, it should almost always be in `.gitignore`.
> You will not need this in the practice repo, but you will meet it in
> real projects, and now you will know what it is.

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

Think you have broken something? You have not, and
[Fixing Mistakes](../FIXING-MISTAKES.md) shows you how to undo it.

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

Next, you create a GitHub account, push your work online, and the rest
of the world can see it for the first time.

🔗 [GitHub Account and SSH](./04-github-account-and-ssh.md)
