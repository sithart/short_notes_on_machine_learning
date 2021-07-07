---
title: "Publish To Docker Hub"
date: 2020-07-22T00:00:00-07:00
description: "Run commands as a user using Dockerfiles."
type: technical_note
draft: False
---

## Create Dockerfile

{{< highlight bash >}}
# Build from base image
FROM ubuntu:latest
{{< /highlight >}}

## Build Image From Dockerfile

Build the Dockerfile (`docker image build`) in the current directory (`.`) and call the image chrisalbon/big-project:dockerhub-example (`--tag chrisalbon/big-project:dockerhub-example`).

{{< highlight bash >}}
docker image build --tag chrisalbon/dockerhub-example .
{{< /highlight >}}
```
Sending build context to Docker daemon  4.608kB
Step 1/1 : FROM ubuntu:latest
 ---> 1e4467b07108
Successfully built 1e4467b07108
Successfully tagged chrisalbon/dockerhub-example:latest
```

## Log In To Docker Hub

{{< highlight bash >}}
docker login
{{< /highlight >}}
```
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: BananaBoatBoy
Password: 
WARNING! Your password will be stored unencrypted in /home/chris/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

## Publish To Docker Hub

Publish the Docker image (`docker image push`) `chrisalbon/dockerhub-example` to Docker Hub.

{{< highlight bash >}}
docker image push chrisalbon/dockerhub-example
{{< /highlight >}}
```
The push refers to repository [docker.io/chrisalbon/dockerhub-example]
095624243293: Mounted from library/ubuntu 
a37e74863e72: Mounted from library/ubuntu 
8eeb4a14bcb4: Mounted from library/ubuntu 
ce3011290956: Mounted from library/ubuntu 
latest: digest: sha256:60f560e52264ed1cb7829a0d59b1ee7740d7580e0eb293aca2d722136edb1e24 size: 1152
```