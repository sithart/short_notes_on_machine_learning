---
title: "Silence Errors"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to silence standard error of a command or program to a file using the Linux command line."
type: technical_note
draft: false
---

The most common method of silencing an error in Linux is to redirect than error to `/dev/null` which is like the trash bucket of the system. We can do that by including `2> /dev/null` to the end of a command.

## Create Code That Will Produce Error

{{< highlight markdown >}}
ls a_fake_directory/
{{< /highlight >}}
```
ls: a_fake_directory/: No such file or directory
```

## Silence Error

Notice that we aren't silencing so much as redirecting into `/dev/null`. This is like sending the error into a black hole.

{{< highlight markdown >}}
ls a_fake_directory/ 2> /dev/null
{{< /highlight >}}