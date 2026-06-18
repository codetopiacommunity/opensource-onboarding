# Day 03 — Improve Your Profile and Open a New PR

Welcome back. 👋

Yesterday you read through your profile with fresh eyes. Today you fix what you found.

This is what real open source contribution looks like — not just adding something once and moving on, but coming back to make it better. Iteration is a core part of the process.

---

## What You Will Do Today

- Update your profile with better content
- Commit the changes on a new branch
- Open a new Pull Request

---

## Step 1 — Go to Your Repo

```bash
cd ~/codetopia-community/open-source-get-started
```

Make sure you are on `main` and it is up to date:

```bash
git checkout main
git pull origin main
```

What you should see:

```
Already up to date.
```

or a list of files being pulled down if there were updates since you last synced.

> Hint: Always pull before creating a new branch. This makes sure you are starting from the latest version of the project, not an outdated copy.

---

## Step 2 — Create a New Branch

```bash
git checkout -b improve-my-profile
```

What you should see:

```
Switched to a new branch 'improve-my-profile'
```

---

## Step 3 — Update Your Profile

Open your profile file:

```bash
code profiles/your-github-username.mdx
```

Go through each section and improve it. Use the checklist below.

**Frontmatter**
- [ ] `name` is your real full name — not a placeholder
- [ ] `github` matches your actual GitHub username exactly
- [ ] `role` is filled in

**Bio**
- [ ] At least two sentences
- [ ] Says who you are, where you are from, or what you are working towards
- [ ] No filler like "I am a developer" with nothing else

**Skills**
- [ ] At least three specific skills
- [ ] Use tools and technologies you have actually used — HTML, Python, Git, Figma, etc.
- [ ] No vague entries like "hard work" or "fast learner"

**Fun Fact**
- [ ] One sentence, actually interesting
- [ ] Something a stranger would remember about you

Use the Markdown you learned on Day 01. You can use **bold**, _italic_, and `inline code` inside your Bio and Fun Fact sections if it fits naturally.

> Hint: Do not over-format. Bold and italic are for emphasis — use them sparingly. If everything is bold, nothing stands out.

Save the file when you are done.

---

## Step 4 — Commit Your Changes

Check what changed:

```bash
git diff profiles/your-github-username.mdx
```

Lines in red are what you removed. Lines in green are what you added. Make sure the changes look right.

Stage and commit:

```bash
git add profiles/your-github-username.mdx
git commit -m "improve your-github-username profile"
```

Replace `your-github-username` with your actual username.

---

## Step 5 — Push and Open a PR

```bash
git push origin improve-my-profile
```

Go to your fork on GitHub. You will see the banner prompting you to open a PR. Click **Compare and pull request**.

For the title, use:

```
Improve [your-github-username] profile
```

In the description, briefly explain what you changed and why. For example:

```
- Rewrote Bio to include my background and goals
- Replaced vague skills with specific tools I have used
- Updated Fun Fact
```

Click **Create pull request**.

> Hint: A PR description that explains *what* changed and *why* is far more useful to a reviewer than one that just says "updated profile." It shows you are thinking about the reader.

---

## Quick Reference — What You Practiced Today

| Action | Command |
|---|---|
| Sync with latest | `git pull origin main` |
| New branch | `git checkout -b branch-name` |
| See your changes | `git diff filename` |
| Stage and commit | `git add filename` → `git commit -m "message"` |
| Push branch | `git push origin branch-name` |

---

## Done? Share Your Update

Drop a message in the WhatsApp group with your PR link:

```
Day 03 ✅ (Week 02)
- PR: [link to your pull request]
- What I improved: [one or two things you changed]
- Stuck on: [anything blocking you, or "nothing"]
- Next: Day 04
```

---

## What Is Next

Tomorrow you go beyond your own profile and make a contribution to a different part of the project.

See you on [Day 04](./day-04.md).
