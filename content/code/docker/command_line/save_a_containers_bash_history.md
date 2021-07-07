---
title: "Save A Container's Bash History"
date: 2020-07-22T00:00:00-07:00
description: "Save a container's bash history."
type: technical_note
draft: false
aliases: [/docker/command_line/save_a_containers_bash_history/]
---

## Create Dockerfile

{{< highlight bash >}}
# Build from base image
FROM ubuntu:latest
{{< /highlight >}}

## Build Image From Dockerfile

Build the Dockerfile (`docker build`) in the current directory (`.`) and call the image chrisalbon/ubuntu:ubuntu (`--tag chrisalbon/big-project:ubuntu`).

{{< highlight bash >}}
docker build --tag chrisalbon/big-project:ubuntu .
{{< /highlight >}}
```
Sending build context to Docker daemon  4.608kB
Step 1/1 : FROM ubuntu:latest
 ---> 1e4467b07108
Successfully built 1e4467b07108
Successfully tagged chrisalbon/big-project:ubuntu
```

## Run Docker Container While Saving Bash History

Run container (`docker run`) called `chrisalbon/big-project:ubuntu` while connecting the container's bash history (`/root/.bash_history`) with a file on the host machine (`~/.containers_bash_history`). Make it interative (`-it`). Run bash (`/bin/bash`).

{{< highlight bash >}}
docker run -v ~/.containers_bash_history:/root/.bash_history -it chrisalbon/big-project:ubuntu /bin/bash
{{< /highlight >}}
```
root@104183340a88:/#
```

The container's bash history will now be recorded on the host machine in `~/.containers_bash_history`.