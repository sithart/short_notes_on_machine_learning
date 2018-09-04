---
title: "Delete Files And Directories In Current Directory"
author: "Chris Albon"
date: 2018-07-16T00:00:00-07:00
description: "How to delete files and directories using the Linux command line."
type: technical_note
draft: false
---

The `rm` (remove) command is used to delete files and folders in Linux.

## Create Example Files

{{< highlight markdown >}}
touch devops.txt hr.txt marketing.txt operations.txt procurement.txt sales.txt
{{< /highlight >}}

## Create Example Subdirectories

{{< highlight markdown >}}
mkdir devops sales marketing
{{< /highlight >}}

## Show Directory Contents

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 12
drwxrwxr-x 2 chris chris 4096 Jul 28 09:05 devops
-rw-rw-r-- 1 chris chris    0 Jul 28 09:05 devops.txt
-rw-rw-r-- 1 chris chris    0 Jul 28 09:05 hr.txt
drwxrwxr-x 2 chris chris 4096 Jul 28 09:05 marketing
-rw-rw-r-- 1 chris chris    0 Jul 28 09:05 marketing.txt
-rw-rw-r-- 1 chris chris    0 Jul 28 09:05 operations.txt
-rw-rw-r-- 1 chris chris    0 Jul 28 09:05 procurement.txt
drwxrwxr-x 2 chris chris 4096 Jul 28 09:05 sales
-rw-rw-r-- 1 chris chris    0 Jul 28 09:05 sales.txt
```

## Delete All Files And Subdirectories

{{< highlight markdown >}}
rm -rf *
{{< /highlight >}}

## Show Directory Contents

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
ls -l
total 0
```