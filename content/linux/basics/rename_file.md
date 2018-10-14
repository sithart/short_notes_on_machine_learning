---
title: "Rename File"
author: "Chris Albon"
date: 2018-07-16T00:00:00-07:00
description: "How to rename files using the Linux command line."
type: technical_note
draft: false
---

The `mv` (move) command is used to rename files To rename a file, "move" it from one filename to another. 

## Make File

{{< highlight markdown >}}
touch untitled.txt
{{< /highlight >}}

## View Directory Contents Directory

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 0
-rw-rw-r-- 1 chris chris 0 Jul 24 13:22 untitled.txt
```

## Make File

{{< highlight markdown >}}
mv untitled.txt august_records.txt
{{< /highlight >}}

## View Directory Contents Directory

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 0
-rw-rw-r-- 1 chris chris 0 Jul 24 13:22 august_records.txt
```

### `mv` Options:

- `-u` Copy only files that don't exist or are newer than files with the same names in the destination directory
- `-v` Show verbose description of copy
- `-i` Prompt if copy would override file