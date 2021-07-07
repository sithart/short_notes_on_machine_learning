---
title: "Run A Detached Container"
date: 2020-07-22T00:00:00-07:00
description: "Run A Detached Container In Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/run_a_detached_container/]
---

## Run Detached Container

Create and start (`docker run`) the detached (`--detach`) the Docker image called special-project (`--name special-project`) based on the `python:3.8-slim` Docker image.

{{< highlight bash >}}
docker run --detach --name special-project python:3.8-slim
{{< /highlight >}}
```
e9f9ace9b2c4b8d5fc06a5b18ce7ea89ff5b2322233baf6e4a3154294a389422
```