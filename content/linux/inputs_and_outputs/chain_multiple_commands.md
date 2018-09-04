---
title: "Chain Multiple Commands"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to chain commands together using the Linux command line."
type: technical_note
draft: false
---

Most commands take in some input and return some output. In Linux, we can use this feature to chain together multiple commands, each one taking the standard output of the previous command as its standard input. We can do this using the pipeline operator, `|`.

## Create Example Files

{{< highlight markdown >}}
touch sales.txt marketing.txt operations.txt hr.txt procurement.txt devops.txt
{{< /highlight >}}

## Create A Pipeline

`ls` and `sort` are two commands. In this example we pipe the standard output of `ls` into the standard input of `sort` and then see `sort`'s standard output. This simple example pipeline chain only contains two commands but often chains contain three or four commands.

{{< highlight markdown >}}
ls | sort
{{< /highlight >}}
```
devops.txt
hr.txt
marketing.txt
operations.txt
procurement.txt
sales.txt
```