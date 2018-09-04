---
title: "Quickly View File Contents"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to check the amount of free memory in a system using the Linux command line."
type: technical_note
draft: false
---

Often we want to quickly take a peek at a file's contents without opening the file in an editor program. The `cat` command makes this easy.

## Create A Text File With Some Contents

{{< highlight markdown >}}
echo 'Here is some text content inside of the file.' > example_file.txt
{{< /highlight >}}

## View Contents Of Text File

{{< highlight markdown >}}
cat example_file.txt
{{< /highlight >}}
```
Here is some text content inside of the file.
```

## View Contents Of Text File With Line Numbers

{{< highlight markdown >}}
cat -n example_file.txt
{{< /highlight >}}
```
     1	Here is some text content inside of the file.
```