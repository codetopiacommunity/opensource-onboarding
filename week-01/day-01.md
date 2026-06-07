# Day 01 — Meet Your Terminal

Hey, welcome to the Codetopia Community Open Source Bootcamp. 👋

This is not a course. No videos. No long theory.

You will be **doing things** from day one — real things that real developers do every day.

By the end of this week, you'll have made your first open source contribution. For real.

But today? We start at the very beginning.

---

## What You'll Do Today

- Find and open your terminal
- Learn to navigate your computer using only the terminal
- Understand where you are on your machine at any point

That's it. Just the terminal today. Small win, big foundation.

---

## Step 1 — Open Your Terminal

The terminal is a text-based way to talk to your computer. Instead of clicking folders, you type commands. It sounds scary — it isn't.

Find yours based on your OS:

**Windows**
Search for **Git Bash** in your Start menu. If you don't have it, download Git from https://git-scm.com/downloads and install it. Git Bash comes with it. Use Git Bash for everything in this bootcamp — not Command Prompt, not PowerShell.

**Mac**
Press `Cmd + Space`, type **Terminal**, hit Enter.

**Linux**
Press `Ctrl + Alt + T` or search for **Terminal** in your apps.

Once it's open, you'll see a blinking cursor. That's your starting point.

---

## Step 2 — Where Are You?

The first thing to know: **you are always somewhere** in your computer when you're in the terminal — just like being inside a folder.

Type this and hit Enter:

```bash
pwd
```

`pwd` means "print working directory." It shows you where you are right now.

You'll see something like:
- `/home/yourname` on Linux
- `/Users/yourname` on Mac
- `/c/Users/yourname` on Windows (Git Bash)

That's your **home folder**. This is where you start every time.

---

## Step 3 — Look Around

Now let's see what's inside the folder you're in.

Type:

```bash
ls
```

You'll see a list of files and folders — same as opening your file explorer, but in text.

---

## Step 4 — Move Into a Folder

`cd` means "change directory." It's how you move into a folder.

Try moving into your Desktop:

```bash
cd Desktop
```

Now run `pwd` again. See how the path changed? You moved.

Run `ls` again. You'll see what's on your Desktop.

---

## Step 5 — Go Back

To go back one level (out of the folder you're in):

```bash
cd ..
```

Two dots means "go up one level." Run `pwd` to confirm you moved back.

---

## Step 6 — Create a Folder for This Bootcamp

Let's make a folder where all your bootcamp work will live. First go to a place that makes sense — your Desktop or home folder.

To go home from anywhere:

```bash
cd ~
```

Now create a new folder:

```bash
mkdir codetopia-community
```

Move into it:

```bash
cd codetopia-community
```

Run `pwd`. You should be inside your new `codetopia-community` folder. This is where everything will live from now on.

---

## Quick Reference — Commands You Learned Today

| Command | What it does |
|---|---|
| `pwd` | Show where you are |
| `ls` | List files and folders here |
| `cd foldername` | Move into a folder |
| `cd ..` | Go back one level |
| `cd ~` | Go back to home |
| `mkdir foldername` | Create a new folder |

---

## Done? Share Your Update

Drop a message in the WhatsApp group with this format:

```
Day 01 ✅
- OS: [Windows / Mac / Linux]
- Stuck on: [anything blocking you, or "nothing"]
- Next: Day 02
```

If you're stuck on anything — **don't sit on it alone**. Drop it in the group immediately.

---

## What's Next

we install Git and set it up. The real stuff begins.

See you on Day 02.