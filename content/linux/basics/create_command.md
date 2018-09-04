---
title: "Create Command"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to create a command using the Linux command line."
type: technical_note
draft: false
---

## Check If Command's Name Is Taken

{{< highlight markdown >}}
type make_example_directory
{{< /highlight >}}
```
-bash: type: make_example_directory: not found
```

Okay good!

## Create Custom Command

Let us create a custom command that creates a bunch of files and subdirectories in a directory. I've used this command a few times for tutorial to simulate a real project. We will separate each command using `;` so they can all be on one line. Specifically, the commands we will run are:

`touch config.txt; touch data.csv; touch readme.md; mkdir sales_data; mkdir scripts`

Notice that the format for creating a command is `alias [command_name]='[command contents]'`

{{< highlight markdown >}}
alias make_fake_project='touch config.txt; touch data.csv; touch readme.md; mkdir sales_data; mkdir scripts'
{{< /highlight >}}

## Run Custom Command

{{< highlight markdown >}}
make_fake_project
{{< /highlight >}}

## View Directory Contents To Check If Command Worked

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 12
-rw-rw-r-- 1 chris chris    0 Jul 25 16:43 config.txt
-rw-rw-r-- 1 chris chris    0 Jul 25 16:43 data.csv
drwxrwxr-x 2 chris chris 4096 Jul 25 16:31 example_directory
-rw-rw-r-- 1 chris chris    0 Jul 25 16:31 example_file.txt
-rw-rw-r-- 1 chris chris    0 Jul 25 16:43 readme.md
drwxrwxr-x 2 chris chris 4096 Jul 25 16:43 sales_data
drwxrwxr-x 2 chris chris 4096 Jul 25 16:43 scripts
```

## Delete Custom Command

{{< highlight markdown >}}
unalias make_fake_project
{{< /highlight >}}