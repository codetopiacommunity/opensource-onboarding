# Contributing to This Guide

This repo is the onboarding guide itself, and it is open source too.
If you spot a typo, a step that did not work on your machine, or an
explanation that confused you, you can fix it. That fix helps every
person who comes after you.

If you have not been through the guides yet, start with
[00-what-is-open-source.md](./Getting-Started/00-what-is-open-source.md).
Contributing here uses exactly the same steps you learn there.

---
## What we need most

You do not need to be an expert on Git to improve this guide. In fact,
the closer you are to being a beginner, the more useful your feedback
is. The most valuable contributions here are:

- **Fixing anything that did not work for you.** A command that failed,
  output that did not match what the guide said you would see, a link
  that is broken.
- **Clarifying confusing wording.** If you had to read a paragraph
  three times, rewrite it so the next person only reads it once.
- **Filling in missing steps.** If you had to search the internet to
  get past a step, that step is missing something.
- **Adding screenshots.** Several guides have image placeholders
  waiting to be filled in. See [Adding images](#adding-images) below.
- **Platform gaps.** Most steps are written for Windows, macOS, and
  Linux. If your platform is missing or wrong, say so.

Please do not open a pull request that rewrites a whole guide at once.
Small, focused changes get reviewed and merged quickly. Large ones sit
around waiting.

---
## How to contribute

If a step here is unfamiliar, the guide that teaches it is linked next
to it.

1. **Open an issue first** describing what you want to change, unless
   it is an obvious typo. This saves you from doing work that turns
   out to duplicate someone else's.
   ([Guide 07](./Getting-Started/07-finding-and-claiming-an-issue.md))
2. **Fork this repo and clone your fork** to your computer.
   ([Guide 05](./Getting-Started/05-your-first-pull-request.md))
3. **Create a branch** named for what you are doing:
   `fix/broken-link-guide-04`, `docs/clarify-ssh-step`.
4. **Make your change** and read it back once before committing.
5. **Commit** with a message in the style described below.
6. **Push your branch** and open a pull request explaining what you
   changed and why. If it closes an issue, write `Closes #N` in the
   description.
   ([Guide 05](./Getting-Started/05-your-first-pull-request.md))
7. **Respond to review comments.** A maintainer will read your change
   and may suggest a tweak. That is normal, and it is not criticism.
   ([Guide 06](./Getting-Started/06-reviewing-a-pull-request.md))

---
## Commit messages

Use a short prefix, then a description in the present tense of what
the change does:

```bash
git commit -m "docs: clarify the SSH key passphrase step in guide 04"
git commit -m "fix: correct broken link to guide 08 in the README"
```

- `docs:` for wording, structure, or new content
- `fix:` for something that was actually wrong: broken links, wrong
  commands, incorrect output
- `chore:` for everything else, like renaming or moving files

Keep the first line under about 72 characters. If a change needs more
explanation, put it in the pull request description rather than
cramming it into the commit message.

---
## Writing style

The guides follow a consistent style. Match it so the whole thing
reads as one voice.

**Write for someone who has never done this before.** No assumed
knowledge. If you use a term for the first time, explain it in the
same sentence.

**Say what to type and what should happen.** Every command gets a
fenced code block, followed by a "What you should see" description of
the expected output. A beginner cannot tell success from failure
without it.

````markdown
```bash
git status
```

What you should see:

```
On branch main
nothing to commit, working tree clean
```
````

**Use second person and plain language.** "You will see", not "the
user will observe".

**Wrap prose at about 70 characters.** Keep links, tables, and code
blocks on one line even when they run longer.

**Use GitHub alerts for asides**, not bold paragraphs:

```markdown
> [!TIP]
> Useful but optional.

> [!NOTE]
> Worth knowing before you continue.

> [!IMPORTANT]
> Skipping this will cause problems later.
```

**Open external links in a new tab** so nobody loses their place in
the guide:

```markdown
<a href="https://example.com" target="_blank" rel="noopener noreferrer">Example</a>
```

Links to other files in this repo are plain Markdown links.

---
## Guide structure

Each numbered guide in `Getting-Started/` follows the same shape:

1. `# Title`, then a short intro on what this guide is for
2. `## What you will do in this guide`, a bulleted list
3. `## Step 1:`, `## Step 2:`, and so on, separated by `---`
4. `## Quick reference`, a table of what was learned, where useful
5. `## What's next?`, ending with a link to the following guide:
   `🔗 [Next Guide Title](./NN-next-guide.md)`

If you add a new guide, number it in sequence, link it from the
`What you will learn` list in the README, and update the `What's
next?` link at the end of the guide before it.

---
## Adding images

Guides mark where a screenshot belongs with an HTML comment:

```markdown
<!-- IMAGE: Terminal showing git status output. Target path: images/git-status-modified.png -->
```

To fill one in, take the screenshot described, save it at the target
path, and replace the comment with the image:

```markdown
![Terminal showing git status output](../images/git-status-modified.png)
```

Some rules for screenshots:

- Crop to what matters. No full desktops, no visible taskbars.
- Blur or edit out anything personal: email addresses, real file paths
  with your name in them, tokens, anything private.
- Use PNG, and keep files under about 500 KB.
- Always write alt text that describes what is in the image, for
  people using a screen reader.

---
## Before you open your pull request

- [ ] Your change is focused on one thing.
- [ ] Every command you added has been run on a real machine.
- [ ] Every new link has been clicked and works.
- [ ] Prose wraps at about 70 characters.
- [ ] The README list is updated if you added or renamed a guide.

---
## Getting help

Stuck on any of this, or unsure whether an idea is worth doing? Ask in
the
<a href="https://discord.gg/md6e2fmfEw" target="_blank" rel="noopener noreferrer">Discord community</a>.
Asking first is always welcome. Nobody here will mind.
