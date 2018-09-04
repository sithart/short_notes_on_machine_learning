---
title: "View A Text File's Contents"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to view the contents of a text file in the Linux command line."
type: technical_note
draft: false
---

Often we want to look at the contents of some code or configuration file. In Linux, we can do this using the `less` command.

## Create A Text File With Some Contents

{{< highlight markdown >}}
echo "Hello World" > hello_world.txt
{{< /highlight >}}

## View Contents Of File

To view the contents of a file we can open it in the `nano`, a common text editor in Linux systems.

{{< highlight markdown >}}
nano hello_world.txt
{{< /highlight >}}

If we want to leave a file we can press `ctrl-x`.