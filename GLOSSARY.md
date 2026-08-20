# Glossary

Every word in these guides that might be new, in one place, in plain
language.

You do not need to read this page start to finish. Come here when you
meet a word you do not know, look it up, and go back to what you were
doing. Nothing here expects you to already know something else.

Words are listed alphabetically.

---

**Backtick**
The character `` ` ``. It sits on the key to the left of the `1` key,
just above Tab on most keyboards. It is not an apostrophe and it is not
a quote mark. Putting three backticks on the line above some text and
three on the line below keeps it looking like computer text when you
post it on GitHub or Discord.

**Branch**
A separate version of a project where you can make changes without
touching the main version. Think of it as a rough draft: you work on
your branch, and only when it is ready does it get combined back in.
Every project has one main branch, usually called `main`, which holds
the version everyone agrees on. Taught in
[guide 05](./Getting-Started/05-your-first-pull-request.md).

**Clone**
To download a complete copy of a repository from GitHub onto your own
computer, so you can work on it there. You clone once per project. The
command is `git clone`. Taught in
[guide 04](./Getting-Started/04-github-account-and-ssh.md).

**Command**
An instruction you type into the terminal and run by pressing Enter,
such as `ls` or `git status`.

**Command line**
Another name for the terminal. See **Terminal**.

**Commit**
A saved snapshot of your changes, with a short message explaining what
you did and why. Commits are the units a project's history is made of.
Making a commit does not send anything to GitHub; that is a separate
step called pushing. Taught in
[guide 03](./Getting-Started/03-your-first-commit.md).

**Contributor**
Anyone who has improved a project, whether once or a hundred times.
There is no application and no approval step. Once your change is
accepted, you are one.

**Directory**
The word computers use for a folder. They mean exactly the same thing.
The terminal says "directory", your desktop says "folder".

**Environment**
The setup a problem happened in: which operating system you are using,
which versions of things you have installed. People ask for it because
the same command can behave differently on different machines.

**Fetch**
To download new changes from GitHub without applying them to your work
yet. It is the safe half of getting up to date: you look first, then
decide. The command is `git fetch`. Taught in
[guide 07](./Getting-Started/07-finding-and-claiming-an-issue.md).

**Fork**
Your own personal copy of somebody else's repository, stored under your
GitHub account. You cannot change other people's projects directly, so
you fork one, change your copy, and then offer your change back. Taught
in [guide 04](./Getting-Started/04-github-account-and-ssh.md).

**Git**
The program that tracks changes to files over time. It runs on your own
computer and works without the internet. Git is not GitHub. Installed
in [guide 02](./Getting-Started/02-installing-and-configuring-git.md).

**Git Bash**
A terminal program for Windows that comes with Git. Windows has other
terminals, but the commands in these guides are written for Git Bash,
so use it. Installed in
[guide 02](./Getting-Started/02-installing-and-configuring-git.md).

**GitHub**
A website that stores repositories online so people can work on them
together. Git is the tool; GitHub is the place. You can use Git without
GitHub, and many people do.

**Home directory**
Your personal folder on your computer, the one holding your Desktop,
Documents and so on. The terminal writes it as `~`, so `cd ~` means
"take me home from wherever I am".

**Issue**
A public note on a project saying something needs attention: a bug, a
confusing instruction, a missing feature. Each one gets a number like
`#42`. Anyone can open one, and doing so is already a contribution.
Taught in
[guide 10](./Getting-Started/10-reporting-a-good-issue.md).

**Label**
A coloured tag a maintainer puts on an issue to sort it, such as `bug`,
`documentation` or `good first issue`. You do not add these yourself.

**Licence** (spelled **license** in American English, and in the
filename)
A file, usually named `LICENSE`, in which the author of a project
states what other people are allowed to do with it. Without one,
copyright's strict default applies and nobody may legally reuse the
work, no matter how public it is. A licence is what makes a project
open source rather than merely visible. Explained in
[guide 00](./Getting-Started/00-what-is-open-source.md).

**Maintainer**
Someone responsible for a project. They review incoming changes and
decide what gets included. Usually a volunteer doing it in their spare
time.

**Markdown**
A simple way of formatting text using ordinary characters. Surrounding
a word with `**` makes it bold, a `#` at the start of a line makes a
heading. GitHub uses it everywhere: issues, pull requests, and every
file in this course ending in `.md`.

