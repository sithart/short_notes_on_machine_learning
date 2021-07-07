---
title: "Stop A Container"
date: 2020-07-22T00:00:00-07:00
description: "Stop a Container In Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/stop_a_container/]
---

Don't use `docker kill`. It forces the process to stop without giving it a chance to do clean-up in the system. Instead use `docker stop`.

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