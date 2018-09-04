---
title: "Find Symbolic Links"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to find files using the Linux command line."
type: technical_note
draft: false
---

## Make Files, Directories, And A Symbolic Link
{{< highlight markdown >}}
touch sales.txt, marketing.txt, data_science.csv, product.html; mkdir sales marketing
ln -nsf sales.txt marketing.txt
{{< /highlight >}}

## View Files And Directories, And Symbolic Link
{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 8
-rw-rw-r-- 1 chris chris    0 Jul 29 21:21 data_science.csv,
drwxrwxr-x 2 chris chris 4096 Jul 29 21:21 marketing
lrwxrwxrwx 1 chris chris    9 Jul 29 21:58 marketing.txt -> sales.txt
-rw-rw-r-- 1 chris chris    0 Jul 29 21:21 marketing.txt,
-rw-rw-r-- 1 chris chris    0 Jul 29 21:21 product.html
drwxrwxr-x 2 chris chris 4096 Jul 29 21:21 sales
-rw-rw-r-- 1 chris chris    0 Jul 29 21:21 sales.txt,
```

## Find All Symbolic Links In A Given File Path

`-type l` indicates we want to find only files.

{{< highlight markdown >}}
find ~/example_directory -type l
{{< /highlight >}}
```
/home/chris/example_directory/marketing.txt
```