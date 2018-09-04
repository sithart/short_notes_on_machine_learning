---
title: "Archive And Unarchive Files"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to archive and unarchive directories using the Linux command line."
type: technical_note
draft: false
---

## Make Directory

{{< highlight markdown >}}
mkdir regiment_data
{{< /highlight >}}

## Make Files In Directory

{{< highlight markdown >}}
touch regiment_data/battles.txt regiment_data/regiment.txt
{{< /highlight >}}

## Compress Directory

Here we create (`c`) an archive file from the directory `regiment_data` called file (`f`) called `regiment.tar`.

{{< highlight markdown >}}
tar cf regiment.tar regiment_data
{{< /highlight >}}

## View Contents Of Directory

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 24
drwxrwxr-x 2 chris chris  4096 Jul 31 13:23 regiment_data
-rw-rw-r-- 1 chris chris 10240 Jul 31 13:25 regiment.tar
```

## Uncompress Directory

Here we unarchive (`x`) the archived file (`f`) called `regiment.tar`.

{{< highlight markdown >}}
tar xf regiment.tar
{{< /highlight >}}

## View Contents Of Directory

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 24
-rw-rw-r-- 1 chris chris    36 Jul 31 13:17 battles.txt
drwxrwxr-x 2 chris chris  4096 Jul 31 13:23 regiment_data
-rw-rw-r-- 1 chris chris 10240 Jul 31 13:25 regiment.tar
-rw-rw-r-- 1 chris chris    46 Jul 31 13:17 regiment.txt
```