---
title: "If Else For Strings"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to write if else statements for strings using the Linux command line."
type: technical_note
draft: false
---

While you can often use `[[ ]]` for integers, `(( ))` is specifically designed to work with integers and provides a lot more functionality.

## Create Variable

{{< highlight markdown >}}
name="Ralph Holmes"
{{< /highlight >}}

## Create If Else Statement

{{< highlight markdown >}}
if [[ "$name" == "Ralph Holmes" ]]; then
    echo "It is Ralph."
else
    echo "It is not Ralph"
fi
{{< /highlight >}}
```
It is Ralph.
```