# Reporting a Good Issue

In guide 07 you fixed a problem someone else had written down. Now you
write one yourself.

This is worth learning properly, because it is how most people make
their first contribution to a project they have never touched before.
You do not need to know how to fix a problem to report it, and you do
not need permission from anyone. Spotting something and describing it
clearly is genuinely useful work.

Remember Rosemary from
[guide 00](./00-what-is-open-source.md)? Her whole contribution started
with one issue. This is that step.

---
## What an issue actually is

An issue is a public note attached to a project that says "here is
something that needs attention."

Think of it as a numbered ticket. Every issue gets a number, like `#42`,
and anyone can read it, comment on it, and link to it. It stays visible
until someone marks it **closed**, which usually means it was fixed, or
sometimes that the project decided not to act on it.

Issues are not complaints, and filing one is not bothering anyone. A
clear issue is one of the most welcome things you can give a project.
Maintainers cannot fix what they do not know about, and they cannot use
a report they do not understand.

Issues are used for more than bugs. All of these belong in an issue:

- Something is broken.
- Something is confusing or badly explained.
- Something is missing that should exist.
- A link is dead, a word is misspelled, an instruction is out of date.

---
## What you will do in this guide

- Learn when something belongs in an issue, and when it belongs
  somewhere else
- Search a project to check nobody has reported it already
- Write a clear title and a clear description
- Submit a real issue on the practice repo
- Know what happens after you press the button

Nothing to install. This one happens entirely in your web browser.

---
## Step 1: Decide whether it is an issue at all

Not everything belongs in an issue. Before you write one, ask yourself
one question:

> **Would somebody need to do something about this, and would it be a
> shame if it were forgotten in a week?**

If yes, it is an issue. If no, it belongs somewhere else.

| What you have | Where it goes |
|---|---|
| "This is broken" or "this should exist" | **An issue** |
| "Why does Git work this way?" | **A discussion or question** |
| "Is anyone around? I am stuck right now" | **Chat, like Discord** |

The difference is whether there is work to be done. An issue is a piece
of work waiting for someone. A question is just a question: once it is
answered, it is finished.

> [!TIP]
> If you genuinely cannot tell, open the issue. A maintainer can move
> or close it in ten seconds, and nobody will mind. A real problem that
> nobody wrote down is a much bigger loss.

> [!IMPORTANT]
> One exception, and it matters. If you find a **security
> vulnerability**, something that would let a stranger break into
> people's accounts or read private data, do **not** open a public
> issue. Writing it publicly tells attackers about it before it can be
> fixed. Look for a `SECURITY.md` file in the project, which explains
> how to report it privately, or contact a maintainer directly. You
> will probably never need this, but professionals treat it as an
> absolute rule.

---
## Step 2: Search before you write

Before writing anything, check whether someone has already reported it.
Duplicate issues create work for maintainers and split the discussion
across two places.

Go to the practice repo:

```
https://github.com/codetopiacommunity/open-source-practice
```

Click the **Issues** tab, then type a couple of words describing your
problem into the search box at the top of the list.

<!-- IMAGE: The Issues tab of the open-source-practice repo. The search box above the issue list is highlighted with a search term typed into it. Target path: images/issues-search.png -->

Search with the plainest words you can, and use as few as possible. If
you found a link that does not work on the resources page, search
`resources link`. Do not search
`the link on the resources page does not open anything`. Search looks
for issues containing all the words you type, so every extra word
throws away more results. Two or three words is usually right.

**Also search closed issues.** By default GitHub only shows open ones.
In the search box you will see `is:issue is:open`. Delete the
`is:open` part and press Enter to see closed issues too.

What you should see: either a list of issues that might match yours, or
"No results matched your search."

> [!NOTE]
> Found one that already describes your problem? You are not out of
> luck. Add a comment saying you hit it too, and include anything the
> original report is missing. That is a real contribution as well, and
> it tells maintainers the problem affects more than one person.

---
## Step 3: Open the new issue form

If nothing matched, you are clear to write one.

