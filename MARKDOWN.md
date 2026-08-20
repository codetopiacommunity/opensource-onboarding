# Markdown

Markdown is a way of formatting text using ordinary characters you
already have on your keyboard.

You will use it constantly without being taught it: every issue, every
pull request description, every comment on GitHub, and every file in
this course ending in `.md` is written in Markdown. Discord uses most
of it too.

The whole idea is that you type plain characters, and the website turns
them into formatting when it displays your text. Typing `**hello**`
shows as **hello**.

There is not much to it. This page covers everything you actually need.

---
## Bold and italic

| You type | You get |
|---|---|
| `**bold**` | **bold** |
| `*italic*` | *italic* |

Two stars for bold, one for italic. Nothing else to remember.

---
## Headings

A `#` at the start of a line makes a heading. More `#` characters make
a smaller heading.

```markdown
# A big heading
## A smaller heading
### A smaller one still
```

You need a space after the `#`. Without it, nothing happens.

---
## Lists

For a bulleted list, start each line with `-` and a space:

```markdown
- First thing
- Second thing
- Third thing
```

For a numbered list, use numbers:

```markdown
1. First step
2. Second step
3. Third step
```

To indent an item underneath another one, put two spaces in front of
it:

```markdown
- First thing
  - Something under the first thing
```

---
## Links

Square brackets for the words you want to show, then round brackets for
the address:

```markdown
[the Codetopia Community site](https://community.codetopia.org)
```

That shows as an ordinary clickable link reading "the Codetopia
Community site". You do not need to paste raw web addresses into your
writing.

---
## Code and errors

This is the one that matters most on GitHub, because it is how you
paste a command or an error message without it turning into ordinary
words.

For something short inside a sentence, wrap it in single backticks:

```markdown
Run `git status` to see what changed.
```

For anything longer, or for an error message, put three backticks on
the line above and three on the line below:

````markdown
```
fatal: not a git repository
```
````

A backtick is `` ` ``. It sits on the key to the left of the `1` key,
just above Tab on most keyboards. It is **not** an apostrophe and not a
quote mark, and neither of those will work instead.

> [!TIP]
> You can name the language after the opening three backticks, like
> ` ```bash `, and GitHub will colour the code in. Useful, never
> required.

---
## Quotes

A `>` at the start of a line marks quoted text, which is how you reply
to part of what someone else said:

```markdown
> the install docs are missing a step

Agreed, I hit this too.
```

---
## Checklists

On GitHub, `- [ ]` makes a box people can tick:

```markdown
- [ ] Not done yet
- [x] Already done
```

These become real clickable checkboxes in issues and pull requests.
Handy for listing what is left to do.

---
## Blank lines matter

The most common Markdown surprise. If you write two lines with nothing
between them:

```markdown
First line
Second line
```

They come out joined together as one line. To keep them apart, leave a
blank line between:

```markdown
First line

Second line
```

The same applies before a list or a heading. When your formatting comes
out wrong, a missing blank line is usually why.

---
## Check before you post

GitHub shows you exactly how your text will look before you submit it.
Above every box where you type, there is a **Preview** tab. Click it,
check it looks right, click **Write** to go back and fix anything.

<!-- IMAGE: A GitHub comment box with the "Write" and "Preview" tabs above it, with Preview highlighted. Target path: images/markdown-preview-tab.png -->

Use it every time until this becomes automatic. It takes two seconds
and it is how you avoid posting a wall of broken formatting.

---
## Quick reference

| You type | You get |
|---|---|
| `**bold**` | Bold text |
| `*italic*` | Italic text |
| `# Heading` | A heading |
| `- item` | A bulleted list |
| `1. item` | A numbered list |
| `[words](address)` | A link |
| `` `code` `` | Code inside a sentence |
| Three backticks | A block of code or an error |
| `> quoted` | Quoted text |
| `- [ ] task` | A tickable checkbox |

---
## More

That is genuinely most of it. If you want the complete list, GitHub
publishes a
<a href="https://docs.github.com/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax" target="_blank" rel="noopener noreferrer">guide to their version of Markdown</a>.

Any word here you have not met is in the [Glossary](./GLOSSARY.md), and
[Getting Help](./HELP.md) covers where to ask.
