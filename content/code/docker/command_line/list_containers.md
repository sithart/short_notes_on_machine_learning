---
title: "List Containers"
date: 2020-07-22T00:00:00-07:00
description: "List Containers In Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/list_containers/]
---

## List Containers

View all (`-a`) containers (`docker ps`)

{{< highlight bash >}}
docker ps -a
{{< /highlight >}}
```
[sudo] password for chris: 
CONTAINER ID        IMAGE                       COMMAND                  CREATED             STATUS              PORTS               NAMES
b622067d595e        dockerinaction/ch2_agent    "/watcher/watcher.sh"    2 minutes ago       Up 2 minutes                            agent
4263374fbc42        busybox:1.29                "/bin/sh"                8 minutes ago       Up 8 minutes                            web_test
fecff8afca16        dockerinaction/ch2_mailer   "/mailer/mailer.sh"      11 minutes ago      Up 11 minutes       33333/tcp           mailer
db1be25177d3        nginx:latest                "/docker-entrypoint.…"   21 minutes ago      Up 21 minutes       80/tcp              www
```

- `CONTAINER ID`: ID of the container
- `IMAGE`: Image used by the container
- `COMMAND`: Command executed in the container
- `CREATED`: When the container was created
- `STATUS`: Length of time the container as been running
- `PORTS`: Port exposed by the container
- `NAMES`: Name of the container