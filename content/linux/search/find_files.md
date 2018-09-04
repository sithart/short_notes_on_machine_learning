---
title: "Find Files"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to find files using the Linux command line."
type: technical_note
draft: false
---

## Make Files And Directories
{{< highlight markdown >}}
touch sales.txt, marketing.txt, data_science.csv, product.html; mkdir sales marketing
{{< /highlight >}}

## View Files And Directories
{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 8
-rw-rw-r-- 1 chris chris    0 Jul 29 21:21 data_science.csv,
drwxrwxr-x 2 chris chris 4096 Jul 29 21:21 marketing
-rw-rw-r-- 1 chris chris    0 Jul 29 21:21 marketing.txt,
-rw-rw-r-- 1 chris chris    0 Jul 29 21:21 product.html
drwxrwxr-x 2 chris chris 4096 Jul 29 21:21 sales
-rw-rw-r-- 1 chris chris    0 Jul 29 21:21 sales.txt,
```

## Find All Files In A Given File Path

`-type f` indicates we want to find only files.

{{< highlight markdown >}}
find ~/example_directory -type f
{{< /highlight >}}
```
/home/chris/example_directory/data_science.csv,
/home/chris/example_directory/product.html
/home/chris/example_directory/sales.txt,
/home/chris/example_directory/marketing.txt,
```