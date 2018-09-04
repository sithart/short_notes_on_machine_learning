---
title: "If Else With Multiple Conditions"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to write if else statements for strings using the Linux command line."
type: technical_note
draft: false
---

## Create Variable

{{< highlight markdown >}}
age=23
{{< /highlight >}}

## Check Greater Than 17 And Less Than 30

To combine conditional tests with "and" use `&&`.

{{< highlight markdown >}}
if (( "$age" > 17  && "$age" < 30 )); then
    echo "Greater than 17 and less than 30"
else
    echo "Not greater than 17 and less than 30"
fi
{{< /highlight >}}
```
Greater than 17 and less than 30
```

## Check Greater Than 17 Or Less Than 20

To combine conditional tests with "or" use `||`.

{{< highlight markdown >}}
if (( "$age" > 17 || "$age" < 30)); then
    echo "Greater than 17, or less than 30"
else
    echo "Not greater than 17 or less than 30"
fi
{{< /highlight >}}
```
Greater than 17 or less than 30
```