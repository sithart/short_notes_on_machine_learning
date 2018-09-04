---
title: "Append Output To File"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to append the standard output of a command or program to a file using the Linux command line."
type: technical_note
draft: false
---

We can append the outputs of a program to a file by using the `>>` operator.

## Run `date` To See Standard Output

Note `+"%T.%N"` gives the current time with nanseconds

{{< highlight markdown >}}
date +"%T.%N"
{{< /highlight >}}
```
21:19:26.291589981
```

## Create File

{{< highlight markdown >}}
touch records.txt
{{< /highlight >}}

## Append The Standard Output To File

Note that we run `date +%s%N` four times, each time appending the results to `records.txt`.

{{< highlight markdown >}}
date +"%T.%N" >> records.txt; date +"%T.%N" >> records.txt; date +"%T.%N" >> records.txt; date +"%T.%N"  >> records.txt
{{< /highlight >}}

## View File's Contents To See Redirected Standard Output

{{< highlight markdown >}}
cat records.txt
{{< /highlight >}}
```
21:21:50.875588383
21:21:50.876275526
21:21:50.876939495
21:21:50.877571864
```