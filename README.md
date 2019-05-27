# notes
Technical Notes On Using Data Science & Artificial Intelligence To Fight For Something That Matters.

## To Deploy

1. Run `make.ipynb`
2. Run `hugo` in the `notes` folder
3. Run `git add -A`
4. Run `git commit -m "commit message"`
5. Run `git push`

Site's html is in the master branch's `/docs` folder.

## Useful Aliases

```
alias jn='cd /Users/chrisalbon/dropbox/cra/projects/notes && jupyter notebook'
alias n='cd /Users/chrisalbon/dropbox/cra/projects/notes'
alias hs='cd /Users/chrisalbon/dropbox/cra/projects/notes && hugo server'
alias gn='cd /Users/chrisalbon/dropbox/cra/projects/notes && hugo && git add -A && git commit -m "made changes" && gp && git push'
```