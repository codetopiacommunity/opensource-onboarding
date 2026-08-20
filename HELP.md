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
## If it is a word you do not know

Look it up in the [Glossary](./GLOSSARY.md). Not understanding a word
is a completely normal reason to be stuck, and it is the fastest kind
to fix.

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

There are two places to ask, and they are equally welcome. Pick
whichever suits you.

First, a quick sanity check on where your thing belongs:

| What you have | Where it goes |
|---|---|
| "This is broken" or "this should exist" | An **issue** |
| "Why does this work this way?" | **GitHub Discussions** |
| "I am stuck right now, is anyone around?" | **Discord**, or Discussions |

The test is whether somebody would need to *do* something about it. If
yes, it belongs in an issue, where it can be tracked until it is done.
If it is just a question, it does not.

### Option 1: GitHub Discussions

<a href="https://github.com/codetopiacommunity/opensource-onboarding/discussions/categories/q-a" target="_blank" rel="noopener noreferrer">Ask in Discussions</a>
using the **Q&A** category. A form walks you through what to include,
so you do not have to work out how to phrase it.

Use this if you would rather not add another chat app, if your network
blocks Discord, if you are on limited mobile data, or if you simply
prefer taking your time over writing a question. It needs nothing
except the GitHub account this course gives you anyway.

Answers come from a maintainer, usually within a day. Slower than
Discord, but it never depends on someone happening to be online, and
your answer stays public and searchable for the next person who hits
the same wall.

### Option 2: The Codetopia Community Discord

The <a href="https://discord.gg/md6e2fmfEw" target="_blank" rel="noopener noreferrer">Codetopia Community Discord</a>
is the fastest route. Someone is usually around, and answers tend to
come in minutes. It is also where the rest of the community is, if you
want that.

Never used Discord? Here is the whole thing: it is a free chat app, it
runs in your web browser without installing anything, and you sign up
with just an email address. Click the link, create an account, and post
in the onboarding channel.

> [!NOTE]
> **Discord is entirely optional.** You never need it to finish this
> course. If you do not want an account, or cannot reach it from your
> network, Discussions covers everything.

### Reporting a problem with a guide

Different from asking for help: if a guide is wrong, unclear, or
missing a step,
<a href="https://github.com/codetopiacommunity/opensource-onboarding/issues" target="_blank" rel="noopener noreferrer">open an issue</a>
instead. That is a real contribution, and
[CONTRIBUTING.md](./CONTRIBUTING.md) explains how. Better still, fix it
yourself.

> [!TIP]
> Creating a GitHub account is free and takes about two minutes. You
> will make one in [guide 04](./Getting-Started/04-github-account-and-ssh.md)
> regardless, but if you want the GitHub-only route from the very
> start, make it now:
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
> To paste code or an error into Discord or GitHub and have it stay
> looking like code, put three backticks on the line above it and three
> on the line below it.
>
> A backtick is `` ` ``. It usually sits on the key to the left of the
> `1` key, just above Tab. It is **not** an apostrophe or a quote mark,
> and those will not work in its place.
>
> So you type this:
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
