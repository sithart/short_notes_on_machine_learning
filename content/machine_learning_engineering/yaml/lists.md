---
title: "Lists"
author: "Chris Albon"
date: 2020-07-03T00:00:00-00:00
description: "Lists in YAML files."
type: technical_note
draft: false
---

There are two says to create lists in YAML files.

## Lists Using Dashes

{{< highlight yaml >}}
---
- "Apple"
- "Banana"
- "Green Bean"
- "Pineapple"
- "Grape"
{{< /highlight >}}

## Lists Using Brackets And Commas

{{< highlight yaml >}}
---
["Apple", "Banana", "Green Bean", "Pineapple", "Grape"]
{{< /highlight >}}

## Create Lists Within Lists

Nested list item should be indented _two_ spaces.

{{< highlight yaml >}}
---
- "Apple":
  - "Fuji"
  - "Granny"
  - "Green"
  - "Honeybrook"
- "Banana"
- "Green Bean"
- "Pineapple"
- "Grape"
{{< /highlight >}}