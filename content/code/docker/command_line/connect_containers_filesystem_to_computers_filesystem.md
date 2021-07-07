---
title: "Connect Container's Filesystem To Computer's Filesystem"
date: 2020-07-22T00:00:00-07:00
description: "How to connect a container's filesystem to a computer filesystem in Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/connect_containers_filesystem_to_computers_filesystem/]
---

Imagine we want to map `important_file_in_container.txt` inside the container with `important_file.txt` outside the container. For example, if we wanted to output the logs from a process inside the container to a log file outside the container.

## Create File

Create a file (`touch`) called `important_file.txt`.

{{< highlight bash >}}
touch important_file.txt
{{< /highlight >}}

## Create Two Filepaths

{{< highlight bash >}}
# Create absolute filepath to file on computer filesystem
ORIGINAL=~/sandbox/docker/important_file.txt

# Create absolute path to where we want to create or replace
# a file inside the container
CONTAINER=/important_file_in_container.txt
{{< /highlight >}}

## Create Container With A Mount Bind

Create and start a detached (`-d`) Docker container (`docker run`) based on the Docker image `nginx:latest` called website (`--name website`). Create a mount bind point (`--mount type=bind`) connecting the file specified by ORIGINAL outside the container (`src=${ORIGINAL}`)  with the file specified by CONTAINER inside the container (`dst=${CONTAINER}`).

{{< highlight bash >}}
docker run -d --name website --mount type=bind,src=${ORIGINAL},dst=${CONTAINER} nginx:latest
{{< /highlight >}}
```
5ca87a0c5c8b5e0535540b8fb4890ec8aae0b6a3d0189dabf9746ab9122abc58
```

## SSH Into Container

Execute (`docker exec`) `/bin/bash` interactively (`-it`) on the Docker container called `website`.

{{< highlight bash >}}
docker exec -it website /bin/bash
{{< /highlight >}}
```
root@5ca87a0c5c8b:/#
```

## View Files And Folder In Container

View all files and folders (`ls`) that displays using long format and shows hidden files (`-al`)

Notice that `important_file_in_container.txt` exists inside the container. That is functionally the same file at `important_file.txt` outside the container.

{{< highlight bash >}}
ls -al
{{< /highlight >}}
```
total 88
drwxr-xr-x   1 root root 4096 Aug  2 05:58 .
drwxr-xr-x   1 root root 4096 Aug  2 05:58 ..
-rwxr-xr-x   1 root root    0 Aug  2 05:58 .dockerenv
drwxr-xr-x   2 root root 4096 Jul 20 00:00 bin
drwxr-xr-x   2 root root 4096 May  2 16:39 boot
drwxr-xr-x   5 root root  340 Aug  2 05:58 dev
drwxr-xr-x   1 root root 4096 Jul 22 03:23 docker-entrypoint.d
-rwxrwxr-x   1 root root 1202 Jul 22 03:22 docker-entrypoint.sh
drwxr-xr-x   1 root root 4096 Aug  2 05:58 etc
drwxr-xr-x   2 root root 4096 May  2 16:39 home
-rw-r--r--   1 1000 1000    0 Aug  2 05:48 important_file_in_container.txt
drwxr-xr-x   1 root root 4096 Jul 22 03:23 lib
drwxr-xr-x   2 root root 4096 Jul 20 00:00 lib64
drwxr-xr-x   2 root root 4096 Jul 20 00:00 media
drwxr-xr-x   2 root root 4096 Jul 20 00:00 mnt
drwxr-xr-x   2 root root 4096 Jul 20 00:00 opt
dr-xr-xr-x 863 root root    0 Aug  2 05:58 proc
drwx------   2 root root 4096 Jul 20 00:00 root
drwxr-xr-x   1 root root 4096 Aug  2 05:58 run
drwxr-xr-x   2 root root 4096 Jul 20 00:00 sbin
drwxr-xr-x   2 root root 4096 Jul 20 00:00 srv
dr-xr-xr-x  13 root root    0 Aug  2 05:39 sys
drwxrwxrwt   1 root root 4096 Jul 22 03:23 tmp
drwxr-xr-x   1 root root 4096 Jul 20 00:00 usr
drwxr-xr-x   1 root root 4096 Jul 20 00:00 var
```