---
title: "Create An Image"
date: 2020-07-22T00:00:00-07:00
description: "Create a new image in Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/create_an_image/]
---

## Create Docker Container

Create and start a docker container (`docker container run`) that is interactive (`-it`), called "new-project" (`--name new-project`), and is based on `python:3.8-slim`. Then run `/bin/bash` to get a terminal.

{{< highlight bash >}}
docker container run -it --name new-project python:3.8-slim /bin/bash
{{< /highlight >}}
```
Unable to find image 'python:3.8-slim' locally
3.8-slim: Pulling from library/python
bf5952930446: Pull complete 
385bb58d08e6: Pull complete 
ab14b629693d: Pull complete 
7a5d07f2fd13: Pull complete 
56745e40505a: Pull complete 
Digest: sha256:f7edd1bb431a224e7f4f3e23cbb22738e82f4895a6d28f86294ce006177360c3
Status: Downloaded newer image for python:3.8-slim
root@094e51f501f2:/#
```

## Create File In Container

Create a file (`touch`) called `analysis.py`.

{{< highlight bash >}}
touch analysis.py
{{< /highlight >}}

## Exit Container
{{< highlight bash >}}
exit
{{< /highlight >}}

## Create New Image

Create a new image (`docker container commit`) from the `new-project` container called `new-project-with-analysis-file`. Add author info (`-a "Chris Albon"`) and a commit message (`-m "Added analysis file"`)

{{< highlight bash >}}
docker container commit -a "Chris Albon" -m "Added analysis file" new-project new-project-with-analysis-file
{{< /highlight >}}
```
sha256:0684311a4db5010d334dc524112c83daa891dc3d31edd720b372edfd7b1ab94a
```
