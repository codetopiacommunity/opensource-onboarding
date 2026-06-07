# Day 02 — Install Git and Make Your First Commit

Welcome back. 👋

Yesterday you got comfortable moving around in the terminal. Today you meet Git.

Git is a tool that tracks changes in your files over time. Think of it as a save system for your work. Every time you make a meaningful change, you save it with Git. You can always go back to any previous save. Every professional developer uses Git every single day.

Let us get it set up.

---

## What You Will Do Today

- Install Git on your machine
- Tell Git who you are
- Create a practice folder and initialise Git in it
- Make your first commit

---

## Step 1 — Check if Git is Already Installed

Before installing, check if Git is already on your machine. Open your terminal and type:

```bash
git --version
```

What you should see:

```
git version 2.x.x
```

What it means: Git is already installed. Skip to Step 2.

If you see something like `command not found`, Git is not installed yet. Follow the instructions below for your OS.

**Windows**
Download Git from https://git-scm.com/downloads. Run the installer and use all the default options. After it finishes, close Git Bash and open it again. Run `git --version` to confirm.

**Mac**
Run this in your terminal:

```bash
xcode-select --install
```

A popup will appear asking you to install developer tools. Click Install and wait for it to finish. It may take a few minutes.

**Linux**
Run this in your terminal:

```bash
sudo apt install git
```

Your terminal will ask for your password. Type it and hit Enter. You will not see the characters as you type — that is normal.

> Hint: After installing on any OS, run `git --version` again to confirm it worked before moving on.

---

## Step 2 — Tell Git Who You Are

Git needs to know your name and email so it can attach your identity to every change you make. This is how open source projects know who contributed what.

Run this command with your actual name:

```bash
git config --global user.name "Your Name"
```

What you should see: nothing. No output means it worked.

Now run this with your actual email:

```bash
git config --global user.email "your@email.com"
```

Now confirm both were saved:

```bash
git config --global --list
```

What you should see:

```
user.name=Your Name
user.email=your@email.com
```

What it means: Git has saved your identity. Every commit you make from now on will have your name and email on it.

> Hint: Use the same email you will use for your GitHub account. This is important later when your commits need to be linked to your GitHub profile.

---

## Step 3 — Go to Your Codetopia Community Folder

You created this folder on Day 01. Go back into it:

```bash
cd ~/codetopia-community
```

What you should see: your prompt changes to show you are inside the codetopia folder:

```
yourname@computer:~/codetopia-community$
```

What it means: you are in your workspace. This is where all your work during this onboarding will live.

> Hint: If you get "No such file or directory", you may have named the folder differently on Day 01. Run `ls ~` to see all folders in your home directory and find the right name.

---

## Step 4 — Create a Practice Folder

Create a small folder to practice Git in:

```bash
mkdir practice
```

Move into it:

```bash
cd practice
```

Run `pwd` to confirm where you are:

```bash
pwd
```

What you should see:

```
/home/yourname/codetopia-community/practice
```

---

## Step 5 — Initialise Git

This tells Git to start tracking everything inside this folder.

```bash
git init
```

What you should see:

```
Initialized empty Git repository in /home/yourname/codetopia/practice/.git/
```

What it means: Git has created a hidden folder called `.git` inside your practice folder. That folder is where Git stores all the history of your changes. You will never need to touch it directly.

> Hint: You only ever run `git init` once per project. If you run it again by mistake nothing breaks, but you do not need to.

---

## Step 6 — Create a File

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

What it means: `echo` prints text, and `>` sends that text into a file. You just created a file from the terminal without opening any editor.

---

## Step 7 — Check the Status

This is one of the most important Git commands. It tells you what Git is aware of and what state your files are in.

```bash
git status
```

What you should see:

```
Untracked files:
  hello.txt
```

What it means: Git can see `hello.txt` exists but is not tracking it yet. It is like Git saying "I see this file but you have not told me to care about it."

> Hint: Run `git status` often. It is your way of asking Git "what is going on right now?" You can never break anything by running it.

---

## Step 8 — Stage the File

Staging means telling Git which changes you want to include in your next save. Think of it as putting items into a box before sealing it.

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

What it means: `hello.txt` is now staged. It is in the box, ready to be saved.

> Hint: You can stage all changed files at once with `git add .` — the dot means "everything in this folder." For now, practice staging files one by one so you understand what you are saving.

---

## Step 9 — Make Your First Commit

A commit is the actual save. You seal the box, label it, and Git stores it permanently in the history.

```bash
git commit -m "my first commit"
```

What you should see:

```
[main (root-commit) abc1234] my first commit
 1 file changed, 1 insertion(+)
 create mode 100644 hello.txt
```

What it means: your change is saved. The `-m` flag lets you attach a message to the commit. Always write a short, clear message that describes what you changed and why.

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

What it means: that is your work. Saved. Tracked. Yours. Every commit you ever make will show up here.

> Hint: Press `q` to exit the git log view and return to your prompt.

---

## Quick Reference — Git Commands You Learned Today

| Command | What it does |
|---|---|
| `git --version` | Check if Git is installed |
| `git config --global user.name "Name"` | Set your Git name |
| `git config --global user.email "email"` | Set your Git email |
| `git init` | Start tracking a folder with Git |
| `git status` | See what Git is tracking |
| `git add filename` | Stage a file for commit |
| `git add .` | Stage all changed files |
| `git commit -m "message"` | Save your staged changes |
| `git log` | See your commit history |

---

## Done? Share Your Update

Drop a message in the WhatsApp group:

```
Day 02 ✅
- OS: [Windows / Mac / Linux]
- Stuck on: [anything blocking you, or "nothing"]
- Next: Day 03
```

---

## What Is Next

Tomorrow you create a GitHub account, push your work online, and the rest of the world can see it for the first time.

See you on Day 03.