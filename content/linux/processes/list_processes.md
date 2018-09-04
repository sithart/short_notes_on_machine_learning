---
title: "List Processes"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to list processes using the Linux command line."
type: technical_note
draft: false
---

## List Processes

We are often interested in the `STAT` column:
- `R` - process is running
- `S` - process is sleeping
- `D` - process is in uninterruptible sleep
- `T` - process is terminated
- `D` - process is dead
- `<` - process is high priority
- `N` - process is low priority

Note that normally the list of processes is very long, so for the sake of this tutorial we included `| head` which will show only the first few processes.

{{< highlight markdown >}}
ps aux | head
{{< /highlight >}}
```
USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root          1  0.0  0.0 185492  6144 ?        Ss   07:43   0:01 /sbin/init splash
root          2  0.0  0.0      0     0 ?        S    07:43   0:00 [kthreadd]
root          4  0.0  0.0      0     0 ?        I<   07:43   0:00 [kworker/0:0H]
root          6  0.0  0.0      0     0 ?        I<   07:43   0:00 [mm_percpu_wq]
root          7  0.0  0.0      0     0 ?        S    07:43   0:00 [ksoftirqd/0]
root          8  0.0  0.0      0     0 ?        I    07:43   0:03 [rcu_sched]
root          9  0.0  0.0      0     0 ?        I    07:43   0:00 [rcu_bh]
root         10  0.0  0.0      0     0 ?        S    07:43   0:00 [migration/0]
root         11  0.0  0.0      0     0 ?        S    07:43   0:00 [watchdog/0]
```