**Merge**
To combine changes from one branch into another. When a maintainer
accepts your pull request, they merge it, and your work becomes part of
the project.

**Merge conflict**
What happens when two people change the same lines of the same file and
Git cannot tell which version should win, so it stops and asks you. It
sounds alarming and is not. Nothing is broken and nothing is lost.
Taught in
[guide 08](./Getting-Started/08-resolving-a-merge-conflict.md).

**Open source**
Software whose code is public, so anyone can read it, learn from it,
use it, and help improve it. Explained in
[guide 00](./Getting-Started/00-what-is-open-source.md).

**`origin`**
The name Git gives to your fork on GitHub: the copy you cloned from and
push your work to. It is just a nickname for a web address, so you do
not have to type the whole thing every time. Compare **`upstream`**.
Taught in [guide 04](./Getting-Started/04-github-account-and-ssh.md).

**Path**
The full address of a file or folder on your computer, written as names
separated by slashes, like `~/codetopia-community/practice`. It tells
you exactly where something lives.

**Prompt**
The text the terminal shows at the start of a line while it waits for
you to type, often ending in `$`. Seeing the prompt again means the
last command has finished.

**Pull request** (often shortened to **PR**)
A proposal that says "here are my changes, please include them in the
project." It is where your work gets seen, discussed, and either
accepted or improved. Opening one does not change anything by itself.
Taught in
[guide 05](./Getting-Started/05-your-first-pull-request.md).

**Push**
To send commits from your computer up to GitHub. Until you push, your
work exists only on your machine. The command is `git push`.

**README**
The file a project shows on its front page, explaining what the project
is and how to get started. It is always the first thing to read when
you arrive somewhere new.

**Rebase**
Another way of bringing your branch up to date with the latest changes.
You will meet it in
[guide 09](./Getting-Started/09-keeping-your-fork-in-sync.md). Treat it
as an advanced tool for now.

**Remote**
A named connection to a copy of the project that lives somewhere else,
usually on GitHub. Your two remotes in this course are `origin` and
`upstream`. Run `git remote -v` to see them.

**Repository** (almost always shortened to **repo**, said "REP-oh")
A project as Git stores it: every file, plus the complete history of
every change ever made. Really just a folder that remembers its own
past.

**Reproduce**
To make a problem happen again on purpose, by following the same steps.
"Steps to reproduce" means the list of things someone else can do to
see the problem for themselves. Without it, a problem is very hard to
fix.

**Review**
Reading someone else's proposed changes and giving feedback on them.
Not a test and not a judgement of the person. Taught in
[guide 06](./Getting-Started/06-reviewing-a-pull-request.md).

**SSH key**
A pair of long files on your computer that proves to GitHub you are
you, so you do not type a password every time you push. One half is
public and you paste it into GitHub; the other half is private and you
never share it with anyone. Set up in
[guide 04](./Getting-Started/04-github-account-and-ssh.md).

**Stage** (also **staging area**)
Choosing which changed files go into your next commit. You stage a file
with `git add`. Think of it as putting things into a box before sealing
it: staging fills the box, committing seals it. Taught in
[guide 03](./Getting-Started/03-your-first-commit.md).

**Sync**
To bring your copy of a project up to date with the original, so you
are not building on an old version. Taught in
[guide 09](./Getting-Started/09-keeping-your-fork-in-sync.md).

**Terminal**
A program where you type instructions to your computer instead of
clicking them. Anything you can do by clicking, you can do by typing.
Introduced in
[guide 01](./Getting-Started/01-your-computer-and-the-terminal.md).

**`upstream`**
The name Git gives to the original project you forked from, as opposed
to your own copy. You pull other people's newly merged work from
`upstream`. Compare **`origin`**. Taught in
[guide 04](./Getting-Started/04-github-account-and-ssh.md).

**URL**
A web address: the text in the bar at the top of your browser, starting
with `https://`.

---
## Still not clear?

If a word here is explained using another word you do not know, that is
a failure of this page, not of you. Please
<a href="https://github.com/codetopiacommunity/opensource-onboarding/issues" target="_blank" rel="noopener noreferrer">tell us</a>
and we will fix it, or ask in
[Getting Help](./HELP.md). A word missing from this list is worth
reporting too.
