---
title: "Create Sequential List Of Files And Directories"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to create a sequential list of files and directories in the Linux command line."
type: technical_note
draft: false
---

## Create Sequential List Of Files

{{< highlight markdown >}}
touch script_version_{1..5}.py
{{< /highlight >}}

## Create Sequential List Of Directories

{{< highlight markdown >}}
mkdir data_{2015..2018}
{{< /highlight >}}

## View Files And Directories

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 16
drwxrwxr-x 2 chris chris 4096 Jul 29 11:17 data_2015
drwxrwxr-x 2 chris chris 4096 Jul 29 11:17 data_2016
drwxrwxr-x 2 chris chris 4096 Jul 29 11:17 data_2017
drwxrwxr-x 2 chris chris 4096 Jul 29 11:17 data_2018
-rw-rw-r-- 1 chris chris    0 Jul 29 11:18 script_version_1.py
-rw-rw-r-- 1 chris chris    0 Jul 29 11:18 script_version_2.py
-rw-rw-r-- 1 chris chris    0 Jul 29 11:18 script_version_3.py
-rw-rw-r-- 1 chris chris    0 Jul 29 11:18 script_version_4.py
-rw-rw-r-- 1 chris chris    0 Jul 29 11:18 script_version_5.py
```