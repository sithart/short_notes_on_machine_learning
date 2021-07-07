---
title: "Automatically Generate Human-Readable Container Names"
date: 2020-07-22T00:00:00-07:00
description: "Automatically Generate Human-Readable Container Names In Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/automatically_generate_human_readable_container_names/]
---

If you don't define a name for a docker container an automatically generated name will be created.

## Create Three Containers

Create and start (`docker run`) a detacted (`--detach`) container using the `nginx:latest` Docker image. Run this three times.

{{< highlight bash >}}
docker run --detach nginx:latest
docker run --detach nginx:latest
docker run --detach nginx:latest
{{< /highlight >}}
```
6b29f78dbf01f7642cca1c54f69e8c068e6048536ef3307cd2960d56192ca11
495ee8ab187a60a9a4f2ecbe40f9de944d597a9afec1be43826249609541d3b
6a96b04886182535b63dfe46111644626ff2f036b3c4cac6c9908100d27b2719
```

## View Automatically Generated Names

Show the Docker containers that are running (`docker ps`).

Add (`-a`) to view all containers.

{{< highlight bash >}}
docker ps
{{< /highlight >}}
```
CONTAINER ID        IMAGE                       COMMAND                  CREATED             STATUS              PORTS               NAMES
6a96b0488618        nginx:latest                "/docker-entrypoint.…"   4 seconds ago       Up 2 seconds        80/tcp              nifty_antonelli
495ee8ab187a        nginx:latest                "/docker-entrypoint.…"   6 seconds ago       Up 4 seconds        80/tcp              silly_ramanujan
6b29f78dbf01        nginx:latest                "/docker-entrypoint.…"   8 seconds ago       Up 7 seconds        80/tcp              dazzling_diffie
```

In this example, the three automatically generated human-readable names are `nifty_antonelli`, `silly_ramanujan`, and `dazzling_diffie`.