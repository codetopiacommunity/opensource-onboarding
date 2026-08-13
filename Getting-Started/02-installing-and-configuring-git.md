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
## What's next?

Git is installed and knows who you are. Next, you put it to work and
make your first commit.

🔗 [Your First Commit](./03-your-first-commit.md)
