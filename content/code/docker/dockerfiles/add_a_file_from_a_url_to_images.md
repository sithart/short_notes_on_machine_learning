---
title: "Add A File From A URL To Images"
date: 2020-07-22T00:00:00-07:00
description: "Add a file from a URL to images using Dockerfiles."
type: technical_note
draft: False
---

## Create Dockerfile

{{< highlight bash >}}
# Build from base image
FROM ubuntu:latest

# Add file from URL to tmp directory
ADD ["https://raw.githubusercontent.com/chrisalbon/notes/master/LICENSE.txt", "/tmp/"]
{{< /highlight >}}

## Build Image From Dockerfile

Build the Dockerfile (`docker build`) in the current directory (`.`) and call the image chrisalbon/ubuntu:file-from-url (`--tag chrisalbon/ubuntu:file-from-url`).

{{< highlight bash >}}
docker build --tag chrisalbon/ubuntu:file-from-url .
{{< /highlight >}}
```
Sending build context to Docker daemon  4.608kB
Step 1/2 : FROM ubuntu:latest
 ---> 1e4467b07108
Step 2/2 : ADD ["https://raw.githubusercontent.com/chrisalbon/notes/master/LICENSE.txt", "/tmp/"]
Downloading     223B
 ---> 9ef46cc7fd3a
Successfully built 9ef46cc7fd3a
Successfully tagged chrisalbon/ubuntu:file-from-url
```

## Run Docker Container From Image

Start and create (`docker run`) an interative (`-it`) Docker container from the image called `chrisalbon/ubuntu:file-from-url`. Remove the container after it stops (`-rm`)

{{< highlight bash >}}
docker run --rm -it chrisalbon/ubuntu:file-from-url
{{< /highlight >}}
```
root@7a5f4dbb0dc7:/#
```

## View Destination Directory

View all files and folders (`ls`) that displays using long format and shows hidden files (`-al`) in the directory `tmp`.

{{< highlight bash >}}
ls -al tmp/
{{< /highlight >}}
```
total 12
drwxrwxrwt 1 root root 4096 Aug 20 00:38 .
drwxr-xr-x 1 root root 4096 Aug 20 00:42 ..
-rw------- 1 root root  223 Jan  1  1970 LICENSE.txt
```