---
title: "Count Unique Rows"
author: "Chris Albon"
date: 2018-07-16T00:00:00-07:00
description: "How to count unique items using the Linux command line."
type: technical_note
draft: false
---

## Create Example File With List Of Names

Notice that we have duplicated rows

{{< highlight markdown >}}
echo 'Luca Gartside' >> adventurers.txt
echo 'Reule Smyth' >> adventurers.txt
echo 'Spencer Smit' >> adventurers.txt
echo 'Spencer Smit' >> adventurers.txt
echo 'Spencer Smit' >> adventurers.txt
echo 'Uli Pinetotem' >> adventurers.txt
echo 'Uli Pinetotem' >> adventurers.txt
echo 'Uli Pinetotem' >> adventurers.txt
{{< /highlight >}}

## View File

{{< highlight markdown >}}
cat adventurers.txt
{{< /highlight >}}
```
Luca Gartside
Reule Smyth
Spencer Smit
Spencer Smit
Spencer Smit
Uli Pinetotem
Uli Pinetotem
Uli Pinetotem
```

## Get Unique Rows

{{< highlight markdown >}}
cat adventurers.txt | uniq
{{< /highlight >}}
```
Luca Gartside
Reule Smyth
Spencer Smit
Uli Pinetotem
```

## Get Duplicated Rows

{{< highlight markdown >}}
cat adventurers.txt | uniq -d
{{< /highlight >}}
```
Spencer Smit
Uli Pinetotem
```

## Count Unique Rows

`uniq` filters out all non-unique rows. `wc -l` counts the number of lines.

{{< highlight markdown >}}
cat adventurers.txt | uniq | wc -l
{{< /highlight >}}
```
4
```
