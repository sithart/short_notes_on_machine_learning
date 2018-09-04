---
title: "Append Error To File"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to append the standard error of a command or program to a file using the Linux command line."
type: technical_note
draft: false
---

We can append the errors of a program to a file by using the `2>>` operator.

## Run Error Producing Code To See Error

{{< highlight markdown >}}
pwd -thiswillproduceerror
{{< /highlight >}}
```
-bash: pwd: -t: invalid option
pwd: usage: pwd [-LP]
```

## Create File

{{< highlight markdown >}}
touch errors.txt
{{< /highlight >}}

## Append The Standard Error To File

Note that we run `pwd -thiswillproduceerror` three times, each time appending the results to `errors.txt`.

{{< highlight markdown >}}
pwd -thiswillproduceerror 2>> errors.txt; pwd -thiswillproduceerror 2>> errors.txt; pwd -thiswillproduceerror 2>> errors.txt
{{< /highlight >}}

## View File's Contents To See Redirected Standard Output

{{< highlight markdown >}}
cat errors.txt
{{< /highlight >}}
```
-bash: pwd: -t: invalid option
pwd: usage: pwd [-LP]
-bash: pwd: -t: invalid option
pwd: usage: pwd [-LP]
-bash: pwd: -t: invalid option
pwd: usage: pwd [-LP]
```