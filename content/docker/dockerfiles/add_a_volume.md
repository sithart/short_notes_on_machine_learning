---
title: "Add A Volume"
date: 2020-07-22T00:00:00-07:00
description: "Add volumes to images using Dockerfiles."
type: technical_note
draft: False
---

## Create Dockerfile

`VOLUME` creates volume that both exists as a directory inside the container's filesystem _and_ is accessible on the host's file system. However, note that the name of the volume in the host file system is a long string of random characters, _NOT_ the same name as the directory in the container's filesystem.

Volumes are the prefered way to store persistence data from a container and can be used to share data between containers.

{{< highlight bash >}}
# Build from base image
FROM ubuntu:latest

# Add volume
VOLUME ["project_data"]
{{< /highlight >}}

## Build Image From Dockerfile

Build the Dockerfile (`docker build`) in the current directory (`.`) and call the image chrisalbon/ubuntu:volume-example (`--tag chrisalbon/big-project:volume-example`).

{{< highlight bash >}}
docker build --tag chrisalbon/big-project:volume-example .
{{< /highlight >}}
```
Sending build context to Docker daemon  4.608kB
Step 1/2 : FROM ubuntu:latest
 ---> 1e4467b07108
Step 2/2 : VOLUME ["project_data"]
 ---> Running in bc20457b6aba
Removing intermediate container bc20457b6aba
 ---> 91de40c6d3f0
Successfully built 91de40c6d3f0
Successfully tagged chrisalbon/big-project:volume-example
```

## Run Docker Container From Image

Start and create (`docker run`) an interative (`-it`) Docker container called volume-example (`--name volume-example`) from the image called `chrisalbon/big-project:volume-example`. Remove the container after it stops (`-rm`)

{{< highlight bash >}}
docker container run -it --name volume-example chrisalbon/big-project:volume-example /bin/bash
{{< /highlight >}}
```
root@bff8d32d1675:/#
```

## View Destination Directory

View all files and folders (`ls`) that displays using long format and shows hidden files (`-al`).

{{< highlight bash >}}
ls -al
{{< /highlight >}}
```
total 60
drwxr-xr-x   1 root root 4096 Aug 19 06:00 .
drwxr-xr-x   1 root root 4096 Aug 19 06:00 ..
-rwxr-xr-x   1 root root    0 Aug 19 06:00 .dockerenv
lrwxrwxrwx   1 root root    7 Jul 20 14:43 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 15 11:09 boot
drwxr-xr-x   5 root root  360 Aug 19 06:00 dev
drwxr-xr-x   1 root root 4096 Aug 19 06:00 etc
drwxr-xr-x   2 root root 4096 Apr 15 11:09 home
lrwxrwxrwx   1 root root    7 Jul 20 14:43 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Jul 20 14:43 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Jul 20 14:43 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Jul 20 14:43 libx32 -> usr/libx32
drwxr-xr-x   2 root root 4096 Jul 20 14:43 media
drwxr-xr-x   2 root root 4096 Jul 20 14:43 mnt
drwxr-xr-x   2 root root 4096 Jul 20 14:43 opt
dr-xr-xr-x 867 root root    0 Aug 19 06:00 proc
drwxr-xr-x   2 root root 4096 Aug 19 06:00 project_data
drwx------   2 root root 4096 Jul 20 14:57 root
drwxr-xr-x   1 root root 4096 Jul 24 14:38 run
lrwxrwxrwx   1 root root    8 Jul 20 14:43 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Jul 20 14:43 srv
dr-xr-xr-x  13 root root    0 Aug 19 05:08 sys
drwxrwxrwt   2 root root 4096 Jul 20 14:57 tmp
drwxr-xr-x   1 root root 4096 Jul 20 14:43 usr
drwxr-xr-x   1 root root 4096 Jul 20 14:57 var
```

Notice that the directory `project_data` exists. The directory is avaliable inside the consider as `project_data` and on the host filesystem as a directory in `/var/lib/docker/volumes/`.