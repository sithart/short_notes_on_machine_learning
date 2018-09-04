---
title: "Copy Files And Directories"
author: "Chris Albon"
date: 2018-07-16T00:00:00-07:00
description: "How to copy files and directories using the Linux command line."
type: technical_note
draft: false
---

The `cp` command copy-pastes the file to a destination directory. The `mv` command moves a file (deleting it from the original directory).

## Make File

{{< highlight markdown >}}
touch file.txt
{{< /highlight >}}

## Make Directory

{{< highlight markdown >}}
mkdir example
{{< /highlight >}}

## View Directory Contents Directory

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 4
drwxrwxr-x 2 chris chris 4096 Jul 24 08:49 example
-rw-rw-r-- 1 chris chris    0 Jul 24 08:49 file.txt
```

## Copy File To Directory

{{< highlight markdown >}}
cp file.txt example
{{< /highlight >}}

## Change To Directory

{{< highlight markdown >}}
cd example
{{< /highlight >}}

## View Directory Contents Directory

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 0
-rw-rw-r-- 1 chris chris 0 Jul 24 08:49 file.txt
```

### `cp` Options:

- `-a` Copy with original permissions and attributes
- `-u` Copy only files that don't exist or are newer than files with the same names in the destination directory
- `-v` Show verbose description of copy
- `-r` Copy directories and files recursively
- `-i` Prompt if copy would override file