---
title: "View First And Last Parts Of Files"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to view the first and last parts of files using the Linux command line."
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
echo 'Ognem Dustsplitter' >> adventurers.txt
echo 'Ebil Frugroll' >> adventurers.txt
echo 'Gordon Humphrey' >> adventurers.txt
echo 'Jermaine Randall' >> adventurers.txt
echo 'Eli Steele' >> adventurers.txt
echo 'Gregory Potts' >> adventurers.txt
echo 'Emil Carter' >> adventurers.txt
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
Ognem Dustsplitter
Ebil Frugroll
Gordon Humphrey
Jermaine Randall
Eli Steele
Gregory Potts
Emil Carter
```

## View First 10 Lines Of Fine

{{< highlight markdown >}}
head adventurers.txt
{{< /highlight >}}
```
Luca Gartside
Reule Smyth
Spencer Smit
Crurnirk Steelflow
Uli Pinetotem
Ognem Dustsplitter
Ebil Frugroll
Gordon Humphrey
Jermaine Randall
Eli Steele
```

## View First 3 Lines Of Fine

{{< highlight markdown >}}
head -n 3 adventurers.txt
{{< /highlight >}}
```
Luca Gartside
Reule Smyth
Spencer Smit
```

## View Last 5 Lines Of Fine

{{< highlight markdown >}}
tail -n 5 adventurers.txt
{{< /highlight >}}
```
Gordon Humphrey
Jermaine Randall
Eli Steele
Gregory Potts
Emil Carter
```