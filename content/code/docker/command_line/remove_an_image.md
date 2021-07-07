---
title: "Remove An Image"
date: 2020-07-22T00:00:00-07:00
description: "Remove a docker image."
type: technical_note
draft: false
aliases: [/docker/command_line/remove_an_image/]
---

## Pull Down An Image From A Docker Repository

Pull down the docker image (`docker pull`) called `python:3.8-slim` from Docker.io (the default registry).

{{< highlight bash >}}
docker pull python:3.8-slim
{{< /highlight >}}
```
3.8-slim: Pulling from library/python
Digest: sha256:f7edd1bb431a224e7f4f3e23cbb22738e82f4895a6d28f86294ce006177360c3
Status: Image is up to date for python:3.8-slim
docker.io/library/python:3.8-slim
```

## Remove Docker Image

Remove the docker image `docker rmi` called `python:3.8-slim`

{{< highlight bash >}}
docker rmi python:3.8-slim
{{< /highlight >}}
```
Untagged: python:3.8-slim
Untagged: python@sha256:f7edd1bb431a224e7f4f3e23cbb22738e82f4895a6d28f86294ce006177360c3
```