---
title: "Append File Contents To Another File"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to check the amount of free memory in a system using the Linux command line."
type: technical_note
draft: false
---

## Create A File With A Record Of A Sale

{{< highlight markdown >}}
echo 'Bob Jones bought an apple for $2' > sales_monday.txt
{{< /highlight >}}

## Create A File With A Record Of A Sale

{{< highlight markdown >}}
echo 'Sarah Miller bought an orange for $2' > sales_tuesday.txt
{{< /highlight >}}

## Create An Empty File For All Sales

{{< highlight markdown >}}
touch sales.txt
{{< /highlight >}}

## Append Contents Of Both Files To All Sales File

{{< highlight markdown >}}
cat sales_monday.txt sales_tuesday.txt >> sales.txt
{{< /highlight >}}

## View Contents Of All Sales File

{{< highlight markdown >}}
cat sales.txt
{{< /highlight >}}
```
Bob Jones bought an apple for $2
Sarah Miller bought an orange for $2
```