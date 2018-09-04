---
title: "Join Columns"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to join columns of text using the Linux command line."
type: technical_note
draft: false
---

The Linux command `join` operates similar to the join command in SQL, merging two sets of data along a common key.

## Make File With Soldier Names And Soldier Age Data

{{< highlight markdown >}}
echo "Steve Case, 23" >> soldiers.txt
echo "Mary Mills, 35" >> soldiers.txt
echo "Bob Dosjki, 22" >> soldiers.txt
echo "Jack Doi, 45" >> soldiers.txt
echo "Poe Domi, 23" >> soldiers.txt
{{< /highlight >}}

## Make File With Soldier Names And Regiment Names

{{< highlight markdown >}}
echo "Steve Case, The Hell Hosts" >> regiments.txt
echo "Mary Mills, The Hell Hosts" >> regiments.txt
echo "Bob Dosjki, The Red Riders" >> regiments.txt
echo "Jack Doi, The Red Riders" >> regiments.txt
echo "Poe Domi, The Forsaken Battalion" >> regiments.txt
{{< /highlight >}}

## View Soldier File

{{< highlight markdown >}}
cat soldiers.txt
{{< /highlight >}}
```
Steve Case, 23
Mary Mills, 35
Bob Dosjki, 22
Jack Doi, 45
Poe Domi, 23
```

## View Regiment File

{{< highlight markdown >}}
cat regiments.txt
{{< /highlight >}}
```
Steve Case, The Hell Hosts
Mary Mills, The Hell Hosts
Bob Dosjki, The Red Riders
Jack Doi, The Red Riders
Poe Domi, The Forsaken Battalion
```

## Join Soldier And Regiment Data

In the below code we `join` the two comma delimited (`-t ,`) files using the first column of file 1 (`-1 1`) and the first column of file 2 (`-2 1`) as merge keys. File 1 and file 2 are `soldiers.txt` and `regiments.txt` respectively.

{{< highlight markdown >}}
join -t , -1 1 -2 1 soldiers.txt regiments.txt
{{< /highlight >}}
```
Steve Case, 23, The Hell Hosts
Mary Mills, 35, The Hell Hosts
Bob Dosjki, 22, The Red Riders
Jack Doi, 45, The Red Riders
Poe Domi, 23, The Forsaken Battalion
```