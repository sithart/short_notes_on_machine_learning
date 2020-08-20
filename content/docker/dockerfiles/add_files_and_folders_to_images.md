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
mkdir projects/secret-projects
touch config.txt
{{< /highlight >}}

## Create Dockerfile

With `COPY` the final argument is the destination directory in the image, all other arguments are the source files and folders in the host filesystem.

{{< highlight bash >}}
# Build from base image
FROM ubuntu:latest

# Add files and folders to image
COPY ["projects", "config.txt", "./special-projects/"]
{{< /highlight >}}

## Build Image From Dockerfile

Build the Dockerfile (`docker build`) in the current directory (`.`) and call the image chrisalbon/ubuntu:copy-example (`--tag chrisalbon/big-project:copy-example`).

{{< highlight bash >}}
docker build --tag chrisalbon/big-project:copy-example .
{{< /highlight >}}
```
Sending build context to Docker daemon  4.608kB
Step 1/2 : FROM ubuntu:latest
 ---> 1e4467b07108
Step 2/2 : COPY ["projects", "config.txt", "./special-projects/"]
 ---> 487c17de4145
Successfully built 487c17de4145
Successfully tagged chrisalbon/big-project:copy-example
```

## Run Docker Container From Image

Start and create (`docker run`) an interative (`-it`) Docker container called copy-example (`--name copy-example`) from the image called `chrisalbon/big-project:copy-example`. Open a shell (`/bin/bash`). Remove the container after it stops (`-rm`)

{{< highlight bash >}}
docker container run -it --name copy-example chrisalbon/big-project:copy-example /bin/bash
{{< /highlight >}}
```
root@607a348aad51:/#
```

## View Destination Directory

View all files and folders (`ls`) that displays using long format and shows hidden files (`-al`) in the directory `special-projects`.

{{< highlight bash >}}
ls -al /special-projects
{{< /highlight >}}
```
total 12
drwxr-xr-x 3 root root 4096 Aug 19 05:14 .
drwxr-xr-x 1 root root 4096 Aug 19 05:15 ..
-rw-rw-r-- 1 root root    0 Aug 19 04:42 backup_plan.txt
-rw-rw-r-- 1 root root    0 Aug 19 04:42 config.txt
-rw-rw-r-- 1 root root    0 Aug 19 04:41 master_plan.txt
drwxrwxr-x 2 root root 4096 Aug 19 05:12 secret-projects
```

Notice two things:

1. Multiple source directories were placed in a single destination directory.
2. All files and directories have their ownership set to `root`. After the `COPY` line in the Dockerfile, you can use a `RUN` line to change file ownerships and permissions.