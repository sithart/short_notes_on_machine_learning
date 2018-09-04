---
title: "See Free Memory"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to check the amount of free memory in a system using the Linux command line."
type: technical_note
draft: false
---

The best way to check the amount of free memory in a Linux system is to use the `free` command. This command lists the amount of free memory.

## Check System's Free Memory

{{< highlight markdown >}}
free
{{< /highlight >}}
```
              total        used        free      shared  buff/cache   available
Mem:       65908812      244948    64239140      206180     1424724    64672848
Swap:      50226172           0    50226172
```

## Check System's Free Memory In A More Human Readable Format

{{< highlight markdown >}}
free -h
{{< /highlight >}}
```
              total        used        free      shared  buff/cache   available
Mem:            62G        239M         61G        209M        1.4G         61G
Swap:           47G          0B         47G
```