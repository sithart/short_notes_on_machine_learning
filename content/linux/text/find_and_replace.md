---
title: "Find And Replace"
author: "Chris Albon"
date: 2018-07-16T00:00:00-07:00
description: "How to find and replace using the Linux command line."
type: technical_note
draft: false
---

## Create Example File With List Of Adventurers

{{< highlight markdown >}}
echo 'Luca Gartside' >> adventurers.txt
echo 'Reule Smyth' >> adventurers.txt
echo 'Spencer Smit' >> adventurers.txt
{{< /highlight >}}

## View Original File

{{< highlight markdown >}}
$ cat adventurers.txt
{{< /highlight >}}
```
Luca Gartside
Reule Smyth
Spencer Smit
```

## Search And Replace

Here we use the streaming edit (`sed`) command to replace `Spencer Smit` with `Matthew Aldworth` in the file `adventurers.txt`

{{< highlight markdown >}}
$ sed "s/Spencer Smit/Matthew Aldworth/" adventurers.txt
{{< /highlight >}}
```
Luca Gartside
Reule Smyth
Matthew Aldworth
```