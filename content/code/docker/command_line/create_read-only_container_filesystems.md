---
title: "Create Read-Only Filesystems In Containers"
date: 2020-07-22T00:00:00-07:00
description: "Create a read only fileystemin a container In Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/create_read-only_container_filesystems/]
---

## Create Container With Read-Only File System

Create and run (`docker run`) a detached container (`--detach`) whose file system is read-only (`--read-only`) with the exception of the /files/ directory (`-v /files/`) and a temp folder at /tmp (`-tmpfs /tmp`) using the Docker image `nginx:latest`.

{{< highlight bash >}}
docker run --detach --read-only -v /files/ --tmpfs /tmp nginx:latest
{{< /highlight >}}
```
7cc0ce7b4eb7c7b25b49e80c1c9e633fd0cba2a87a30cbc5bae42d8d17ad37bc
```