---
title: "See Disk Drive Space"
author: "Chris Albon"
date: 2018-07-16T00:00:00-07:00
description: "See the amount of disk drive space using the Linux command line."
type: technical_note
draft: false
---

To view the amount of used and free memory on a system, we can use the `df` command.

### View Disk Drive Space

{{< highlight markdown >}}
df
{{< /highlight >}}
```
Filesystem    512-blocks      Used Available Capacity iused               ifree %iused  Mounted on
/dev/disk1s1   975221040 415404896 554253656    43% 2387799 9223372036852388008    0%   /
devfs                382       382         0   100%     662                   0  100%   /dev
/dev/disk1s4   975221040   4194384 554253656     1%       2 9223372036854775805    0%   /private/var/vm
map -hosts             0         0         0   100%       0                   0  100%   /net
map auto_home          0         0         0   100%       0                   0  100%   /home
```