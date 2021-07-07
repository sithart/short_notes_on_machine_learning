---
title: "Export All Files And Folders Out Of A Container"
date: 2020-07-22T00:00:00-07:00
description: "How to export all files and folders out of a container in Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/exporting_all_files_folders_out_of_a_container/]
---

## Run Detached Container

Create and start (`docker run`) the detached (`--detach`) the Docker image called special-project (`--name special-project`) based on the `python:3.8-slim` Docker image.

{{< highlight bash >}}
docker run --detach --name special-project python:3.8-slim
{{< /highlight >}}
```
427e7823c84bdb600ead8411fe3b6685ab7c8e5a000c9e30c136c977d557a55c
```

## Export All Files And Folders Out Of Container

Export all files and folders (`docker container export`) from the container `special-project` and save them into a file (`--output`) called `special-projects.tar`.

{{< highlight bash >}}
docker container export --output special-project.tar special-project
{{< /highlight >}}

A tar file has now been created with the container's complete filesystem.