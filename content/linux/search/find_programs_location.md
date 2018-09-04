---
title: "Find Program's Location"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to find a program's location using the Linux command line."
type: technical_note
draft: false
---

Use the `which` command to find the location of a program on the system. This is particularly useful when you are trying to figure out which version of Python is currently set in the environment.

## Find Program's Location

{{< highlight markdown >}}
which python3
{{< /highlight >}}
```
/home/chris/anaconda3/bin/python3
```

Just to prove that this is true, we can change directory, `cd`, to that location and find the file itself.

## Go To Program's Location

{{< highlight markdown >}}
cd /home/chris/anaconda3/bin/
{{< /highlight >}}

## List Contents Of Directory

The `python*` selection means we are only listing files starting with `python`.

{{< highlight markdown >}}
ls -l python*
{{< /highlight >}}
```
lrwxrwxrwx 1 chris chris       9 Oct 11  2017 python -> python3.6
lrwxrwxrwx 1 chris chris       9 Oct 11  2017 python3 -> python3.6
-rwxrwxr-x 1 chris chris 3747848 Oct 11  2017 python3.6
lrwxrwxrwx 1 chris chris      17 Oct 11  2017 python3.6-config -> python3.6m-config
lrwxrwxrwx 1 chris chris       9 Oct 11  2017 python3.6m -> python3.6
-rwxrwxr-x 1 chris chris    3249 Oct 11  2017 python3.6m-config
lrwxrwxrwx 1 chris chris      17 Oct 11  2017 python3-config -> python3.6m-config
```

And there it is! Both `python` and `python3` are symbolic links to `python3.6`.