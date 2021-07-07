---
title: "Restart A Container"
date: 2020-07-22T00:00:00-07:00
description: "Restart A Container In Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/restart_a_container/]
---

## Run Container

Create and start (`docker run`) a detached (`--detach`) Docker container called new-project (`--name new-project`) based on the `python:3.8-slim` image.

{{< highlight bash >}}
docker run --detach --name new-project python:3.8-slim
{{< /highlight >}}
```
e86b5951906b8a1f0ee0bf9f78adf66fcb16f06d89be5282eec5344c498f365e
```

## Restart That Container

Restart (`docker restart`) the Docker container called `new-project`.

{{< highlight bash >}}
docker restart new-project
{{< /highlight >}}
```
new-project
```