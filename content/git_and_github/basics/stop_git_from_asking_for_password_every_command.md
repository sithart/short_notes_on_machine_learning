---
title: "Stop Git From Asking For Password Every Push And Pull From GitHub"
author: "Chris Albon"
date: 2020-02-01T00:00:00-07:00
description: "Stop git from asking for your username and password every time"
type: technical_note
draft: false
---

If you cloned your GitHub repository using HTTPS, every time you push or pull a repository from GitHub Git [will prompt you for your GitHub username and password](https://help.github.com/en/github/using-git/why-is-git-always-asking-for-my-password). This becomes particularly frustrating if you use multi-factor authentication because you cannot use your regular password but instead use a generated token. You can read more instructions on [how to set up that token here](https://github.blog/2013-09-03-two-factor-authentication/).

To fix this: 

1. Enter the directory containing your repo.
2. Find the `remote.origin.url` using the command: `git config -l`
3. Run the command: `git config remote.origin.url https://{YOUR_USER_NAME}:{PASSWORD}@github.com/{YOUR_USER_NAME}/{REPOSITORY_NAME}.git`

A word of warning: Using this method your password *will be stored in the repository's* `.git/config` *file as plain text*. A safer method for not being required to enter your GitHub username and password every time you push and pull is [to cache your GitHub password](https://help.github.com/en/github/using-git/caching-your-github-password-in-git).
