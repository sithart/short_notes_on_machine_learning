---
title: "Create File"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to make a file in the Linux command line."
type: technical_note
draft: false
---

There are a number of ways to create files in the Linux command line.

## View Directory Contents

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 0
```

## Create An Empty File

{{< highlight markdown >}}
touch empty_file.txt
{{< /highlight >}}

## Create Another Empty File

{{< highlight markdown >}}
> another_empty_file.txt
{{< /highlight >}}

## Create File With Some Content

{{< highlight markdown >}}
echo 'This is the contents to the file' > hello_world.txt
{{< /highlight >}}

## Quickly Create A File With Some Contents

{{< highlight markdown >}}
cat > hello_world.txt
{{< /highlight >}}

Then type the contents of the file and press `ctrl-d`

## View Directory Contents

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 4
-rw-rw-r-- 1 chris chris  0 Jul 22 12:46 another_empty_file.txt
-rw-rw-r-- 1 chris chris  0 Jul 22 12:44 empty_file.txt
-rw-rw-r-- 1 chris chris 10 Jul 22 12:46 hello_world.txt
```