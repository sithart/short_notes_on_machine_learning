---
title: "Get Information On A File"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to find files using the Linux command line."
type: technical_note
draft: false
---

## Make File
{{< highlight markdown >}}
touch sales.txt
{{< /highlight >}}

## Get Information On File
{{< highlight markdown >}}
stat sales.txt
{{< /highlight >}}
```
  File: sales.txt
  Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
Device: 10302h/66306d	Inode: 9437404     Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/   chris)   Gid: ( 1000/   chris)
Access: 2018-07-31 13:07:05.244384050 -0700
Modify: 2018-07-31 13:07:05.244384050 -0700
Change: 2018-07-31 13:07:05.244384050 -0700
 Birth: -
```