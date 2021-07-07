---
title: "View All Changes To A Container"
date: 2020-07-22T00:00:00-07:00
description: "View all changes to a filesystem in Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/view_all_changes_to_a_container/]
---

## Create Docker Container

Run an interactive (`-it`) Docker container called project (`--name project`) based on the `ubuntu:latest` image, then run `/bin/bash`.

{{< highlight bash >}}
docker container run -it --name project ubuntu:latest /bin/bash
{{< /highlight >}}
```
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
3ff22d22a855: Pull complete
e7cb79d19722: Pull complete
323d0d660b6a: Pull complete
b7f616834fd0: Pull complete
Digest: sha256:5d1d5407f353843ecf8b16524bc5565aa332e9e6a1297c73a92d3e754b8a636d
Status: Downloaded newer image for ubuntu:latest
root@60655028c0d0:/#
```

## Create File

Create an empty file (`touch`) called `file.txt`.

{{< highlight bash >}}
touch file.txt
{{< /highlight >}}

## Show Container's Filesystem

View all files and folders (`ls`) that displays using long format and shows hidden files (`-al`)

{{< highlight bash >}}
ls -al
{{< /highlight >}}
```
total 56
drwxr-xr-x   1 root root 4096 Aug  7 19:24 .
drwxr-xr-x   1 root root 4096 Aug  7 19:24 ..
-rwxr-xr-x   1 root root    0 Aug  7 19:24 .dockerenv
lrwxrwxrwx   1 root root    7 Jul 20 14:43 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 15 11:09 boot
drwxr-xr-x   5 root root  360 Aug  7 19:24 dev
drwxr-xr-x   1 root root 4096 Aug  7 19:24 etc
-rw-r--r--   1 root root    0 Aug  7 19:24 file.txt
drwxr-xr-x   2 root root 4096 Apr 15 11:09 home
lrwxrwxrwx   1 root root    7 Jul 20 14:43 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Jul 20 14:43 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Jul 20 14:43 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Jul 20 14:43 libx32 -> usr/libx32
drwxr-xr-x   2 root root 4096 Jul 20 14:43 media
drwxr-xr-x   2 root root 4096 Jul 20 14:43 mnt
drwxr-xr-x   2 root root 4096 Jul 20 14:43 opt
dr-xr-xr-x 867 root root    0 Aug  7 19:24 proc
drwx------   2 root root 4096 Jul 20 14:57 root
drwxr-xr-x   1 root root 4096 Jul 24 14:38 run
lrwxrwxrwx   1 root root    8 Jul 20 14:43 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Jul 20 14:43 srv
dr-xr-xr-x  13 root root    0 Aug  7 18:37 sys
drwxrwxrwt   2 root root 4096 Jul 20 14:57 tmp
drwxr-xr-x   1 root root 4096 Jul 20 14:43 usr
drwxr-xr-x   1 root root 4096 Jul 20 14:57 var
```

Notice that `file.txt` exists in the container's root directory.

## Exit Container
{{< highlight bash >}}
exit
{{< /highlight >}}

## View Changes To Container

View the differences between the current state of `big-project` and the original image it is based on.

- `A` means the file or directory was added.
- `C` means the file or directory was changed.
- `D` means the file or directory was deleted.

{{< highlight bash >}}
docker diff big-project
{{< /highlight >}}
```
C /root
A /root/.bash_history
A /file.txt
```

From this command we can see that we changed the root directory, changed `.bash_history` because we ran a bash command, and added a file called `file.txt`.