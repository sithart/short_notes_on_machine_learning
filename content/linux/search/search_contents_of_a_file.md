---
title: "Search The Contents Of A File"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to search the contents of a file using the Linux command line."
type: technical_note
draft: false
---

## Make File With Some Content

{{< highlight markdown >}}
echo "There were 24 sales in March." >> sales.txt
echo "We have 90 employees." >> employees.txt
{{< /highlight >}}

## Search The File For Some String

{{< highlight markdown >}}
grep March sales.txt
{{< /highlight >}}
```
There were 24 sales in March.
```

## Search The File For Some String, Return With Line Numbers

{{< highlight markdown >}}
grep -n March sales.txt
{{< /highlight >}}
```
1:There were 24 sales in March.
```

## Get Filenames That Match Search

{{< highlight markdown >}}
grep -l March sales.txt
{{< /highlight >}}
```
sales.txt
```