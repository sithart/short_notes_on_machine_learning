---
title: "Extract Text"
author: "Chris Albon"
date: 2018-07-16T00:00:00-07:00
description: "How to extract text using the Linux command line."
type: technical_note
draft: false
---

`cut` is a good cool to extract text that follows some schema such as tab or comma delimited.

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

## Extract Text By Breaking Into Columns

`cut` the text in `staff.txt` that is separated by commas (`-d ','`) into columns, then take the second (`-f 2`) column.

{{< highlight markdown >}}
cut -d ',' -f 2 staff.txt
{{< /highlight >}}
```
 34
 22
 59
```

 ## Extract Certain Chunk Of Characters From Each Row

 `cut` the text in `staff.txt` up such that we return the second to the fifth (`-c 2-5`) characters of each line.

{{< highlight markdown >}}
 cut -c 2-5 staff.txt
{{< /highlight >}}
```
hris
arah
ob,
```