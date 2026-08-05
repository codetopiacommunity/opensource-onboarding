# Reviewing a Pull Request

You opened your first pull request. Now you are on the other side: the
reviewer.

Code review is one of the most important skills in open source and
professional development. It is how teams catch mistakes, share
knowledge, and maintain quality. Being a good reviewer is just as
valuable as being a good contributor.

In this guide, you review a pull request from someone else in the
community.

---
## What you will do in this guide

- Understand what a good review looks like
- Find an open pull request to review
- Leave a meaningful comment
- Submit your review formally

---
## Step 1: What makes a good review

Before you start, understand what you are looking for. A good review
is not about finding fault. It is about making the work better.

When reviewing a CONTRIBUTORS.md pull request, ask yourself:

- Did they add exactly one line?
- Does the line follow the correct format: `- [Name](github-profile-url)`?
- Is the GitHub profile URL a real, working link?
- Did they leave the rest of the file untouched?

You are not expected to be an expert. You are expected to look
carefully and give honest, respectful feedback.

> [!TIP]
> If everything looks good, say so clearly. "Looks good to me, nothing
> to change" is a valid and useful review.

---
## Step 2: Find a pull request to review

Go to the original practice repo on GitHub:

```
https://github.com/codetopiacommunity/open-source-practice
```

Click the **Pull Requests** tab at the top.

<!-- IMAGE: The top navigation of the open-source-practice repo on GitHub. The "Pull requests" tab is highlighted and shows a count of open PRs. Target path: images/pull-requests-tab.png -->

What you should see: a list of open pull requests from other community
members.

Pick one that has not been reviewed yet. A pull request with no
comments usually means no one has looked at it yet.

> [!TIP]
> Do not pick your own pull request. Check the comments on each one
> first to make sure no one else is already reviewing the one you pick.

---
## Step 3: Read the changes

Click on the pull request you chose. You will see:

- The title and description at the top
- A **Files changed** tab showing exactly what was added or modified

Click **Files changed**.

<!-- IMAGE: A pull request page on GitHub with the "Files changed" tab selected. CONTRIBUTORS.md is shown with one new green line added at the bottom. Target path: images/files-changed-tab.png -->

What you should see: `CONTRIBUTORS.md` with one new line highlighted
in green. Green means added content. Red means removed content.

Read it carefully. Check everything from Step 1.

---
## Step 4: Leave a comment

There are two ways to leave a comment:

**On a specific line**

Hover over any line in the Files changed view. A blue `+` button
appears on the left. Click it to leave a comment on that specific
line. Use this when you have feedback about something on that exact
line.

<!-- IMAGE: The Files changed view with the mouse hovering over a line. The blue "+" button is visible on the left side of the line. Target path: images/inline-comment-button.png -->

**On the whole pull request**

Scroll to the bottom of the pull request page. You will see a comment
box. Use this for general feedback about the whole change.

Write your comment clearly and respectfully. If something needs
fixing:

```
The link goes to https://github.com/janedoe but that page does not
exist. Can you double-check your GitHub username?
```

If everything looks good:

```
Looks good to me. Entry follows the correct format and the link works.
```

> [!TIP]
> Never leave a one-word comment like "good" or "fix this." Always
> explain what you mean. The person reading your review should know
> exactly what to do.

---
## Step 5: Submit your review

After writing your comment, submit it formally using the review tool.

Click the **Review changes** button at the top right of the Files
changed tab.

<!-- IMAGE: The top-right area of the Files changed tab showing the green "Review changes" button. Target path: images/review-changes-button.png -->

You will see three options:

- **Comment**: leave feedback without approving or blocking the merge
- **Approve**: you are happy with the changes and they can be merged
- **Request changes**: something needs fixing before this can be merged

Choose based on what you found. Write a short summary in the text box
and click **Submit review**.

What you should see: your review is now visible on the pull request for
the author and maintainers to see.

> [!TIP]
> If you are unsure whether to approve or request changes, choose
> Comment. It is better to give feedback without a final verdict than
> to approve something you are not confident about.

---
## Quick reference

| Term | What it means |
|---|---|
| Code review | Examining someone else's changes and giving feedback |
| Files changed | The tab showing exactly what was added or modified |
| Approve | You confirm the changes are good to merge |
| Request changes | You flag issues that must be fixed before merging |

---
## What's next?

Next, you go beyond adding your name and make a more targeted
contribution: finding a real issue, claiming it, and fixing it.

🔗 [Finding and Claiming an Issue](./06-finding-and-claiming-an-issue.md)
