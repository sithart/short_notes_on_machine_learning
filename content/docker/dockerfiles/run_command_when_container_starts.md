---
title: "Run Command When Container Starts"
date: 2020-07-22T00:00:00-07:00
description: "Run command when container starts using Dockerfiles."
type: technical_note
draft: False
---

## Create Dockerfile

You can use `ENTRYPOINT` and `CMD` to run a command when a container starts. `ENTRYPOINT` defines the program to run while `CMD` defines the argument to pass. Note that if `ENTRYPOINT` is not defined, `CMD` will send commands to `/bin/sh -c`

{{< highlight bash >}}
# Build from base image
FROM ubuntu:latest

# Maintainer label
LABEL maintainer="coder@chrisalbon.com"

# Ping Google.com five times
ENTRYPOINT ["/bin/echo"]
CMD ["Hello", "World"]
{{< /highlight >}}

## Build Image From Dockerfile

Build the Dockerfile (`docker build`) in the current directory (`.`) and call the image chrisalbon/ubuntu:hello-world (`--tag chrisalbon/ubuntu:hello-world`).

{{< highlight bash >}}
docker build --tag chrisalbon/ubuntu:hello-world .
{{< /highlight >}}
```
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM ubuntu:latest
 ---> 1e4467b07108
Step 2/4 : LABEL maintainer="coder@chrisalbon.com"
 ---> Using cache
 ---> 74a6f636b9c1
Step 3/4 : ENTRYPOINT ["/bin/echo"]
 ---> Running in d43915bb2075
Removing intermediate container d43915bb2075
 ---> b7c93aeb23d0
Step 4/4 : CMD ["Hello", "World"]
 ---> Running in 9dc2e4b32004
Removing intermediate container 9dc2e4b32004
 ---> b1ef4c66453f
Successfully built b1ef4c66453f
Successfully tagged chrisalbon/ubuntu:hello-world
```

## Run Docker Container From Image

Start and create (`docker run`) an interative (`-it`) Docker container from the image called `chrisalbon/ubuntu:hello-world`. Remove the container after it stops (`-rm`)

{{< highlight bash >}}
docker run --rm -it chrisalbon/ubuntu:hello-world
{{< /highlight >}}
```
Hello World
```