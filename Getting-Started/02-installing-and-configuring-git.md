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

If you are on Windows, you almost certainly did this already in guide
01 when you installed Git Bash, because Git came bundled with it. Run
`git --version` to confirm and move on to Step 2.

If you somehow do not have it, download Git from
https://git-scm.com/downloads. Run the installer and use the default
options. After it finishes, close Git Bash and open it again. Run
`git --version` to confirm.

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

That is the whole setup. You only do this once per machine, and Git
will remember it from now on.

---
## Quick reference: Git commands you learned

| Command | What it does |
|---|---|
| `git --version` | Check if Git is installed |
| `git config --global user.name "Name"` | Set your Git name |
| `git config --global user.email "email"` | Set your Git email |
| `git config --global --list` | See your saved Git settings |

---
## Stuck?

**You installed Git but `git --version` still is not recognised.**
Close the terminal window completely and open a new one. A terminal
only picks up newly installed programs when it starts.

**On Windows, `git` works nowhere you try it.**
Make sure you are in **Git Bash**, not Command Prompt or PowerShell.
Every command in these guides assumes Git Bash.

**`sudo apt install git` asks for a password and typing does nothing.**
That is deliberate. Linux hides password characters as you type. Type
it anyway and press Enter.

**`git config --global --list` comes back empty.**
The settings did not save. Run both `git config` commands again, and
keep the quotes around your name and email exactly as shown.

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

Git is installed and knows who you are. Next, you put it to work and
make your first commit.

🔗 [Your First Commit](./03-your-first-commit.md)
