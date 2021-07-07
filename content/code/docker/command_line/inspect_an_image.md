---
title: "Inspect An Image"
date: 2020-07-22T00:00:00-07:00
description: "Inspect a Docker image."
type: technical_note
draft: false
aliases: [/docker/command_line/inspect_an_image/]
---

## Inspect Image

Inspect (`docker inspect`) the image called `python:3.8-slim`.

{{< highlight bash >}}
docker inspect python:3.8-slim
{{< /highlight >}}
```
[
    {
        "Id": "sha256:07ea617545cdb52d1b3e5c5002e83cd4a5f1207175111cc6d1722272099cb459",
        "RepoTags": [
            "python:3.8-slim"
        ],
        "RepoDigests": [
            "python@sha256:f7edd1bb431a224e7f4f3e23cbb22738e82f4895a6d28f86294ce006177360c3"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2020-08-05T08:23:20.747039147Z",
        "Container": "9dd453d5c0d64d80ecca0bd83665e08bf91c0ac293e57e55d6fc7bb123d14392",
        "ContainerConfig": {
            "Hostname": "9dd453d5c0d6",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568",
                "PYTHON_VERSION=3.8.5",
                "PYTHON_PIP_VERSION=20.2.1",
                "PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/5578af97f8b2b466f4cdbebe18a3ba2d48ad1434/get-pip.py",
                "PYTHON_GET_PIP_SHA256=d4d62a0850fe0c2e6325b2cc20d818c580563de5a2038f917e3cb0e25280b4d1"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"python3\"]"
            ],
            "ArgsEscaped": true,
            "Image": "sha256:1da6a87e8405ca89ea5233d60082ef0819f8e9754f6223dd8ff6d6a11df16765",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "DockerVersion": "18.09.7",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568",
                "PYTHON_VERSION=3.8.5",
                "PYTHON_PIP_VERSION=20.2.1",
                "PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/5578af97f8b2b466f4cdbebe18a3ba2d48ad1434/get-pip.py",
                "PYTHON_GET_PIP_SHA256=d4d62a0850fe0c2e6325b2cc20d818c580563de5a2038f917e3cb0e25280b4d1"
            ],
            "Cmd": [
                "python3"
            ],
            "ArgsEscaped": true,
            "Image": "sha256:1da6a87e8405ca89ea5233d60082ef0819f8e9754f6223dd8ff6d6a11df16765",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": null
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 112783396,
        "VirtualSize": 112783396,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/86f85240f474c467cd23db86b44217a96c2dddbc3c617a32ac95bb4365e2cc9a/diff:/var/lib/docker/overlay2/6b937eeee0bcbda330a191b60e068a5b76bec75a75ad0e03cc69ba2fce2a3645/diff:/var/lib/docker/overlay2/d7432e088b6cc65f15d131dac1347219ad9740aa64369ebdb1ea9311808d4230/diff:/var/lib/docker/overlay2/9aa04513309a3ef215dae999bc682c0a79c488c1dcd7b4a919f84e236af4fe75/diff",
                "MergedDir": "/var/lib/docker/overlay2/595dc264da79be71f11429d14878c0691848e54b42565723a7e2518c28473e99/merged",
                "UpperDir": "/var/lib/docker/overlay2/595dc264da79be71f11429d14878c0691848e54b42565723a7e2518c28473e99/diff",
                "WorkDir": "/var/lib/docker/overlay2/595dc264da79be71f11429d14878c0691848e54b42565723a7e2518c28473e99/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:d0f104dc0a1f9c744b65b23b3fd4d4d3236b4656e67f776fe13f8ad8423b955c",
                "sha256:2b99e24030638bb97d187a8266695a95cda7853c01aeb4700fbad54a4c80acc0",
                "sha256:98ff2784e9f5382c99cdeac9799e06a6f9c35a66de86005991d3261694495def",
                "sha256:1e441fe06d9010689dcdd9d65a7a586c56a73f2a849cb6c11d285570cece4556",
                "sha256:71c24c079ec4d72c91efa6c5a3ae476c2562b4efc72a5b9a5b3d3fd27152bc69"
            ]
```