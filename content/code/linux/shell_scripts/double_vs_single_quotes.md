---
title: "Double Vs. Single Quotes"
author: "Chris Albon"
date: 2018-07-16T00:00:00-07:00
description: "Strings in Linux shell scripts"
type: technical_note
draft: false
aliases: [/linux/shell_scripts/double_vs_single_quotes/]
---

Shell variables (e.g. `$PATH`) are treated as simple strings when wrapped in single quotes but as variables when wrapped in double quotes.

## Write The Shell Script

{{< highlight bash >}}
#!/bin/sh

# Print a string surrounded in single quotes
echo 'Single Quotes: $PATH'

# Print a string surrounded in double quotes
echo "Double Quotes: $PATH"
{{< /highlight >}}

## Run The Shell Script

{{< highlight bash >}}
sh quotes.sh
{{< /highlight >}}
```
Single Quotes: $PATH
Double Quotes: /home/chris/anaconda3/bin:/home/chris/anaconda3/condabin:/home/chris/.local/bin:/home/chris/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin#!/bin/sh
```