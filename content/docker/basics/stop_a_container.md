---
title: "Stop A Container"
date: 2020-07-22T00:00:00-07:00
description: "Stop a Container In Docker."
type: technical_note
draft: false
---

## Run Container

Create and start (`docker run`) a detached (`--detach`) Docker container called secret-project (`--name secret-project`) based on the Docker image `python:3.8-slim`.

{{< highlight bash >}}
docker run --detach --name secret-project python:3.8-slim
{{< /highlight >}}

## Stop Container

Stop (`docker stop`) the Docker container called `secret-project`.

{{< highlight bash >}}
docker stop secret-project
{{< /highlight >}}
```
secret-project
```