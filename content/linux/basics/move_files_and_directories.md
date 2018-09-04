---
title: "Move Files And Directories"
author: "Chris Albon"
date: 2018-07-16T00:00:00-07:00
description: "How to move files and directories using the Linux command line."
type: technical_note
draft: false
---

The `mv` command moves a file (deleting it from the original directory). The `cp` command copy-pastes the file to a destination directory. 

## Make File

{{< highlight markdown >}}
touch file.txt
{{< /highlight >}}

## Make Directory
{{< highlight markdown >}}
mkdir example_folder
{{< /highlight >}}

## View Directory Contents Directory

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 8
drwxrwxr-x 2 chris chris 4096 Jul 24 13:23 example_folder
-rw-rw-r-- 1 chris chris    0 Jul 24 13:22 file.txt
```

## Move File To Directory

{{< highlight markdown >}}
mv file.txt example_folder
{{< /highlight >}}

## View Directory Contents Directory

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 8
drwxrwxr-x 2 chris chris 4096 Jul 24 13:23 example_folder
```

## Change To Directory

{{< highlight markdown >}}
cd example_folder
{{< /highlight >}}

## View Directory Contents Directory

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 0
-rw-rw-r-- 1 chris chris 0 Jul 24 13:22 file.txt
```

### `mv` Options:

- `-u` Copy only files that don't exist or are newer than files with the same names in the destination directory
- `-v` Show verbose description of copy
- `-i` Prompt if copy would override file