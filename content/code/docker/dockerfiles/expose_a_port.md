---
title: "Expose A Port"
date: 2020-07-22T00:00:00-07:00
description: "Expose a port using Dockerfiles."
type: technical_note
draft: False
---


## Create Dockerfile

`EXPOSE` in the Dockerfile _with_ `-p` in the `docker run` command makes the container accessible via that port on the host machine.

{{< highlight bash >}}
# Build from base image
FROM ubuntu:latest

# Expose port 11
EXPOSE 11
{{< /highlight >}}

## Build Image From Dockerfile

Build the Dockerfile (`docker build`) in the current directory (`.`) and call the image chrisalbon/ubuntu:expose-ports (`--tag chrisalbon/big-project:expose-ports`).

{{< highlight bash >}}
docker build --tag chrisalbon/big-project:expose-ports .
{{< /highlight >}}
```
Sending build context to Docker daemon  4.608kB
Step 1/2 : FROM ubuntu:latest
 ---> 1e4467b07108
Step 2/2 : EXPOSE 80
 ---> Running in cc2bc925b04a
Removing intermediate container cc2bc925b04a
 ---> 14f33f55140f
Successfully built 14f33f55140f
Successfully tagged chrisalbon/ubuntu:expose-port
```

## Run Docker Container From Image

Start and create (`docker run`) an interative (`-it`) Docker container called expose-ports (`--name copy-example`) from the image called `chrisalbon/big-project:expose-ports`. Publish port 11 inside the contain with port 22 outside the container (`-p 11:22`). Open a shell (`/bin/bash`). Remove the container after it stops (`-rm`).

{{< highlight bash >}}
docker container run -p 11:22 -it  --name expose-port chrisalbon/big-project:expose-ports /bin/bash
{{< /highlight >}}
```
root@607a348aad51:/#
```