On the Issues tab, click the green **New issue** button on the right.

<!-- IMAGE: The Issues tab with the green "New issue" button in the top right highlighted. Target path: images/new-issue-button.png -->

What you should see: a page with a box for a title, a larger box for a
description, and a green **Create** button at the bottom.

> [!NOTE]
> Some projects show you a menu of templates first, like "Bug report"
> or "Feature request". A template is just a form with the questions
> already written for you. If you see one, pick the closest match and
> fill in the boxes. It makes this whole guide easier, not harder.

---
## Step 4: Write the title

The title is the single most important part, because it is the only
thing most people will ever read. It appears in a long list of other
issues, and it decides whether anyone opens yours.

**A title should summarise the problem, not announce that you have
one.**

Compare:

| Weak title | Why it fails |
|---|---|
| `Help` | Says nothing at all |
| `Bug` | Every issue is a bug. Which one? |
| `This doesn't work` | What is "this", and what is "work"? |
| `URGENT PLEASE FIX` | Still does not say what is wrong |

| Strong title | Why it works |
|---|---|
| `Broken link to the setup guide on the resources page` | Names the problem and where it is |
| `Typo in docs/about.md: "exsits" should be "exists"` | Someone could fix this without opening it |
| `Setup guide is missing the step that adds the upstream remote` | Clear, specific, actionable |

A good test: if someone read only your title, would they know roughly
what needs doing? If yes, it is a good title.

---
## Step 5: Write the description

This is where you give someone enough to act without having to come
back and ask you questions.

Include these five things. Not every one applies every time, and that
is fine.

**1. What you expected to happen.**
One sentence. It sounds obvious to you, but it is often the part that
reveals a misunderstanding on one side or the other.

**2. What actually happened.**
The real behaviour, including the exact error text if there was one.

**3. How to see it yourself.**
Numbered steps, starting from something anyone can do. This is called
**steps to reproduce**, and it is the difference between an issue that
gets fixed today and one that sits for a month. A maintainer who cannot
see the problem cannot fix it.

**4. Where it happened.**
The file name, the page, or the web address.

The web address, often called the **URL**, is the text in the bar at
the very top of your browser, the part that starts with `https://`.
Click it once and it highlights, then copy it. Giving someone the exact
address of the page you were on saves them guessing.

For something you ran on your own computer instead, say which operating
system you are using, such as Windows 11 or macOS, and what
`git --version` prints. All of that together is called your
**environment**: the setup the problem happened in. The same command
can behave differently on different machines, which is why it matters.

**5. Anything extra that helps.**
A screenshot for something visual. A guess at the cause, clearly
labelled as a guess.

Here is the whole thing put together, for a documentation problem:

```
**What I expected**
Following the steps in docs/setup.md should leave me able to push my
branch to my fork.

**What happened**
Step 4 says to run `git push origin my-branch`, but no earlier step
ever connects the folder to my fork, so it fails with
`fatal: 'origin' does not appear to be a git repository`.

**Steps to reproduce**
1. Open docs/setup.md
2. Follow steps 1 to 4 exactly, in a brand new folder
3. The command in step 4 fails

**Where**
docs/setup.md, step 4

**Environment**
Windows 11, Git Bash, git version 2.44.0

I think a step is missing between steps 3 and 4, but I am new to this
and may be wrong.
```

Notice what that report does not do. It does not apologise, it does not
demand, and it does not pretend to be certain. It gives someone
everything they need and gets out of the way.

