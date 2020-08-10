---
title: "TKTKT"
date: 2020-07-22T00:00:00-07:00
description: "TKTKT in Docker."
type: technical_note
draft: true
---

## View All Containers

View all (`-a`) containers (`docker ps`).

{{< highlight bash >}}
docker ps -a
{{< /highlight >}}
```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
985b01382d12        python:3.8-slim     "python3"                3 hours ago         Exited (0) 3 hours ago                          quirky_khorana
f4bc1146274f        python:3.8-slim     "python3"                3 hours ago         Exited (0) 3 hours ago                          busy_babbage
e9f9ace9b2c4        python:3.8-slim     "python3"                3 hours ago         Exited (0) 3 hours ago                          special-project
e86b5951906b        python:3.8-slim     "python3"                4 hours ago         Exited (0) 4 hours ago                          new-project
b76fb54ae278        python:3.8-slim     "python3"                4 hours ago         Exited (0) 4 hours ago                          python-project
2777ed414fa4        hello-world         "/hello"                 5 hours ago         Exited (0) 5 hours ago                          wonderful_lumiere
9b7575950524        ubuntu:latest       "/bin/bash"              33 hours ago        Exited (130) 33 hours ago                       big-project
924911f748e5        ubuntu:latest       "/bin/bash"              34 hours ago        Exited (0) 33 hours ago                         project
60655028c0d0        ubuntu:latest       "/bin/bash"              35 hours ago        Exited (0) 35 hours ago                         image-dev
5ca87a0c5c8b        nginx:latest        "/docker-entrypoint.…"   6 days ago          Exited (0) 6 days ago                           website
7052fd770e70        nginx:latest        "/docker-entrypoint.…"   6 days ago          Created                                         web
f104467b9c7f        nginx:latest        "/docker-entrypoint.…"   6 days ago          Exited (0) 6 days ago                           www
ad6edd9df5c9        tutum/lamp          "/run.sh"                13 days ago         Created                                         lamp-test
```

## Remove All Stopped Containers

List all (`-a`) Docker containers as numeric IDs (`-q`). Store this output as a variable (`$()`). Remove all the containers (`docker rm`) with those numeric IDs.

The list of ID's outputted will include running containers, however `docker rm` will not be able to remove running containers. Therefore the only containers are removed will be stopped containers.

{{< highlight bash >}}
docker rm $(docker ps -a -q)
{{< /highlight >}}
```
985b01382d12
f4bc1146274f
e9f9ace9b2c4
e86b5951906b
b76fb54ae278
2777ed414fa4
9b7575950524
924911f748e5
60655028c0d0
5ca87a0c5c8b
7052fd770e70
f104467b9c7f
ad6edd9df5c9
```

## View All Containers

View all (`-a`) containers (`docker ps`).

{{< highlight bash >}}
docker ps -a
{{< /highlight >}}
```
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

