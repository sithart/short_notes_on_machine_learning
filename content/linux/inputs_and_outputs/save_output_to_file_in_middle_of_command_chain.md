---
title: "Save Output To File In Middle Of Command Chain"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to save the output of a file in the middle of the command chain using the Linux command line."
type: technical_note
draft: false
---

The `tee` command creates a T-junction in a command pipeline, both saving the standard output of the previous command to a file and passing the standard output onward down the pipeline. It is often useful when we want to see the data at intermediate steps in a command pipeline without interrupting it.

## Create Example File With List Of File Names

{{< highlight markdown >}}
echo 'data_science.txt' >> files.txt
echo 'data_science.html' >> files.txt
echo 'data_science.csv' >> files.txt
echo 'sales.txt' >> files.txt
echo 'operations.html' >> files.txt
echo 'deep_learning.csv' >> files.txt
{{< /highlight >}}

## View File

{{< highlight markdown >}}
cat files.txt
{{< /highlight >}}
```
data_science.txt
data_science.html
data_science.csv
sales.txt
operations.html
deep_learning.csv
```

## Create Pipeline With Tees

In this pipeline, we:

1. `cat files.txt`, view all filenames
2. `tee all_files.txt`, save all filenames to file
3. `grep data_science`, view only filenames with `data_science` in filename
4. `tee data_science_files.txt`, save all data science filenames to file
5. `grep .csv`, view only filenames with `.csv` in filename
6. `tee data_science_csv_files.txt`, save all data science csv filenames to file

{{< highlight markdown >}}
cat files.txt | tee all_files.txt | grep data_science | tee data_science_files.txt | grep .csv | tee data_science_csv_files.txt
{{< /highlight >}}

```
data_science.csv
```

## View File With All Filenames

{{< highlight markdown >}}
cat all_files.txt
{{< /highlight >}}
```
data_science.txt
data_science.html
data_science.csv
sales.txt
operations.html
deep_learning.csv
```

## View File With Data Science Filenames

{{< highlight markdown >}}
cat data_science_files.txt
{{< /highlight >}}
```
data_science.txt
data_science.html
data_science.csv
```

## View File With Data Science CSV Filenames

{{< highlight markdown >}}
cat data_science_csv_files.txt
{{< /highlight >}}
```
data_science.csv
```