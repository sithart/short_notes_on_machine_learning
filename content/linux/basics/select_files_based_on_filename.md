---
title: "Select Files Based On Filename"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "Using wildcard characters in the Linux command line."
type: technical_note
draft: false
---

Often we want to select files based on their file name or file extension. In Linux, we can use wildcard characters to accomplish this.

## Create Some Files

{{< highlight markdown >}}
touch hello_world.txt
touch HELLO_world.txt
touch HELLO_world.md
touch hello_america.txt
touch goodbye_america.txt
touch goodbye_america_2.txt
{{< /highlight >}}

## View Directory Contents

{{< highlight markdown >}}
ls
{{< /highlight >}}
```
goodbye_america_2.txt  goodbye_america.txt  hello_america.txt  hello_world.txt  HELLO_world.txt
```

## Select Files Containing "Hello"

{{< highlight markdown >}}
ls hello*
{{< /highlight >}}
```
hello_america.txt  hello_world.txt
```

## Select Files Starting With "g" or "i"

{{< highlight markdown >}}
ls [gi]*
{{< /highlight >}}
```
goodbye_america_2.txt  goodbye_america.txt
```

## Select All Markdown Files

{{< highlight markdown >}}
ls *.md
{{< /highlight >}}
```
HELLO_world.md
```

## Select All Files That Are Markdown Or Text

{{< highlight markdown >}}
ls *.md *.txt
{{< /highlight >}}
```
goodbye_america_2.txt  goodbye_america.txt  hello_america.txt  HELLO_world.md  hello_world.txt  HELLO_world.txt
```

## Select All Files With A Two Character File Extension

{{< highlight markdown >}}
ls *.??
{{< /highlight >}}
```
HELLO_world.md
```

## Select All Files With A Three Character File Extension

{{< highlight markdown >}}
ls *.???
{{< /highlight >}}
```
goodbye_america_2.txt  goodbye_america.txt  hello_america.txt  hello_world.txt  HELLO_world.txt
```

## Select All Files Containing A Digit

{{< highlight markdown >}}
ls *[0-9]*
{{< /highlight >}}
```
goodbye_america_2.txt
```