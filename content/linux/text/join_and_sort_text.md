---
title: "Join And Sort Text"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to merge and sort text using the Linux command line."
type: technical_note
draft: false
---

## Make Three Files, Each With List Of Fruit

{{< highlight markdown >}}
echo "Apple" >> fruit_1.txt; echo "Banana" >> fruit_1.txt; echo "Orange" >> fruit_1.txt
echo "Tangerine" >> fruit_2.txt; echo "Grape" >> fruit_2.txt; echo "Nectarine" >> fruit_2.txt
echo "Strawberry" >> fruit_3.txt; echo "Blueberry" >> fruit_3.txt; echo "Mango" >> fruit_3.txt
{{< /highlight >}}

## Merge And Sort Into New File

{{< highlight markdown >}}
sort fruit_1.txt fruit_2.txt fruit_3.txt > fruit.txt
{{< /highlight >}}

# View Contents Of New File

{{< highlight markdown >}}
cat fruit.txt
{{< /highlight >}}
```
Apple
Banana
Blueberry
Grape
Mango
Nectarine
Orange
Strawberry
Tangerine
```