> [!TIP]
> Paste error messages and commands as **text**, not as a screenshot of
> text. Text can be searched, copied, and quoted back to you. A
> screenshot of an error cannot.
>
> To keep an error looking like an error rather than turning into
> ordinary words, put three backticks on the line above it and three on
> the line below it.
>
> A backtick is `` ` ``. It usually sits on the key to the left of the
> `1` key, just above Tab. It is **not** an apostrophe or a quote mark,
> and those will not work in its place.
>
> So you type this:
>
> ````
> ```
> fatal: not a git repository
> ```
> ````
>
> Screenshots are still perfect for things you can actually see, like a
> broken layout or a button in the wrong place.

---
## Step 6: One problem per issue

If you noticed three separate problems, open three separate issues.

It feels wasteful. It is not. Each issue gets fixed by a different
change, possibly by a different person, at a different time. An issue
listing three problems cannot be closed until all three are done, so it
sits open for weeks while two of them are long finished.

One issue, one problem, one fix. That is the rhythm the whole system is
built around.

---
## Step 7: Submit it

Read your issue back once before submitting. Ask yourself: could a
stranger act on this without asking me anything?

Then click **Create**.

What you should see: your issue, live, with a number at the top like
`#12`, your username, and the time you posted it.

<!-- IMAGE: A submitted issue on GitHub showing the title, issue number, author, and description body. Target path: images/issue-submitted.png -->

**Now practise it for real.** Go to the practice repo, find something
genuinely worth reporting, and open one issue about it. A typo, an
unclear sentence, a dead link. If you cannot find anything, report
something about this course instead, in the
<a href="https://github.com/codetopiacommunity/opensource-onboarding/issues" target="_blank" rel="noopener noreferrer">onboarding repo issues</a>.
There is always something, and you are exactly the right person to spot
it: you have just read these guides with completely fresh eyes.

---
## What happens next

Issues do not get answered instantly, and that is normal.

**A maintainer may add labels.** Labels are coloured tags like `bug`,
`documentation` or `good first issue`. They are how maintainers sort
work. Nothing is required from you.

**Someone may ask you a question.** Answer it when you can. A report
you follow up on is far more useful than one you abandon.

**Someone may fix it, and the issue closes.** You will get a
notification. Your name stays on that issue permanently, as the person
who found it.

**Or nothing happens for a while.** Most maintainers are volunteers
doing this in evenings and weekends. Silence is almost never rejection.
If a couple of weeks pass, one polite comment asking whether anything
more is needed from you is completely acceptable.

**Or it gets closed without being fixed.** This happens, and it is not
a judgement of you. It may already be known, or intentional, or outside
what the project wants to take on. Ask politely why, if you want to
understand. Then move on to the next one.

> [!TIP]
> Do not post the same report in the Discord as well. Pick one place.
> Two copies means two half conversations, and neither has the full
> picture.

---
## Quick reference

| Step | What to do |
|---|---|
| Before writing | Search open **and** closed issues for duplicates |
| Title | Summarise the problem, specifically |
| Description | Expected, actual, steps to reproduce, where, extras |
| Errors | Paste as text between lines of three backticks, not as a screenshot |
| Scope | One problem per issue |
| Security problems | Never in a public issue |
| After submitting | Answer questions, be patient, do not chase |

---
## Stuck?

**You cannot find the Issues tab.**
Some projects turn issues off. If there is no Issues tab at the top of
the repo, look for a `CONTRIBUTING.md` file, which will say where to
report things instead.

**There is no "New issue" button.**
You are probably signed out. Sign in to GitHub and the button appears.

**You are not sure your issue is worth reporting.**
It is. Report it. Being wrong about a small thing costs a maintainer
one comment; staying quiet about a real thing costs everyone.

**You clicked Create too early and the issue is half written.**
Nothing is broken. Click the `...` menu at the top right of your issue,
choose **Edit**, finish it, and save. Editing your own issue is normal
and expected.

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
## You are done

Look at what you can do now.

You went from never having opened a terminal to forking a real repo,
making commits, opening pull requests, reviewing someone else's,
resolving a merge conflict, keeping a fork in sync, and reporting a
problem clearly enough that a stranger can act on it. That is the
complete loop every open source contributor uses, and you have done all
of it for real.

Go back and read Rosemary's story in
[guide 00](./00-what-is-open-source.md) one more time. Every step in it
is now something you have done yourself.

You are ready to contribute to Codetopia Community's actual projects.
Check the how-tos for more guides as the library grows, and ask in
Discussions or Discord if you want to know what to pick up next.

🔗 [How-To Guides](https://community.codetopia.org/howtos)
