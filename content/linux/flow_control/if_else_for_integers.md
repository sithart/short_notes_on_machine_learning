---
title: "If Else For Integers"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to write if else statements for integers using the Linux command line."
type: technical_note
draft: false
---

## Create Variable

{{< highlight markdown >}}
age=23
{{< /highlight >}}

## Create If Else Statement

The code below in plain English: If the variable `age` is greater than 17, then return "Adult" otherwise return "Child".

{{< highlight markdown >}}
if (( "$age" > 17 )); then
    echo "Adult"
else
    echo "Child"
fi
{{< /highlight >}}
```
Adult
```