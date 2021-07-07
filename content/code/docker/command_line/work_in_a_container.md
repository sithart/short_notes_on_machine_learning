---
title: "Work In A Container"
date: 2020-07-22T00:00:00-07:00
description: "Work in a container in Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/work_in_a_container/]
---

## Create Docker Container

Run a Docker container (`docker container run`) interactively (`-it`) called project (`--name project`) based on the image `ubuntu:latest` and then run `/bin/bash` to get terminal.

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

You are now put into the Bash terminal of the Docker image.

## Show Container's Filesystem

View all files and folders (`ls`) that displays using long format and shows hidden files (`-al`)

{{< highlight bash >}}
ls -al
{{< /highlight >}}
```
total 56
drwxr-xr-x   1 root root 4096 Aug  7 18:37 .
drwxr-xr-x   1 root root 4096 Aug  7 18:37 ..
-rwxr-xr-x   1 root root    0 Aug  7 18:37 .dockerenv
lrwxrwxrwx   1 root root    7 Jul 20 14:43 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 15 11:09 boot
drwxr-xr-x   5 root root  360 Aug  7 18:37 dev
drwxr-xr-x   1 root root 4096 Aug  7 18:37 etc
drwxr-xr-x   2 root root 4096 Apr 15 11:09 home
lrwxrwxrwx   1 root root    7 Jul 20 14:43 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Jul 20 14:43 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Jul 20 14:43 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Jul 20 14:43 libx32 -> usr/libx32
drwxr-xr-x   2 root root 4096 Jul 20 14:43 media
drwxr-xr-x   2 root root 4096 Jul 20 14:43 mnt
drwxr-xr-x   2 root root 4096 Jul 20 14:43 opt
dr-xr-xr-x 864 root root    0 Aug  7 18:37 proc
drwx------   2 root root 4096 Jul 20 14:57 root
drwxr-xr-x   1 root root 4096 Jul 24 14:38 run
lrwxrwxrwx   1 root root    8 Jul 20 14:43 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Jul 20 14:43 srv
dr-xr-xr-x  13 root root    0 Aug  7 18:37 sys
drwxrwxrwt   2 root root 4096 Jul 20 14:57 tmp
drwxr-xr-x   1 root root 4096 Jul 20 14:43 usr
drwxr-xr-x   1 root root 4096 Jul 20 14:57 var
```

We can see from `ls -al` that we are in the root directory of a Ubuntu installation.