---
title: "Add Columns To Text"
author: "Chris Albon"
date: 2018-07-16T00:00:00-07:00
description: "How to add colummns to text using the Linux command line."
type: technical_note
draft: false
---

## Create A File With Comma Separated Text

{{< highlight markdown >}}
echo "chris, 34, male" >> staff.txt
echo "sarah, 22, female" >> staff.txt
echo "Bob, 59, male" >> staff.txt
{{< /highlight >}}

## View File

{{< highlight markdown >}}
cat staff.txt
{{< /highlight >}}
```
chris, 34, male
sarah, 22, female
Bob, 59, male
```

## Extract Text By Breaking Into Columns And Save To File

`cut` the text in `staff.txt` that is separated by commas (`-d ','`) into columns, then take the second (`-f 2`) column, and finally save to `ages.txt`

{{< highlight markdown >}}
cut -d ',' -f 2 staff.txt > ages.txt
{{< /highlight >}}

## View `ages.txt`

{{< highlight markdown >}}
cat ages.txt
{{< /highlight >}}
```
 34
 22
 59
```

## Add `ages.txt` As New Column Of `staff.txt`

Add (`paste`) the content of `ages.txt` as a new column of `staff.txt` delimited with a comma (`-d ','`).

{{< highlight markdown >}}
paste -d ',' ages.txt staff.txt
{{< /highlight >}}
```
 34,chris, 34, male
 22,sarah, 22, female
 59,Bob, 59, male
```