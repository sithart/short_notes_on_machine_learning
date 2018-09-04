---
title: "Ping Website"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to ping a website using the Linux command line."
type: technical_note
draft: false
---

Linux makes it easy to ping a website to test connectivity and/or whether the website is live. Once executed, `ping` will ping the website until it is stopped by pressing `ctrl-C`.

## Ping Google.com

{{< highlight markdown >}}
ping google.com
{{< /highlight >}}
```
PING google.com (172.217.4.174) 56(84) bytes of data.
64 bytes from lax28s01-in-f174.1e100.net (172.217.4.174): icmp_seq=1 ttl=56 time=41.8 ms
64 bytes from lax28s01-in-f174.1e100.net (172.217.4.174): icmp_seq=2 ttl=56 time=35.7 ms
64 bytes from lax28s01-in-f174.1e100.net (172.217.4.174): icmp_seq=3 ttl=56 time=43.6 ms
64 bytes from lax28s01-in-f174.1e100.net (172.217.4.174): icmp_seq=4 ttl=56 time=38.1 ms
64 bytes from lax28s01-in-f174.1e100.net (172.217.4.174): icmp_seq=5 ttl=56 time=38.2 ms
64 bytes from lax28s01-in-f174.1e100.net (172.217.4.174): icmp_seq=6 ttl=56 time=44.0 ms
64 bytes from lax28s01-in-f174.1e100.net (172.217.4.174): icmp_seq=7 ttl=56 time=35.6 ms
64 bytes from lax28s01-in-f174.1e100.net (172.217.4.174): icmp_seq=8 ttl=56 time=46.5 ms
64 bytes from lax28s01-in-f174.1e100.net (172.217.4.174): icmp_seq=9 ttl=56 time=36.9 ms
64 bytes from lax28s01-in-f174.1e100.net (172.217.4.174): icmp_seq=10 ttl=56 time=36.4 ms
64 bytes from lax28s01-in-f174.1e100.net (172.217.4.174): icmp_seq=11 ttl=56 time=38.7 ms
64 bytes from lax28s01-in-f174.1e100.net (172.217.4.174): icmp_seq=12 ttl=56 time=46.5 ms
64 bytes from lax28s01-in-f174.1e100.net (172.217.4.174): icmp_seq=13 ttl=56 time=33.9 ms
64 bytes from lax28s01-in-f174.1e100.net (172.217.4.174): icmp_seq=14 ttl=56 time=37.5 ms
64 bytes from lax28s01-in-f174.1e100.net (172.217.4.174): icmp_seq=15 ttl=56 time=36.0 ms
64 bytes from lax28s01-in-f174.1e100.net (172.217.4.174): icmp_seq=16 ttl=56 time=46.0 ms

--- google.com ping statistics ---
26 packets transmitted, 26 received, 0% packet loss, time 25037ms
rtt min/avg/max/mdev = 31.967/39.521/46.579/4.073 ms
```
