---
title: "Adding Line Numbers"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to add line numbers to text using the Linux command line."
type: technical_note
draft: false
---

## Make File With Some Content

{{< highlight markdown >}}
echo "Jan" >> sales.txt; echo "Feb" >> sales.txt; echo "Mar" >> sales.txt
{{< /highlight >}}

## Make File Contents

{{< highlight markdown >}}
cat sales.txt
{{< /highlight >}}
```
Jan
Feb
Mar
```

## Make File Contents With Line Numbers

{{< highlight markdown >}}
cat -n sales.txt
{{< /highlight >}}
```
     1	Jan
     2	Feb
     3	Mar
```