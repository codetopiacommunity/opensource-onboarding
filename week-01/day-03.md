# Day 03 — GitHub, Fork, and Clone

Welcome back. 👋

Yesterday you installed Git and made your first commit on your local machine. Today you take your work online.

Git lives on your computer. GitHub is the online platform where developers store, share, and collaborate on Git projects. Think of Git as your local save system and GitHub as the cloud backup that the whole world can see and contribute to.

Today you will create a GitHub account, connect Git to GitHub, and bring this repo down to your machine.

---

## What You Will Do Today

- Create a GitHub account
- Connect Git to GitHub using SSH
- Fork this repo
- Clone your fork to your machine

---

## Step 1 — Create a GitHub Account

Go to https://github.com and sign up.

Use the same email you used when configuring Git on Day 02. This is important — GitHub uses your email to link your commits to your account.

Pick a clean, professional username. This is your identity in open source. People will see it on every contribution you make.

> Hint: Avoid usernames with random numbers or characters. Something like `johndoe` or `john-doe` is clean and professional.

Once you sign up, verify your email address. GitHub will send you a confirmation link.

---

## Step 2 — Connect Git to GitHub Using SSH

Right now your computer and GitHub do not know each other. SSH is a secure way to connect them so you can push your work to GitHub without typing your password every time.

**Check if you already have an SSH key**

```bash
ls ~/.ssh
```

What you should see: if you see files named `id_rsa` and `id_rsa.pub` or `id_ed25519` and `id_ed25519.pub`, you already have a key. Skip to the "Add your SSH key to GitHub" part below.

If you see "No such file or directory" or an empty result, you need to create one.

**Create an SSH key**

Run this command with your GitHub email:

```bash
ssh-keygen -t ed25519 -C "your@email.com"
```
> replace "your@email.com" with your github email

What you should see:

```
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/yourname/.ssh/id_ed25519):
```

Press Enter to accept the default location.

It will then ask for a passphrase:

```
Enter passphrase (empty for no passphrase):
```

Press Enter twice to skip the passphrase for now.

What you should see after:

```
Your identification has been saved in /home/yourname/.ssh/id_ed25519
Your public key has been saved in /home/yourname/.ssh/id_ed25519.pub
```

What it means: Git created two files. One is your private key — never share this. The other is your public key — this is what you give to GitHub.

> Hint: Think of the public key as a lock you give to GitHub, and the private key as the only key that opens it. GitHub uses your public key to confirm it is really you when you connect.

**Copy your public key**

```bash
cat ~/.ssh/id_ed25519.pub
```

What you should see: a long line of text starting with `ssh-ed25519`. Select all of it and copy it.

**Add your SSH key to GitHub**

1. Go to https://github.com/settings/keys
2. Click **New SSH key**
3. Give it a title like "My Laptop"
4. Paste your public key into the Key field
5. Click **Add SSH key**

**Test the connection**

```bash
ssh -T git@github.com
```

What you should see:

```
Hi yourusername! You've successfully authenticated, but GitHub does not provide shell access.
```

What it means: your computer and GitHub are now connected. You will not need to enter a password when pushing your work.

> Hint: If you see "Permission denied", your SSH key was not added correctly. Go back and make sure you copied the full public key including the `ssh-ed25519` at the start.

---

## Step 3 — Fork This Repo

A fork is your own personal copy of a repo on GitHub. When you fork a repo, GitHub creates an identical copy under your account. You can make changes to your fork without affecting the original.

1. Go to this repo on GitHub: `https://github.com/codetopiacommunity/open-source-get-started`
2. Click the **Fork** button at the top right of the page
3. Leave all settings as they are and click **Create fork**

What you should see: GitHub takes you to your fork. The URL will change to:

```
https://github.com/your-username/open-source-get-started
```

What it means: this is now your copy of the repo. It lives under your GitHub account.

> Hint: You will always make your changes on your fork, never directly on the original repo. This is how open source collaboration works — everyone works on their own fork and submits changes for review.

---

## Step 4 — Clone Your Fork

Cloning means downloading a copy of a GitHub repo to your local machine so you can work on it.

First go to your codetopia community folder:

```bash
cd ~/codetopia-community
```

Now clone your fork. Go to your fork on GitHub, click the green **Code** button, select **SSH**, and copy the link. It will look like:

```
git@github.com:your-username/open-source-get-started.git
```

Now run:

```bash
git clone git@github.com:your-username/open-source-get-started.git
```

What you should see:

```
Cloning into 'open-source-get-started'...
remote: Enumerating objects...
remote: Counting objects...
Receiving objects: 100%
```

What it means: GitHub sent the entire repo to your machine. You now have a local copy you can work on.

Move into the folder:

```bash
cd open-source-get-started
```

List what is inside:

```bash
ls
```

You should see the repo files including this day file you are reading right now.

> Hint: Always clone using the SSH link, not the HTTPS link. If you use HTTPS, GitHub will ask for your password every time you push. SSH handles this automatically.

---

## Quick Reference — What You Learned Today

| Term | What it means |
|---|---|
| GitHub | Online platform for storing and sharing Git repos |
| SSH | Secure connection between your computer and GitHub |
| Fork | Your personal copy of someone else's repo on GitHub |
| Clone | Downloading a GitHub repo to your local machine |

---

## Done? Share Your Update

Drop a message in the WhatsApp group:

```
Day 03 ✅
- OS: [Windows / Mac / Linux]
- Stuck on: [anything blocking you, or "nothing"]
- Next: Day 04
```

---

## What Is Next

Tomorrow you make a real change to this repo and open your first Pull Request.

See you on Day 04.