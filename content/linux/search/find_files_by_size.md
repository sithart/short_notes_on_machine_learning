---
title: "Find Files By Size"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to find based on file size the Linux command line."
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

## Find Find Files Smaller Than 1M

In this code, we want files smaller than (`-`) one (`1`) megabyte (`M`). You can customize the smaller/greater, number, and unit of file size (e.g. gigabytes is `G`) to fit your specific need. 


{{< highlight markdown >}}
find ~/linux_tutorials -size -1M
{{< /highlight >}}
```
/home/chris/linux_tutorials/sales.txt,
/home/chris/linux_tutorials/marketing.txt,
/home/chris/linux_tutorials/product.html
/home/chris/linux_tutorials/data_science.csv,
```