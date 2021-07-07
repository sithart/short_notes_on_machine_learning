---
title: "Set A Default Working Directory"
date: 2020-07-22T00:00:00-07:00
description: "Set a default working directory using Dockerfiles."
type: technical_note
draft: False
---

## Create Dockerfile

{{< highlight bash >}}
# Build from base image
FROM ubuntu:latest

# Set a default working directory to tmp/
WORKDIR tmp/
{{< /highlight >}}

## Build Image From Dockerfile

Build the Dockerfile (`docker build`) in the current directory (`.`) and call the image chrisalbon/big-project:working-directory (`--tag chrisalbon/big-project:working-directory`).

{{< highlight bash >}}
docker build --tag chrisalbon/big-project:working-directory .
{{< /highlight >}}
```
Sending build context to Docker daemon  4.608kB
Step 1/2 : FROM ubuntu:latest
 ---> 1e4467b07108
Step 2/2 : WORKDIR tmp/
 ---> Running in 9937480bdea0
Removing intermediate container 9937480bdea0
 ---> 89173bdc678a
Successfully built 89173bdc678a
Successfully tagged chrisalbon/big-project:working-directory
```

## Run Docker Container From Image

Start and create (`docker run`) an interative (`-it`) Docker container called copy-example (`--name working-directory`) from the image called `chrisalbon/big-project:working-directory`. Open a shell (`/bin/bash`). Remove the container after it stops (`-rm`)

{{< highlight bash >}}
docker container run -it --name working-directory chrisalbon/big-project:working-directory /bin/bash
{{< /highlight >}}
```
root@a45354732687:/tmp# 
```

Notice that when the container runs the working directory is `tmp`