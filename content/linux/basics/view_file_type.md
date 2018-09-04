---
title: "View A File's Type"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to view the type of a file in a system using the Linux command line."
type: technical_note
draft: false
---

The `file` command allows us to view a file's type.

## Make File

{{< highlight markdown >}}
echo "This is some text." > sales.txt
{{< /highlight >}}

## View A File's Type

{{< highlight markdown >}}
file LICENSE.txt
{{< /highlight >}}
```
sales.txt: ASCII text
```