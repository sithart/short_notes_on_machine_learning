---
title: "Set Default Working Directory"
date: 2020-07-22T00:00:00-07:00
description: "Set the default working directory using Dockerfiles."
type: technical_note
draft: False
---

## Create Dockerfile

`WORKDIR` sets the default working directory of an image. If the directory does not already exist it will be created.

{{< highlight bash >}}
# Build from base image
FROM ubuntu:latest

# Set default working directory
WORKDIR "/projects/super-secret-project"
{{< /highlight >}}

## Build Image From Dockerfile

Build the Dockerfile (`docker build`) in the current directory (`.`) and call the image chrisalbon/ubuntu:super-secret (`--tag chrisalbon/big-project:super-secret`).

{{< highlight bash >}}
docker build --tag chrisalbon/big-project:super-secret .
{{< /highlight >}}
```
Sending build context to Docker daemon  2.048kB
Step 1/2 : FROM ubuntu:latest
 ---> 1e4467b07108
Step 2/2 : WORKDIR "/projects/super-secret-project"
 ---> Running in a8351b81583a
Removing intermediate container a8351b81583a
 ---> 06d74fe681a4
Successfully built 06d74fe681a4
Successfully tagged chrisalbon/big-project:super-secret
```

## Run Docker Container From Image

Start and create (`docker run`) an interative (`-it`) Docker container called super-secret-project (`--name super-secret-project`) from the image called `chrisalbon/big-project:super-secret`. Open a bash shell (`/bin/bash`). Remove the container after it stops (`-rm`).

{{< highlight bash >}}
docker container run -it --name super-secret-project chrisalbon/big-project:super-secret /bin/bash
{{< /highlight >}}
```
root@798559f1cf26:/projects/super-secret-project#
```

## Print Working Directory

{{< highlight bash >}}
pwd
{{< /highlight >}}
```
/projects/super-secret-project
```