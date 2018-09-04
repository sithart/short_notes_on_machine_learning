---
title: "Sort Rows"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to chain commands together using the Linux command line."
type: technical_note
draft: false
---

The sort command reorganizes lines in a text file or standard output (technically the same thing) so they are arranged numerically and alphabetically.

## Create Example File With List Of Names

{{< highlight markdown >}}
echo 'Luca Gartside' >> adventurers.txt
echo 'Reule Smyth' >> adventurers.txt
echo 'Spencer Smit' >> adventurers.txt
echo 'Crurnirk Steelflow' >> adventurers.txt
echo 'Uli Pinetotem' >> adventurers.txt
echo 'Lai Zhi Lightdream' >> adventurers.txt
{{< /highlight >}}

## View File

{{< highlight markdown >}}
cat adventurers.txt
{{< /highlight >}}
```
Luca Gartside
Reule Smyth
Spencer Smit
Crurnirk Steelflow
Uli Pinetotem
Lai Zhi Lightdream
```

## Sort List Of Names And Write To New File

{{< highlight markdown >}}
sort adventurers.txt > adventurers_sorted.txt
{{< /highlight >}}

## View Sorted File

{{< highlight markdown >}}
cat adventurers_sorted.txt
{{< /highlight >}}
```
Crurnirk Steelflow
Lai Zhi Lightdream
Luca Gartside
Reule Smyth
Spencer Smit
Uli Pinetotem
```

## Alternative: Reverse Sort

{{< highlight markdown >}}
sort -r adventurers.txt
{{< /highlight >}}
```
Uli Pinetotem
Spencer Smit
Reule Smyth
Luca Gartside
Lai Zhi Lightdream
Crurnirk Steelflow
```