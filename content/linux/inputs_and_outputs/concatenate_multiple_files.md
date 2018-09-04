---
title: "Concatenate Multiple Files"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to concatenate multiple files using the Linux command line."
type: technical_note
draft: false
---

Often large collections of data will be broken into multiple smaller files. The command line makes it easy to concatenate the contents of these files into a single file for analysis.

## Create Multiple Files

In this example each file contains a single record of a sale, however in the real world each file can contain hundreds or even millions of records.

{{< highlight markdown >}}
echo 'Alan Jones', '$50' > sales_records_1.csv
echo 'Stephanie Lawson', '$20' > sales_records_2.csv
echo 'Lester Holt', '$10' > sales_records_3.csv
{{< /highlight >}}

## Append All Files To A Single File

Specifically, what we are doing in the code below is appending (`>>`) every file with `sales_records_` in the file name (e.g. `sales_records_1.csv`) to a file called `sales_records.csv`.

{{< highlight markdown >}}
cat sales_records_* >> sales_records.csv
{{< /highlight >}}

## View The Single File To Confirm The Appending Worked

{{< highlight markdown >}}
cat sales_records.csv
{{< /highlight >}}
```
Alan Jones, $50
Stephanie Lawson, $20
Lester Holt, $10
```

Note that the contents of the files were concatenated in ascending order, meaning `sales_records_1.csv`'s data comes before `sales_records_1.csv`'s data in the final file.