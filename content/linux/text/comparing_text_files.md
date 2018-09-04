---
title: "Comparing Text Files"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How compare text files using the Linux command line."
type: technical_note
draft: false
---

The `diff` command in Linux will show us the where the lines in text files differ and ignore lines that are the same.

## Create Text File 1

{{< highlight markdown >}}
echo "Khaydarbi Melikov is a foot soldier." >> regiment_version1.txt
echo "Khaydarbi Melikov is a member of the the Maroon Martyrs regiment" >> regiment_version1.txt
{{< /highlight >}}

## Create Text File 2 

{{< highlight markdown >}}
echo "Khaydarbi Melikov is a foot soldier." >> regiment_version2.txt
echo "Khaydarbi Melikov is a member of the Reserve regiment" >> regiment_version2.txt
{{< /highlight >}}

## View Text File 1 

{{< highlight markdown >}}
$ cat regiment_version1.txt
{{< /highlight >}}
```
Khaydarbi Melikov is a foot soldier.
Khaydarbi Melikov is a member of the the Maroon Martyrs regiment
```

## View Text File 2

{{< highlight markdown >}}
$ cat regiment_version1.txt
{{< /highlight >}}
```
Khaydarbi Melikov is a foot soldier.
Khaydarbi Melikov is a member of the Reserve regiment
```

## Create Compare Text Files

{{< highlight markdown >}}
diff regiment_version1.txt regiment_version2.txt
{{< /highlight >}}
```
2c2
< Khaydarbi Melikov is a member of the the Maroon Martyrs regiment
---
> Khaydarbi Melikov is a member of the Reserve regiment
```

Notice that the lines that matched are not shown, instead it outputs only the line in both documents that differs.

If we want to see the context around the differences, we can use the `-c` argument:

{{< highlight markdown >}}
diff -c regiment_version1.txt regiment_version2.txt
{{< /highlight >}}
```
*** regiment_version1.txt	2018-08-03 11:20:07.313559654 -0700
--- regiment_version2.txt	2018-08-03 11:20:10.077617610 -0700
***************
*** 1,2 ****
  Khaydarbi Melikov is a foot soldier.
! Khaydarbi Melikov is a member of the the Maroon Martyrs regiment
--- 1,2 ----rm
  Khaydarbi Melikov is a foot soldier.
! Khaydarbi Melikov is a member of the Reserve regiment
```