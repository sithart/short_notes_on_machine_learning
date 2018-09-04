---
title: "Synchronize Files And Directories"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to synchronize files and directories using the Linux command line."
type: technical_note
draft: false
---

`rsync` is a very handy tool for syncing the files and folders in two directories. `rsync` only copies files that have changed since the time they were sync'd.

## Make Two Directories

{{< highlight markdown >}}
mkdir origin destination
{{< /highlight >}}

## Add Files In Origin Directory


{{< highlight markdown >}}
touch origin/file.txt
{{< /highlight >}}

## View Origin Directory Contents

{{< highlight markdown >}}
ls -l origin
{{< /highlight >}}
```
total 0
-rw-rw-r-- 1 chris chris 0 Jul 31 20:04 file.txt
```

## View Destination Directory Contents

{{< highlight markdown >}}
ls -l destination
{{< /highlight >}}
```
total 0
```

## Sync Origin Directory To Destination Directory

In this code we sync (`rsync`) all the files and subdirectories (`-a`) in `origin` to `destination` while printing out details of the process (`v`), deleting (`--delete`) any files in `destination` that no longer exist in `origin`.

{{< highlight markdown >}}
rsync -av --delete origin destination
{{< /highlight >}}
```
sending incremental file list
origin/
origin/file.txt

sent 136 bytes  received 39 bytes  350.00 bytes/sec
total size is 0  speedup is 0.00
```

## View Destination Directory Contents

Notice that `file.txt` in `origin` is now copied over to `destination/origin`.

{{< highlight markdown >}}
ls -l destination/origin
{{< /highlight >}}
```
total 0
-rw-rw-r-- 1 chris chris 0 Jul 31 20:04 file.txt
```