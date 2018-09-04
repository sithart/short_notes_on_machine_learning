---
title: "Multiple Commands On One Line"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to have multiple commands with one line using the Linux command line."
type: technical_note
draft: false
---

You can have multiple commands in one line as long as they are separated with the `;` symbol.

Note that this is not a very widely used feature -- but it is seen.

## Make A Subdirectory, Make A File, View Directory Contents
{{< highlight markdown >}}
mkdir example_directory; touch example_file.txt; ls -l
{{< /highlight >}}
```
total 4
drwxrwxr-x 2 chris chris 4096 Jul 25 16:31 example_directory
-rw-rw-r-- 1 chris chris    0 Jul 25 16:31 example_file.txt
```