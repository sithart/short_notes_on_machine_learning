---
title: "Find Files By Filename"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to find files by filename using the Linux command line."
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
-rw-rw-r-- 1 chris chris    0 Jul 31 09:02 data_science.csv,
drwxrwxr-x 2 chris chris 4096 Jul 31 09:02 marketing
-rw-rw-r-- 1 chris chris    0 Jul 31 09:02 marketing.txt,
-rw-rw-r-- 1 chris chris    0 Jul 31 09:02 product.html
drwxrwxr-x 2 chris chris 4096 Jul 31 09:02 sales
-rw-rw-r-- 1 chris chris    0 Jul 31 09:02 sales.txt,
```

## Find Files Named `product.html`

find ~ -name product.html

## Find Files With "html" at the end of the filename

find ~/linux_tutorials -name *html