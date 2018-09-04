---
title: "Create Directory"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to make a directory in the Linux command line."
type: technical_note
draft: false
---

When we want to create a directory in the Linux command line, we can use the `mkdir` (make directory) command.

## View Directory Contents

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 60
drwxrwxr-x 20 chris chris 4096 Oct 11  2017 anaconda3
drwxrwxr-x  2 chris chris 4096 Oct 13  2017 automatic_backups
drwxr-xr-x  3 chris chris 4096 Oct 21  2017 Desktop
drwxr-xr-x  2 chris chris 4096 Oct 10  2017 Documents
drwxr-xr-x  2 chris chris 4096 Jul 19 10:47 Downloads
-rw-r--r--  1 chris chris 8980 Oct 10  2017 examples.desktop
drwxr-xr-x  2 chris chris 4096 Oct 10  2017 Music
drwxrwxr-x  4 chris chris 4096 Oct 11  2017 nvvp_workspace
drwxr-xr-x  2 chris chris 4096 Oct 11  2017 Pictures
drwxr-xr-x  2 chris chris 4096 Oct 10  2017 Public
drwxr-xr-x  2 chris chris 4096 Oct 10  2017 Templates
drwxrwxr-x  7 chris chris 4096 Oct 11  2017 tensorflow
drwxr-xr-x  2 chris chris 4096 Oct 10  2017 Videos
```

## Make A New Directory

{{< highlight markdown >}}
mkdir example_directory
{{< /highlight >}}

## View Directory Contents

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 64
drwxrwxr-x 20 chris chris 4096 Oct 11  2017 anaconda3
drwxrwxr-x  2 chris chris 4096 Oct 13  2017 automatic_backups
drwxr-xr-x  3 chris chris 4096 Oct 21  2017 Desktop
drwxr-xr-x  2 chris chris 4096 Oct 10  2017 Documents
drwxr-xr-x  2 chris chris 4096 Jul 19 10:47 Downloads
drwxrwxr-x  2 chris chris 4096 Jul 22 12:39 example_directory
-rw-r--r--  1 chris chris 8980 Oct 10  2017 examples.desktop
drwxr-xr-x  2 chris chris 4096 Oct 10  2017 Music
drwxrwxr-x  4 chris chris 4096 Oct 11  2017 nvvp_workspace
drwxr-xr-x  2 chris chris 4096 Oct 11  2017 Pictures
drwxr-xr-x  2 chris chris 4096 Oct 10  2017 Public
drwxr-xr-x  2 chris chris 4096 Oct 10  2017 Templates
drwxrwxr-x  7 chris chris 4096 Oct 11  2017 tensorflow
drwxr-xr-x  2 chris chris 4096 Oct 10  2017 Videos
```