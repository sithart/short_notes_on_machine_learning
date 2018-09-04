---
title: "Monitor Processes"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to monitor processes using the Linux command line."
type: technical_note
draft: false
---

## Monitor Processes

`top` shows a live list of all processes with information about them. One piece of information that is often useful is `us`, which shows what percentage of the CPU is being used by user processes (e.g. a script training a neural network). Similarly, `id` tells us the percentage of the CPI that is idle.

{{< highlight markdown >}}
top
{{< /highlight >}}

```
top - 13:34:55 up  5:51,  2 users,  load average: 0.13, 0.10, 0.02
Tasks: 332 total,   1 running, 230 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.2 us,  0.1 sy,  0.0 ni, 99.6 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem : 65908812 total, 63062632 free,   775892 used,  2070288 buff/cache
KiB Swap: 50226172 total, 50226172 free,        0 used. 63921080 avail Mem

   PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
  2247 chris     20   0  513496  24680  20164 S   1.7  0.0   5:28.58 indicator-multi
  1219 root     -51   0       0      0      0 S   0.7  0.0   2:43.25 irq/73-nvidia
  2240 chris     20   0  736948  34220  28616 S   0.7  0.1   0:02.26 nm-applet
   979 message+  20   0   44372   5200   3420 S   0.3  0.0   0:02.55 dbus-daemon
  1018 root      20   0  457400  16268  13544 S   0.3  0.0   0:02.32 NetworkManager
  1036 root      20   0  275888   6376   5624 S   0.3  0.0   0:03.68 accounts-daemon
  1325 chris     20   0   43776   4156   2720 S   0.3  0.0   0:31.53 dbus-daemon
  1476 chris     20   0  563888  32668  25712 S   0.3  0.0   0:59.61 unity-panel-ser
  1528 chris     20   0 1217556 104684  67652 S   0.3  0.2   1:49.74 compiz
  1531 chris     20   0  403148  12920  11452 S   0.3  0.0   0:46.46 indicator-appli
  1614 chris     20   0  341612  10044   8868 S   0.3  0.0   0:00.45 geoclue-master
  1627 chris     20   0  429604  12276  10672 S   0.3  0.0   0:00.45 ubuntu-geoip-pr
     1 root      20   0  185492   6144   4028 S   0.0  0.0   0:01.68 systemd
     2 root      20   0       0      0      0 S   0.0  0.0   0:00.00 kthreadd
     4 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 kworker/0:0H
     6 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 mm_percpu_wq
     7 root      20   0       0      0      0 S   0.0  0.0   0:00.02 ksoftirqd/0
     8 root      20   0       0      0      0 I   0.0  0.0   0:03.54 rcu_sched
     9 root      20   0       0      0      0 I   0.0  0.0   0:00.00 rcu_bh
    10 root      rt   0       0      0      0 S   0.0  0.0   0:00.00 migration/0
```

To leave the `top` progress, press `q`
