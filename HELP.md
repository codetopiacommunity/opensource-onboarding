# Getting Help

Everyone gets stuck. It is not a sign you are bad at this, it is the
normal experience of learning to use these tools. What separates people
who get through it from people who quit is knowing where to look next.

This page is where to look next.

---
## Start here: the error is probably normal

Before anything else, read the error message on your screen slowly, all
the way through. Terminal errors look intimidating, but they usually
say exactly what is wrong in the last line. You do not need to
understand every word.

Then check the **Stuck?** section at the bottom of the guide you are on.
The most common failure for each step is listed there with the fix.

That solves most problems without needing to ask anyone.

---
## Problems that come up everywhere

These four account for most of what goes wrong, in any guide.

**`command not found`, or `'git' is not recognized`**
The program is not installed, or your terminal was open before you
installed it. Close the terminal completely, open a new one, and try
again. If it still fails, the install did not finish. Go back to
[guide 02](./Getting-Started/02-installing-and-configuring-git.md).

**`No such file or directory`**
You are not in the folder you think you are in. Run `pwd` to see where
you actually are, and `ls` to see what is there. Nearly every "the file
does not exist" problem is really a "wrong folder" problem.

**`Permission denied (publickey)`**
GitHub does not recognise your computer. Your SSH key is either not
created, not added to GitHub, or not loaded. Work back through
[guide 04, step 2](./Getting-Started/04-github-account-and-ssh.md).

**The command seems frozen and nothing happens**
Some commands wait for input rather than hanging. If you see a `>` on a
line by itself, you probably have an unclosed quote: press `Ctrl+C` and
run the command again. In a text editor opened by Git, press `Esc`,
then type `:q!` and press Enter to get out.

> [!TIP]
> Copy the exact error text and search the web for it. Reading other
> people's answers to the same error is a genuine developer skill, not
> cheating, and it is what the rest of us do all day.

---
## Asking a person

If none of the above got you moving, ask. Nobody will think less of you
for it, and a question you found worth asking is usually one somebody
else is quietly stuck on too.

### The Codetopia Community Discord

The fastest way to get an answer is the
<a href="https://discord.gg/md6e2fmfEw" target="_blank" rel="noopener noreferrer">Codetopia Community Discord</a>.
Someone is usually around, and answers tend to come in minutes rather
than days.

If you have never used Discord before, here is the whole thing: it is a
free chat app, it works in your web browser without installing
anything, and you can sign up with just an email address. Click the
link above, create an account if you do not have one, and you are in.
Post your question in the onboarding channel.

You do not need to introduce yourself, ask permission, or apologise for
being new. Just ask.

### On GitHub

From [guide 04](./Getting-Started/04-github-account-and-ssh.md) onward
you have a GitHub account, which gives you a second option. Use it when
your question is about this guide itself rather than about your own
machine:

- **Something in a guide is wrong, unclear, or missing a step?**
  <a href="https://github.com/codetopiacommunity/opensource-onboarding/issues" target="_blank" rel="noopener noreferrer">Open an issue</a>.
  That is a real contribution, and [CONTRIBUTING.md](./CONTRIBUTING.md)
  explains how.
- **Want to fix it yourself?** Even better. Same link, same file.

> [!NOTE]
> Creating a GitHub account is free and takes about two minutes. If you
> would rather ask questions on GitHub than on Discord, you can create
> yours now instead of waiting for guide 04:
> <a href="https://github.com/signup" target="_blank" rel="noopener noreferrer">github.com/signup</a>.

---
## How to ask so you get a good answer

This matters more than people expect, and it is a skill you will use
for the rest of your career. Include four things:

1. **Which guide and which step** you are on.
2. **The exact command you typed.** Copy and paste it, do not retype it
   from memory.
3. **The exact output you got.** Copy and paste the whole thing, error
   included. A screenshot works too.
4. **What you expected instead**, and anything you already tried.

Compare these two questions:

> git isn't working, help

> I'm on guide 03, step 6. I ran `git add hello.txt` and got
> `fatal: not a git repository`. I expected it to stage the file.
> I ran `git init` in step 3 and it seemed to work.

The second one can be answered immediately. The first one costs three
messages of back and forth before anyone can even start.

> [!TIP]
> To paste code or an error into Discord or GitHub, wrap it in triple
> backticks so it keeps its formatting:
>
> ````
> ```
> your error here
> ```
> ````

---
## One more thing

If you get stuck, work out the fix, and the guide never mentioned it,
that is a gap worth closing. Please
<a href="https://github.com/codetopiacommunity/opensource-onboarding/issues" target="_blank" rel="noopener noreferrer">tell us</a>
or fix it yourself. You have just found something only a beginner could
find, and the next person gets a smoother ride because of it.
