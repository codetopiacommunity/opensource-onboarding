# Day 01 — Learn Markdown

Welcome back. 👋

You just spent a week learning Git, GitHub, and the open source contribution workflow. That is the hard part. Now let us slow down and learn something that will make your contributions look polished.

Today you learn Markdown.

Markdown is a simple way to format text. It is what every README, pull request description, GitHub issue, and profile file is written in — including the file you are reading right now.

---

## What You Will Do Today

- Understand what Markdown is and where it is used
- Learn the core syntax: headings, text formatting, lists, links, images, and code
- Write your first Markdown file from scratch
- Preview it on GitHub

---

## Step 1 — What Is Markdown?

Markdown is plain text with special characters that control how it looks when rendered.

For example, this:

```
## Hello World
```

Renders as a large heading that looks like this:

## Hello World

And this:

```
**bold** and _italic_
```

Renders as: **bold** and _italic_

You write Markdown in a plain `.md` file. GitHub, Notion, Discord, and most dev tools know how to render it automatically. No setup needed.

> Hint: The file you are reading right now is a `.md` file. Everything you see formatted — the headings, the bold text, the code blocks — is Markdown.

Want to go deeper? Bookmark this reference and come back to it any time: [Markdown Guide — Basic Syntax](https://www.markdownguide.org/basic-syntax/)

---

## Step 2 — Headings

Headings are made with the `#` symbol. The number of `#` symbols controls the size.

```
# Heading 1  — biggest
## Heading 2
### Heading 3
#### Heading 4
```

Rules:
- Always put a space between `#` and your text
- Use headings in order — do not jump from `#` to `###`

> Hint: `# Heading 1` is for the page title. You only use it once per document. Use `##` and `###` for sections inside the document.

---

## Step 3 — Text Formatting

```
**bold text**
_italic text_
~~strikethrough~~
`inline code`
```

Renders as:

**bold text**
_italic text_
~~strikethrough~~
`inline code`

Use backticks ( ` ) for anything that is a command, filename, or piece of code inside a sentence.

---

## Step 4 — Lists

**Unordered list** (bullet points):

```
- First item
- Second item
- Third item
```

**Ordered list** (numbered):

```
1. First step
2. Second step
3. Third step
```

> Hint: For ordered lists, you can write `1.` for every item and Markdown will number them correctly. This makes reordering items easier — you do not have to renumber by hand.

---

## Step 5 — Links and Images

**Link:**

```
[Link text](https://example.com)
```

The text in square brackets is what shows up. The URL in parentheses is where it goes.

**Image:**

```
![Alt text](https://example.com/image.png)
```

Same as a link, but with a `!` in front. The alt text in square brackets describes the image for screen readers and when the image fails to load.

> Hint: Always write meaningful alt text for images. "profile photo" is better than "image1".

---

## Step 6 — Code Blocks

For a single line of code inside a sentence, use backticks:

```
Run `npm install` to install dependencies.
```

For a full block of code, use triple backticks and optionally specify the language:

````
```bash
git add .
git commit -m "my message"
git push
```
````

The language name after the opening backticks (like `bash`, `js`, `python`) tells GitHub to apply syntax highlighting.

---

## Step 7 — Write Your First Markdown File

Now it is your turn. Open your terminal, go to your repo, and create a new file.

```bash
cd ~/codetopia-community/open-source-get-started
```

Create the file:

```bash
touch practice.md
```

Open it in your text editor:

```bash
code practice.md
```

> Hint: If `code` does not open VS Code, open the file manually in any text editor you have.

Write the following inside the file. Replace the placeholder values with real ones:

````markdown
# My Markdown Practice

## About Me

My name is **[your name]** and I am learning open source at Codetopia.

## What I Have Learned So Far

- Terminal basics
- Git and version control
- GitHub, forking, and cloning
- Opening and reviewing Pull Requests
- Markdown

## My GitHub

[Visit my profile](https://github.com/your-username)

## A Command I Use Often

```bash
git status
```
````

Save the file.

---

## Step 8 — Preview It on GitHub

Push your file up to your fork so you can see it rendered.

```bash
git add practice.md
git commit -m "add markdown practice file"
git push
```

Now go to your fork on GitHub:

```
https://github.com/your-username/open-source-get-started
```

Click on `practice.md` in the file list. GitHub will render it automatically. You should see your headings, bold text, bullet points, and link — all formatted.

If something looks off, go back and check your syntax. One missing space or a wrong character is usually the cause.

> Hint: GitHub has a built-in Markdown preview. In the file editor on GitHub.com, click the **Preview** tab next to **Edit** to see how your Markdown will look before saving.

---

## Quick Reference — Markdown Syntax

| Syntax | Result |
|---|---|
| `# Heading` | Large heading |
| `## Heading` | Smaller heading |
| `**text**` | **Bold** |
| `_text_` | _Italic_ |
| `` `code` `` | `Inline code` |
| `- item` | Bullet point |
| `1. item` | Numbered list |
| `[text](url)` | Link |
| `![alt](url)` | Image |
| ` ```lang ``` ` | Code block |

---

## Done? Share Your Update

Drop a message in the WhatsApp group with a link to your practice file:

```
Day 01 ✅ (Week 02)
- practice.md: [link to your file on GitHub]
- Stuck on: [anything blocking you, or "nothing"]
- Next: Day 02
```

---

## What Is Next

Tomorrow you learn what MDX is, understand frontmatter, and read your own profile file with fresh eyes.

See you on [Day 02](./day-02.md).
