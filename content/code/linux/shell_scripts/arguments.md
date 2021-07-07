---
title: "Arguments"
author: "Chris Albon"
date: 2018-07-16T00:00:00-07:00
description: "Arguments in Linux shell scripts"
type: technical_note
draft: false
aliases: [/linux/shell_scripts/arguments/]
---

Shell scripts can accept positional arguments. They also have some useful built-in arguments.

## Write The Shell Script

{{< highlight bash >}}
#!/bin/sh

echo 'This is the first argument:'
echo $1
echo 'This is the second argument:'
echo $2
echo 'This is the third argument:'
echo $3

echo '-----------'

echo 'This is the number of arguments:'
echo $#

echo '-----------'

echo 'This is all the arguments':
echo $@

echo '-----------'

echo 'This is the process ID':
echo $$

echo '-----------'

echo 'This is the script filename':
echo $0

echo '-----------'

echo 'This is the exit code':
echo $?
{{< /highlight >}}

## Run The Shell Script

{{< highlight bash >}}
sh arguments.sh banana apple grape
{{< /highlight >}}
```
This is the first argument:
banana
This is the second argument:
apple
This is the third argument:
grape
-----------
This is the number of arguments:
3
-----------
This is all the arguments:
banana apple grape
-----------
This is the process ID:
92787
-----------
This is the script filename:
test.sh
-----------
This is the exit code:
0
```