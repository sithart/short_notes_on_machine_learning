---
title: "Saving An Image As A File"
date: 2020-07-22T00:00:00-07:00
description: "Saving a Docker image as a file."
type: technical_note
draft: false
aliases: [/docker/command_line/saving_an_image_as_a_file/]
---

## Pull Down An Image From Docker Registry

Pull down the docker image (`docker pull`) called `python:3.8-slim` from Docker.io (the default registry).

{{< highlight bash >}}
docker pull python:3.8-slim
{{< /highlight >}}
```
3.8-slim: Pulling from library/python
Digest: sha256:f7edd1bb431a224e7f4f3e23cbb22738e82f4895a6d28f86294ce006177360c3
Status: Image is up to date for python:3.8-slim
docker.io/library/python:3.8-slim
```

## Save Image As A File

Save the Docker image (`docker save`) `python:3.8-slim` to the file (`-o`) named `python-3.8.tar`.

{{< highlight bash >}}
docker save -o python-3.8.tar python:3.8-slim
{{< /highlight >}}

## Check File Exists

View all files and folders (`ls`) that displays using long format and shows hidden files (`-al`)

{{< highlight bash >}}
ls -al
{{< /highlight >}}
```
total 1432
drwxrwxr-x 2 chris chris    4096 Aug  1 20:39 ./
drwxr-xr-x 3 chris chris    4096 Jul 25 12:22 ../
-rw------- 1 root  root  1451008 Aug  1 20:39 python-3.8.tar
```