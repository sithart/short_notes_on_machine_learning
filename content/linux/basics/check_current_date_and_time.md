---
title: "Check Current Date And Time"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to check the current date and time of a system using the Linux command line."
type: technical_note
draft: false
---

If we want to see the system's current date and time, we can use the `date` command.

## Check System's Current Time
{{< highlight markdown >}}
date
{{< /highlight >}}
```
Tue Jul 17 10:07:27 PDT 2018
```

## Check System's Current Time In UTC Time

{{< highlight markdown >}}
date -u
{{< /highlight >}}
```
Tue Jul 17 17:26:25 UTC 2018
```