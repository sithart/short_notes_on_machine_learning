---
title: "Measure How Long A Process Takes"
author: "Chris Albon"
date: 2018-07-16T00:00:00-07:00
description: "Measure how long a process takes using the Linux command line."
type: technical_note
draft: false
aliases: [/linux/processes/measure_how_long_a_process_takes/]
---

## Time A Process

{{< highlight markdown >}}
-- Time running the Python program main.py
/usr/bin/time python main.py
{{< /highlight >}}
```
2.16user 0.16system 0:15.71elapsed 14%CPU (0avgtext+0avgdata 63676maxresident)k
0inputs+0outputs (0major+17289minor)pagefaults 0swaps
```

The process took 2.16 seconds of CPU time, 0.16 seconds of kernel time, and a total of 15.71 seconds of total time.