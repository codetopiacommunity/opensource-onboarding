# Day 01 — Meet Your Terminal

Hey, welcome to the Codetopia Community Open Source Onboarding. 👋

This is not a course. No videos. No long theory.

You will be doing things from day one — real things that real developers do every day.

By the end of this week, you will have made your first open source contribution. For real.

But today we start at the very beginning.

---

## What You Will Do Today

- Find and open your terminal
- Understand what a prompt is
- Learn to navigate your computer using only the terminal
- Know where you are on your machine at any point

That is it. Just the terminal today. Small win, big foundation.

---

## Step 1 — Open Your Terminal

The terminal is a text-based way to talk to your computer. Instead of clicking folders and icons, you type commands and your computer responds. It sounds scary. It is not.

Find yours based on your OS:

**Windows**
Search for **Git Bash** in your Start menu. If you do not have it, download Git from https://git-scm.com/downloads and install it. Git Bash comes with it. Use Git Bash for everything in this bootcamp — not Command Prompt, not PowerShell.

**Mac**
Press `Cmd + Space`, type **Terminal**, hit Enter.

**Linux**
Press `Ctrl + Alt + T` or search for **Terminal** in your apps.

Once it opens, you will see something like this:

```
yourname@computer:~$
```

That line is called the **prompt**. It is the terminal waiting for you to type something. It will look slightly different depending on your OS and setup, but it always ends with a `$` or `%` symbol.

> Hint: The prompt is not something you type. It is just the terminal saying "I am ready." You type your commands after the `$` symbol.

---

## Step 2 — Where Are You?

When you are in the terminal, you are always inside a folder on your computer — just like being inside a folder in your file explorer. The terminal does not show you this visually, so you have to ask.

Type this exactly and hit Enter:

```bash
pwd
```

What you should see:

```
/home/yourname
```

or on Mac:

```
/Users/yourname
```

or on Windows (Git Bash):

```
/c/Users/yourname
```

What it means: `pwd` stands for "print working directory." It is telling you the full path of the folder you are currently inside. This is your **home folder** — the starting point every time you open the terminal.

> Hint: If nothing shows up or you see an error, make sure you typed `pwd` in lowercase. Commands are case-sensitive.

---

## Step 3 — Look Around

Now let us see what is inside the folder you are in.

Type:

```bash
ls
```

What you should see: a list of files and folders inside your current location. It will look something like:

```
Desktop  Documents  Downloads  Music  Pictures
```

What it means: `ls` stands for "list." It shows you everything inside your current folder — the same as opening your file explorer and looking inside a folder.

> Hint: If you see nothing, the folder is just empty. That is fine. Try running `ls` on your Desktop in the next step and you will see more.

---

## Step 4 — Move Into a Folder

`cd` stands for "change directory." It is how you move into a folder.

Let us move into your Desktop:

```bash
cd Desktop
```

What you should see: your prompt changes slightly. On most systems it will now show Desktop in the path:

```
yourname@computer:~/Desktop$
```

What it means: you are now inside the Desktop folder. Think of it as double-clicking the Desktop folder in your file explorer.

Now run `ls` again:

```bash
ls
```

You will see the files and folders sitting on your Desktop.

> Hint: If you get "No such file or directory", the folder name might be spelled differently. Folder names are case-sensitive. Try `cd desktop` in lowercase or run `ls` first to see the exact folder names available.

---

## Step 5 — Go Back

To go back one level — out of the folder you are currently in:

```bash
cd ..
```

What you should see: your prompt goes back to the previous path.

What it means: two dots (`..`) always means "go up one level." It does not matter where you are, `cd ..` takes you one step back.

Run `pwd` to confirm you moved back.

> Hint: You can chain this to go up multiple levels. `cd ../..` goes up two levels at once.

---

## Step 6 — Go Home From Anywhere

No matter where you are in the terminal, this command takes you straight back to your home folder:

```bash
cd ~
```

What you should see: your prompt goes back to showing just `~`.

What it means: the tilde symbol (`~`) is shorthand for your home folder. You will use this a lot.

> Hint: If you ever feel lost in the terminal, run `cd ~` and you are back to the beginning.

---

## Step 7 — Create a Folder for This Onboarding

Let us make a folder where all your work will live during this onboarding. First go home:

```bash
cd ~
```

Now create a new folder called `codetopia`:

```bash
mkdir codetopia-community
```

What you should see: nothing. No output means it worked.

What it means: `mkdir` stands for "make directory." It creates a new folder. The lack of output is normal — the terminal only speaks up when something goes wrong.

> Hint: If you see "File exists", a folder with that name already exists. That is fine, just move into it in the next step.

Now move into it:

```bash
cd codetopia-community
```

Run `pwd` to confirm:

```bash
pwd
```

You should see something like `/home/yourname/codetopia-community`. This is your workspace for the rest of this onboarding. Everything lives here.

---

## Quick Reference — Commands You Learned Today

| Command | What it does |
|---|---|
| `pwd` | Show where you are |
| `ls` | List files and folders here |
| `cd foldername` | Move into a folder |
| `cd ..` | Go back one level |
| `cd ~` | Go back to home from anywhere |
| `mkdir foldername` | Create a new folder |

---

## Done? Share Your Update

Drop a message in the WhatsApp group:

```
Day 01 ✅
- OS: [Windows / Mac / Linux]
- Stuck on: [anything blocking you, or "nothing"]
- Next: Day 02
```

If you are stuck on anything, drop it in the group immediately. Do not sit on a blocker alone.

---

## What Is Next

Tomorrow we install Git and make your first commit. The real stuff begins.

See you on [Day 02](./day-02.md).