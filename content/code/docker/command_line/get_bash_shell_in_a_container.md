---
title: "Get Bash Shell In A Container"
date: 2020-07-22T00:00:00-07:00
description: "Get a bash shell in a running container in Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/get_bash_shell_in_a_container/]
---

## Run Detached Container

Create and start a Docker container (`docker run`) that is detached (`-detacted`), named www (`--name www`), and uses the Docker image `ngix:latest`.

{{< highlight bash >}}
docker run --detach --name www nginx:latest
{{< /highlight >}}
```
f104467b9c7fea62ef6a1b369f90da246eb170dd5c90f6d1d9feede9c2dc7ea1
```

## SSH Into Container

Execute (`docker exec`) `/bin/bash` on the interactive (`-it`) container called `www`.

{{< highlight bash >}}
sudo docker exec -it www /bin/bash
{{< /highlight >}}
```
root@f104467b9c7f:/#
```

## View Container's Filesystem

View all files and folders (`ls`) that displays using long format and shows hidden files (`-al`)

{{< highlight bash >}}
# View container's filesystem
ls -al
{{< /highlight >}}
```
total 88
drwxr-xr-x   1 root root 4096 Aug  2 05:37 .
drwxr-xr-x   1 root root 4096 Aug  2 05:37 ..
-rwxr-xr-x   1 root root    0 Aug  2 05:37 .dockerenv
drwxr-xr-x   2 root root 4096 Jul 20 00:00 bin
drwxr-xr-x   2 root root 4096 May  2 16:39 boot
drwxr-xr-x   5 root root  340 Aug  2 05:37 dev
drwxr-xr-x   1 root root 4096 Jul 22 03:23 docker-entrypoint.d
-rwxrwxr-x   1 root root 1202 Jul 22 03:22 docker-entrypoint.sh
drwxr-xr-x   1 root root 4096 Aug  2 05:37 etc
drwxr-xr-x   2 root root 4096 May  2 16:39 home
drwxr-xr-x   1 root root 4096 Jul 22 03:23 lib
drwxr-xr-x   2 root root 4096 Jul 20 00:00 lib64
drwxr-xr-x   2 root root 4096 Jul 20 00:00 media
drwxr-xr-x   2 root root 4096 Jul 20 00:00 mnt
drwxr-xr-x   2 root root 4096 Jul 20 00:00 opt
dr-xr-xr-x 879 root root    0 Aug  2 05:37 proc
drwx------   2 root root 4096 Jul 20 00:00 root
drwxr-xr-x   1 root root 4096 Aug  2 05:37 run
drwxr-xr-x   2 root root 4096 Jul 20 00:00 sbin
drwxr-xr-x   2 root root 4096 Jul 20 00:00 srv
dr-xr-xr-x  13 root root    0 Aug  2 05:37 sys
drwxrwxrwt   1 root root 4096 Jul 22 03:23 tmp
drwxr-xr-x   1 root root 4096 Jul 20 00:00 usr
drwxr-xr-x   1 root root 4096 Jul 20 00:00 var
```