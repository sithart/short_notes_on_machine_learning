---
title: "Rename A Container"
date: 2020-07-22T00:00:00-07:00
description: "Rename a Container In Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/rename_a_container/]
---

## Run Container

Create and start (`docker run`) a detached (`--detach`) Docker container called python-project (`-name python-project`) from the image `python:3.8-slim`.

{{< highlight bash >}}
docker run --detach --name python-project python:3.8-slim
{{< /highlight >}}
```
Unable to find image 'python:3.8-slim' locally
3.8-slim: Pulling from library/python
Digest: sha256:f7edd1bb431a224e7f4f3e23cbb22738e82f4895a6d28f86294ce006177360c3
Status: Downloaded newer image for python:3.8-slim
b76fb54ae278dc9ba951c4bd1826a37389e2c5a32b82914d95bcfea9e8731529
```

## Rename Container

Rename (`docker rename`) the Docker container `python-project` to `python-production-application`.

{{< highlight bash >}}
docker rename python-project python-production-application
{{< /highlight >}}