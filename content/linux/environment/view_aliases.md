---
title: "View Aliases"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to all the aliases in the environment in the Linux command line."
type: technical_note
draft: false
---

We can see all the aliases in the environment using the `alias` command. This can be useful if we have setup some aliases operations we do frequently (like `cd` into a particular project's folder) and we want to remember what they are.

{{< highlight markdown >}}
aliases
{{< /highlight >}}
```
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias l='ls -CF'
alias la='ls -A'
alias lcl='ls -l'
alias ll='ls -alF'
alias ls='ls --color=auto'
```