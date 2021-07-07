---
title: "Add Comments"
date: 2020-07-22T00:00:00-07:00
description: "Add comments in Dockerfiles."
type: technical_note
draft: False
---

## Create Dockerfile

Comment Dockerfiles by starting a line with `#`.

{{< highlight bash >}}
# Build from the Python 3.8 slim image
FROM python:3.8-slim

# Update packages
RUN apt-get update
{{< /highlight >}}

## Build Image From Dockerfile

Build the Dockerfile (`docker build`) in the current directory (`.`) and call the image chrisalbon/python:updated (`--tag chrisalbon/python:updated`).

{{< highlight bash >}}
docker build --tag chrisalbon/python:updated .
{{< /highlight >}}
```
Sending build context to Docker daemon  4.096kB
Step 1/2 : FROM python:3.8-slim
 ---> 07ea617545cd
Step 2/2 : RUN apt-get update
 ---> Using cache
 ---> bfa108e3dff9
Successfully built bfa108e3dff9
Successfully tagged python:updated
```