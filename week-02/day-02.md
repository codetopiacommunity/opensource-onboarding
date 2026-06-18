# Day 02 — Understand MDX and Frontmatter

Welcome back. 👋

Yesterday you learned Markdown. Today you take one step further.

The profile file you submitted in Week 01 was not a plain `.md` file — it was a `.mdx` file. Today you learn what that means and why it matters.

---

## What You Will Do Today

- Understand what MDX is and how it differs from Markdown
- Understand what frontmatter is and how it works
- Read through your own profile file with fresh eyes
- Know exactly what every line in that file does

---

## Step 1 — What Is MDX?

MDX is Markdown with superpowers.

Regular Markdown lets you format text. MDX lets you do that **plus** embed components — interactive or structured pieces of a web page — directly inside your content.

This is what powers modern documentation sites, blogs, and profile pages (including the Codetopia project).

A `.mdx` file looks almost identical to a `.md` file. The difference is that MDX files can include things like:

```mdx
<ProfileCard name="John Doe" />
```

You do not need to write components yet. What matters right now is understanding the format so you can write MDX content confidently.

> Hint: If you can write Markdown, you can already write 90% of MDX. The extra 10% comes later.

---

## Step 2 — What Is Frontmatter?

Open your profile file from Week 01. The very top of it looks like this:

```
---
name: Your Full Name
github: your-github-username
role: Intern
---
```

That block at the top — between the two `---` lines — is called **frontmatter**.

Frontmatter is structured data about the file. It is not content that shows up as text on the page. Instead, the website reads it and uses it to display your name, link your GitHub, and label your role automatically.

Think of it like a label on a package. The label is not the thing inside the box — it is information *about* what is inside.

The format used is **YAML** (Yet Another Markup Language). It is simple: each line is a `key: value` pair.

```yaml
name: John Doe        # the key is "name", the value is "John Doe"
github: johndoe       # the key is "github", the value is "johndoe"
role: Intern          # the key is "role", the value is "Intern"
```

Rules:
- Always start and end the frontmatter block with `---`
- One key per line
- No quotes needed unless your value contains special characters
- Frontmatter must be at the very top of the file — nothing before it

> Hint: If your frontmatter is wrong, the site may not display your profile at all. A missing `---`, a typo in a key name, or content before the frontmatter block are the most common mistakes.

---

## Step 3 — The Full Structure

Here is the complete structure of a profile `.mdx` file:

```
---
name: Your Full Name
github: your-github-username
role: Intern
---

## Bio

Write a short intro about yourself here.

## Skills

- Skill one
- Skill two
- Skill three

## Fun Fact

Something interesting about you.
```

Breaking it down:

| Part | What it is |
|---|---|
| `--- ... ---` | Frontmatter — structured data read by the site |
| `## Bio` | A Markdown heading starting your written content |
| `- Skill` | A Markdown list |
| Everything else | Plain Markdown |

The frontmatter and the Markdown content work together. The site uses the frontmatter for your profile metadata and renders the Markdown below it as the body of your profile page.

---

## Step 4 — Review Your Own Profile

Go to your fork on GitHub and open your profile file:

```
https://github.com/your-username/open-source-get-started
```

Navigate to `profiles/your-github-username.mdx` and read through it.

Ask yourself:

- Is my frontmatter complete? Are all three fields filled in — `name`, `github`, and `role`?
- Is there anything left blank from the template?
- Does my Bio actually say something about me?
- Are my Skills real and specific? "Problem solving" is vague. "Git", "HTML", "Python" are specific.
- Is my Fun Fact actually fun?

You do not need to make changes today. Just read critically. Tomorrow you will improve it.

> Hint: Read your profile as if you are a stranger seeing it for the first time. Would you know who this person is? Would it tell you anything useful about them?

---

## Quick Reference — What You Learned Today

| Term | What it means |
|---|---|
| MDX | Markdown that can also include components |
| Frontmatter | Structured metadata at the top of a file, between `---` lines |
| YAML | The format used to write frontmatter — simple `key: value` pairs |

---

## Done? Share Your Update

Drop a message in the WhatsApp group:

```
Day 02 ✅ (Week 02)
- Profile link: [link to your profile file on GitHub]
- One thing to improve: [something you noticed when re-reading your profile]
- Stuck on: [anything blocking you, or "nothing"]
- Next: Day 03
```

---

## What Is Next

Tomorrow you go back into your profile, improve it with everything you now know, and open a new Pull Request with the updates.

See you on [Day 03](./day-03.md).
