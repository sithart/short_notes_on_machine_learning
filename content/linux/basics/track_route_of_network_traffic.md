---
title: "Track Route Of Network Traffic"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to track the route of network traffic using the Linux command line."
type: technical_note
draft: false
---

## Trace Route From Local Computer To Website

`traceroute` shows the path of our network traffic across the internet. Press `ctrl-C` to cancel.

{{< highlight markdown >}}
traceroute google.com
{{< /highlight >}}
```
traceroute to google.com (216.58.219.14), 30 hops max, 60 byte packets
 1  10.0.1.1 (10.0.1.1)  0.920 ms  1.742 ms  2.294 ms
 2  10.33.236.1 (10.33.236.1)  10.222 ms  14.140 ms  14.381 ms
 3  72.215.229.12 (72.215.229.12)  18.079 ms  18.182 ms  18.423 ms
 4  bellcorc02-te-0-0-0-5.ph.ph.cox.net (70.169.72.188)  20.697 ms  20.938 ms  24.585 ms
 5  68.1.4.252 (68.1.4.252)  36.520 ms  36.788 ms  102.515 ms
 6  72.215.224.173 (72.215.224.173)  51.262 ms  43.500 ms 72.215.224.175 (72.215.224.175)  43.209 ms
 7  108.170.247.225 (108.170.247.225)  47.121 ms
 *  45.889 ms
```