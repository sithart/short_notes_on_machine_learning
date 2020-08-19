---
title: "Add Files And Folders To Images"
date: 2020-07-22T00:00:00-07:00
description: "Add files and folders to images using Dockerfiles."
type: technical_note
draft: False
---

## Make Files And Folders

{{< highlight bash >}}
mkdir projects
touch projects/master_plan.txt
touch projects/backup_plan.txt
touch config.txt
{{< /highlight >}}

## Create Dockerfile

With `COPY` the final argument is the destination directory in the image, all other arguments are the source files and folders in the host filesystem.

{{< highlight bash >}}
# Build from base image
FROM ubuntu:latest

# Add Files And Folders To Image
COPY ["projects", "config.txt", "./special-projects/"]
{{< /highlight >}}

## Build Image From Dockerfile

Build the Dockerfile (`docker build`) in the current directory (`.`) and call the image chrisalbon/ubuntu:copy-example (`--tag chrisalbon/big-project:copy-example`).

{{< highlight bash >}}
docker build --tag chrisalbon/big-project:copy-example .
{{< /highlight >}}
```
Sending build context to Docker daemon  4.096kB
Step 1/2 : FROM ubuntu:latest
 ---> 1e4467b07108
Step 2/2 : COPY ["projects", "config.txt", "./special-projects/"]
 ---> f4613c3edb81
Successfully built f4613c3edb81
Successfully tagged chrisalbon/big-project:copy-example
```


## Run Docker Container From Image

Start and create (`docker run`) an interative (`-it`) Docker container called super-secret-project (`--name super-secret-project`) from the image called `chrisalbon/big-project:super-secret`. Remove the container after it stops (`-rm`)

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













