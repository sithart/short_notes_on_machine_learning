---
title: "Add Metadata"
date: 2020-07-22T00:00:00-07:00
description: "Add Metadata in Dockerfiles."
type: technical_note
draft: False
---

## Create Dockerfile

{{< highlight bash >}}
# Build from the Python 3.8 slim image
FROM python:3.8-slim

# Maintainer label
LABEL maintainer="coder@chrisalbon.com"

# Labels from http://label-schema.org/rc1/
LABEL org.label-schema.name="chrisalbon/python-slim-3.8"
LABEL org.label-schema.description="A test container for ChrisAlbon.com"
LABEL org.label-schema.url="https://chrisalbon.com/"

# Update packages
RUN apt-get update
{{< /highlight >}}

## Build Image From Dockerfile

Build the Dockerfile (`docker build`) in the current directory (`.`) and call the image chrisalbon/python-slim-3.8 (`--tag chrisalbon/python-slim-3.8`).

{{< highlight bash >}}
docker build --tag chrisalbon/python:updated .
{{< /highlight >}}
```
Sending build context to Docker daemon  2.048kB
Step 1/6 : FROM python:3.8-slim
 ---> 07ea617545cd
Step 2/6 : LABEL maintainer="coder@chrisalbon.com"
 ---> Running in 09b74adcac2e
Removing intermediate container 09b74adcac2e
 ---> f6807f2e0ec7
Step 3/6 : LABEL org.label-schema.name="chrisalbon/python-slim-3.8"
 ---> Running in 30d8b408f432
Removing intermediate container 30d8b408f432
 ---> 06d9cd2e6c12
Step 4/6 : LABEL org.label-schema.description="A test container for ChrisAlbon.com"
 ---> Running in 3e65c2a4cb49
Removing intermediate container 3e65c2a4cb49
 ---> 671c0bcf63b4
Step 5/6 : LABEL org.label-schema.url="https://chrisalbon.com/"
 ---> Running in c12017f760c0
Removing intermediate container c12017f760c0
 ---> 19e8a45c41c2
Step 6/6 : RUN apt-get update
 ---> Running in a9a53039186e
Get:1 http://deb.debian.org/debian buster InRelease [122 kB]
Get:2 http://security.debian.org/debian-security buster/updates InRelease [65.4 kB]
Get:3 http://deb.debian.org/debian buster-updates InRelease [51.9 kB]
Get:4 http://security.debian.org/debian-security buster/updates/main amd64 Packages [218 kB]
Get:5 http://deb.debian.org/debian buster/main amd64 Packages [7906 kB]
Get:6 http://deb.debian.org/debian buster-updates/main amd64 Packages [7868 B]
Fetched 8372 kB in 1s (6003 kB/s)
Reading package lists...
Removing intermediate container a9a53039186e
 ---> 1ac7fee0c377
Successfully built 1ac7fee0c377
Successfully tagged big-project:v2
```