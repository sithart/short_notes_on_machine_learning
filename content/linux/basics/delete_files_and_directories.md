---
title: "Delete Files And Directories"
author: "Chris Albon"
date: 2018-07-16T00:00:00-07:00
description: "How to delete files and directories using the Linux command line."
type: technical_note
draft: false
---

The `rm` (remove) command is used to delete files and folders in Linux.

## Create Files

{{< highlight markdown >}}
touch sales.csv
touch config.json
touch README.md
touch documentation.html
touch sales.html
{{< /highlight >}}

## Create Subdirectory

{{< highlight markdown >}}
mkdir sales_reports
{{< /highlight >}}

## Create File In Subdirectory

{{< highlight markdown >}}
touch sales_reports/report.html
{{< /highlight >}}

## View Current Directory

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 4
-rw-rw-r-- 1 chris chris    0 Jul 24 17:01 config.json
-rw-rw-r-- 1 chris chris    0 Jul 24 17:01 documentation.html
-rw-rw-r-- 1 chris chris    0 Jul 24 17:01 README.md
-rw-rw-r-- 1 chris chris    0 Jul 24 17:01 sales.csv
-rw-rw-r-- 1 chris chris    0 Jul 24 17:01 sales.html
drwxrwxr-x 2 chris chris 4096 Jul 24 17:02 sales_reports
```

## Delete File

{{< highlight markdown >}}
rm config.json
{{< /highlight >}}

## Delete All HTML Files

{{< highlight markdown >}}
rm *.html
{{< /highlight >}}

## Delete Subdirectory (And Contained Files)

The `-r` option indicates that files/directories are deleted _recursively_, meaning not only is the directory deleted, but everything inside that directory.

{{< highlight markdown >}}
rm sales_reports -r
{{< /highlight >}}

## View Current Directory

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 0
-rw-rw-r-- 1 chris chris 0 Jul 24 17:01 README.md
-rw-rw-r-- 1 chris chris 0 Jul 24 17:01 sales.csv
```
