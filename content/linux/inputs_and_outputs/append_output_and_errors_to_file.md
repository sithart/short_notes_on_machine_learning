---
title: "Append Outputs And Errors To File"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to write the standard error of a command or program to a file using the Linux command line."
type: technical_note
draft: false
---

To write both the output and the errors of a program to a file, we can use the `&>>` on newer versions of bash to append (not write over) either standard outputs or standard errors to a file.

## Create Code That Will Produce An Output

{{< highlight markdown >}}
pwd
{{< /highlight >}}
```
/home/chris/example_directory
```

## Create Code That Will Produce An Error

{{< highlight markdown >}}
pwd -thisisafakeargumenttoproduceerror
{{< /highlight >}}
```
-bash: pwd: -t: invalid option
pwd: usage: pwd [-LP]
```

## Create File To Hold Output And Errors
{{< highlight markdown >}}
touch log.txt
{{< /highlight >}}

## Append Working Code's Output To File
{{< highlight markdown >}}
pwd &>> log.txt
{{< /highlight >}}

## Append Error-Producing Code's Error To File
{{< highlight markdown >}}
pwd -thisisafakeargumenttoproduceerror &>> log.txt
{{< /highlight >}}

## View File Contents To Show Both Output And Error
{{< highlight markdown >}}
cat log.txt
{{< /highlight >}}
```
/home/chris/example_directory
-bash: pwd: -t: invalid option
pwd: usage: pwd [-LP]
```