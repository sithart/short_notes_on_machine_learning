---
title: "Changing Directories"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to view change directories in a terminal session using the Linux command line."
type: technical_note
draft: false
---

We can navigate Linux systems in the command line using the `cd` command.

## View Current Working Directory

{{< highlight markdown >}}
pwd
{{< /highlight >}}
```
/home/chris
```

## List Subdirectories

Note `-d */` is a hacky means to list only directories (not files) in a directory.

{{< highlight markdown >}}
ls -d */
{{< /highlight >}}
```
anaconda3/  automatic_backups/  Desktop/  Documents/  Downloads/  Music/  nvvp_workspace/  Pictures/  Public/  Templates/  tensorflow/  Videos/
```

## Change To A Directory Using An Absolute Path

{{< highlight markdown >}}
cd /home/chris/anaconda3
{{< /highlight >}}

## View Current Working Directory

{{< highlight markdown >}}
pwd
{{< /highlight >}}
```
/home/chris/anaconda3
```

## Go Up One Directory

{{< highlight markdown >}}
cd ..
{{< /highlight >}}

## View Current Working Directory

{{< highlight markdown >}}
pwd
{{< /highlight >}}
```
/home/chris
```

## Go Up To A Subdirectory

{{< highlight markdown >}}
cd anaconda3
{{< /highlight >}}

## View Current Working Directory

{{< highlight markdown >}}
pwd
{{< /highlight >}}
```
/home/chris/anaconda3
```

Note: Linux systems often can autocomplete commands. We can take advantage of this by typing `cd` then the first letter of the subdirectory and pressing `tab`. Linux should autocomplete the name - saving us some time.