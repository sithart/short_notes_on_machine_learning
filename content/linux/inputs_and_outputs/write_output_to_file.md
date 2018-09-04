---
title: "Write Output To File"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to write the standard output of a command or program to a file using the Linux command line."
type: technical_note
draft: false
---

By default standard output of a program goes to the screen. For example, the standard output of `ls` is a list of files and directories in a directory, which is by default shown on the terminal screen. However, it does not need to be. We can redirect the standard output of a program to a file using the `>` operator.

## Make Some Files And Folders

{{< highlight markdown >}}
touch config.txt; touch data.csv; touch readme.md; mkdir sales_data; mkdir scripts
{{< /highlight >}}

## Run `ls` To See Standard Output

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 8
-rw-rw-r-- 1 chris chris    0 Jul 26 11:23 config.txt
-rw-rw-r-- 1 chris chris    0 Jul 26 11:23 data.csv
-rw-rw-r-- 1 chris chris    0 Jul 26 11:23 readme.md
drwxrwxr-x 2 chris chris 4096 Jul 26 11:23 sales_data
drwxrwxr-x 2 chris chris 4096 Jul 26 11:23 scripts
```

## Redirect `ls`'s Standard Output To File

Notice the `>` operator followed by the file where the standard output will be written.

{{< highlight markdown >}}
ls -l > directory_contents.txt
{{< /highlight >}}

## View File's Contents To See Redirected Standard Output

{{< highlight markdown >}}
cat directory_contents.txt
{{< /highlight >}}
```
total 8
-rw-rw-r-- 1 chris chris    0 Jul 26 11:23 config.txt
-rw-rw-r-- 1 chris chris    0 Jul 26 11:23 data.csv
-rw-rw-r-- 1 chris chris    0 Jul 26 11:24 directory_contents.txt
-rw-rw-r-- 1 chris chris    0 Jul 26 11:23 readme.md
drwxrwxr-x 2 chris chris 4096 Jul 26 11:23 sales_data
drwxrwxr-x 2 chris chris 4096 Jul 26 11:23 scripts
```