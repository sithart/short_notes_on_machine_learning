---
title: "Multiline Strings"
author: "Chris Albon"
date: 2020-07-03T00:00:00-00:00
description: "Multiline strings in YAML files."
type: technical_note
draft: false
---

There are two types of multiline strings in YAML:

## Multiline Strings Preserving Newlines

To preserve line breaks, use `|`.

{{< highlight yaml >}}
---
|
This is a multiline
string that has
a series of line breaks.
{{< /highlight >}}
```
This is a multiline
string that has
a series of line breaks.
```

## Multiline Strings Not Preserving Newlines

To not preserve line breaks, use `>`.

{{< highlight yaml >}}
---
>
This is a multiline
string that has
a series of line breaks.
{{< /highlight >}}
```
This is a multiline string that has a series of line breaks.
```