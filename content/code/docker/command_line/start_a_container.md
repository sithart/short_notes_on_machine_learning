---
title: "Start A Container"
date: 2020-07-22T00:00:00-07:00
description: "Start A Container In Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/start_a_container/]
---

## Create Container

Create a Docker container (`docker create`) from the image `python:3.8-slim`. Then save the output as a variable (`CID=$()`).

This works because upon completion `docker create` outputs the unique container ID to `stout`.

{{< highlight bash >}}
CID=$(docker create python:3.8-slim)
{{< /highlight >}}

## Start Container

Start the Docker container (`docker start`) with the container ID specified by CID ($CID)

{{< highlight bash >}}
# With root privileges, start the Container that has 
# the container ID defined in the variable CID
docker start $CID
{{< /highlight >}}
```
f4bc1146274fb6f32f583824e1df58ed6187de7b979b7c843997d42eb86fdd11
```