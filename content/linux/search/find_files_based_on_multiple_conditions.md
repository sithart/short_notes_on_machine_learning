---
title: "Find Files Based On Multiple Conditions"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to find files based on multiple conditions using the Linux command line."
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

## Find Files And Greater Than 500MBs

`-type f` specifies that we only want to find files, not directories.

{{< highlight markdown >}}
find ~ \( -type f \) -and \( -size +500M \)
{{< /highlight >}}
```
/home/chris/anaconda3/lib/python3.6/site-packages/tensorflow/python/_pywrap_tensorflow_internal.so
/home/chris/Downloads/Anaconda3-5.2.0-Linux-x86_64.sh
/home/chris/Downloads/cuda_9.0.176_384.81_linux.run
```

## Find Files That Have Permission 300 Or Are Greater Than 500MBs

{{< highlight markdown >}}
find ~ \( -perm 0300 \) -or \( -size +500M \)
{{< /highlight >}}
```
/home/chris/anaconda3/lib/python3.6/site-packages/tensorflow/python/_pywrap_tensorflow_internal.so
/home/chris/Downloads/Anaconda3-5.2.0-Linux-x86_64.sh
/home/chris/Downloads/cuda_9.0.176_384.81_linux.run
```