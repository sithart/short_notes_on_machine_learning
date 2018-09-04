---
title: "For Loops"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to write for loop statements strings using the Linux command line."
type: technical_note
draft: false
---

## Create For Loop

In plain English: For each name in Lucien, Maurice, Renald, Johnson, and Alfred, print the name.

{{< highlight markdown >}}
for name in Lucien Maurice Renald Johnson Alfred; do
    echo $name
done
{{< /highlight >}}
```
Lucien
Maurice
Renald
Johnson
Alfred
```

## Create C Style For Loop

Alternatively, we can use a style of for loop seen in the programming language C.

In plain English: Starting with `i` being 0, (`i=0`), as long as `i` is less than 10 (`i<10`), keep returning `i`, adding one to `i` (`i=i+1`) at the end of each loop.

{{< highlight markdown >}}
for (( i=0; i<10; i=i+1 )); do
        echo $i
done
{{< /highlight >}}
```
0
1
2
3
4
5
6
7
8
9
```