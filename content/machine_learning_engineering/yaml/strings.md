---
title: "Comments"
author: "Chris Albon"
date: 2020-07-03T00:00:00-00:00
description: "Strings in YAML files."
type: technical_note
draft: false
---

Strings in YAML files can have no quotations, double-quotes, or single-quotes.

{{< highlight yaml >}}
---
- This is a string.
- "This is a string."
- 'This is a string.'
{{< /highlight >}}