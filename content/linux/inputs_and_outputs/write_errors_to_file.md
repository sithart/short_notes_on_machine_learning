---
title: "Write Errors To File"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to write the standard error of a command or program to a file using the Linux command line."
type: technical_note
draft: false
---

Standard errors are by default printed on the screen. However, it is often useful to write errors to a file for logging purposes. We can do that using `2>`.

## Create Code That Will Produce Error

{{< highlight markdown >}}
ls /a/
{{< /highlight >}}
```
ls: cannot access '/a/': No such file or directory
```

## Create File To Store Error

{{< highlight markdown >}}
touch errors.log
{{< /highlight >}}

## Write Error To File

In this line we run the command that produces the error and then add `2> errors.log` to tell the system to write any errors to the file `errors.log` instead of printing them on the screen.

{{< highlight markdown >}}
ls /a/ 2> errors.log
{{< /highlight >}}

## View Contents Of File To Check That The Error Was Written

{{< highlight markdown >}}
cat errors.log
{{< /highlight >}}
```
ls: cannot access '/a/': No such file or directory
```