# Installing and Configuring Git

You got comfortable moving around in the terminal. Now you meet Git.

Git is a tool that tracks changes in your files over time. Think of it
as a save system for your work. Every time you make a meaningful
change, you save it with Git, and you can always go back to any
previous save. Every professional developer uses Git every single day.

Let us get it set up.

---
## What you will do in this guide

- Install Git on your machine
- Tell Git who you are
- Create a practice folder and initialize Git in it
- Make your first commit

---
## Step 1: Check if Git is already installed

Before installing, check if Git is already on your machine. Open your
terminal and type:

```bash
git --version
```

What you should see:

```
git version 2.x.x
```

What it means: Git is already installed. Skip to Step 2.

If you see something like `command not found`, Git is not installed
yet. Follow the instructions below for your OS.

### Windows

Download Git from https://git-scm.com/downloads. Run the installer and
use the default options. After it finishes, close Git Bash and open it
again. Run `git --version` to confirm.

<!-- IMAGE: The Git for Windows installer open on Windows, showing the default options selected. Target path: images/02-install-git-windows.png -->

### macOS

Run this in your terminal:

```bash
xcode-select --install
```

A popup will appear asking you to install developer tools. Click
Install and wait for it to finish. It may take a few minutes.

<!-- IMAGE: macOS popup dialog asking to install developer tools, with the Install button highlighted. Target path: images/02-install-git-macos.png -->

### Linux

Run this in your terminal:

```bash
sudo apt install git
```

Your terminal will ask for your password. Type it and hit Enter. You
will not see the characters as you type. That is normal.

> [!TIP]
> After installing on any OS, run `git --version` again to confirm it
> worked before moving on.

---
## Step 2: Tell Git who you are

Git needs to know your name and email so it can attach your identity to
every change you make. This is how open source projects know who
contributed what.

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

What it means: Git has saved your identity. Every commit you make from
now on will have your name and email attached to it.

> [!TIP]
> Use the same email you will use for your GitHub account. This
> matters later, when your commits need to be linked to your GitHub
> profile.

---
## Step 3: Go to your Codetopia Community folder

You created this folder in the previous guide. Go back into it:

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
## Step 4: Create a practice folder

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
## Step 5: Initialize Git

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
## Step 6: Create a file

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
## Step 7: Check the status

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
## Step 8: Stage the file

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
## Step 9: Make your first commit

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
## What's next?

Next, you create a GitHub account, push your work online, and the rest
of the world can see it for the first time.

🔗 [GitHub Account and SSH](./03-github-account-and-ssh.md)
