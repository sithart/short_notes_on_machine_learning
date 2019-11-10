# notes

This is Chris Albon's collection of personal notes on coding, statistics, machine learning, and technical management. These notes are posted publically at https://ChrisAlbon.com. What is in this repo will not be useful to other folks.

## Overview

The master record of a note is either a Jupyter Notebook or a Markdown file. These files are in the `content` folder. The website HTML is contained in the `docs` folder.

## Full Deploy Procedure

1. Run `make.ipynb` to convert the Jupyter Notebooks and associated images into Markdown files.
2. Run `hugo` to convert the Markdown files into HTML pages
3. Run `git add -A` 
4. Run `git commit -m "commit message"`
5. Run `git push`

## Markdown Head Metadata Example

```
---
title: "Give Table An Alias"
author: "Chris Albon"
date: 2019-01-28T00:00:00-07:00
description: "Give a table an alias in Snowflake using SQL."
type: technical_note
draft: false
---
```

## Useful Aliases

To reduce the barriers to publishing a new note as much as possible, here are some useful aliases for your `.bash_profile`:

```
# Notes Project

# Go to Notes folder
alias n='cd /Users/chrisalbon/dropbox/cra/projects/notes'

# Go to Notes folder and open Jupyter Notebook
alias jn='cd /Users/chrisalbon/dropbox/cra/projects/notes && jupyter notebook'

# Launch in Hugo server of Notes site
alias hs='cd /Users/chrisalbon/dropbox/cra/projects/notes && hugo server'

# Publish a new note
alias nn='cd /Users/chrisalbon/dropbox/cra/projects/notes && git pull && hugo && git add -A && git commit -m "made changes" && gp && git push'
```

Note that when you run `nn` you might be prompted for an application password. You can get that / generate that from GitHub.com in account settings.