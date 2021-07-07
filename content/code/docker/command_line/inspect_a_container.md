---
title: "Inspect A Container"
date: 2020-07-22T00:00:00-07:00
description: "How to inspect a Docker container."
type: technical_note
draft: false
aliases: [/docker/command_line/inspect_a_container/]
---

## Create Dockerfile

{{< highlight bash >}}
# Build from base image
FROM ubuntu:latest
{{< /highlight >}}

## Build Image From Dockerfile

Build the Dockerfile (`docker build`) in the current directory (`.`) and call the image chrisalbon/ubuntu:ubuntu (`--tag chrisalbon/big-project:ubuntu`).

{{< highlight bash >}}
docker build --tag chrisalbon/big-project:ubuntu .
{{< /highlight >}}
```
Sending build context to Docker daemon  4.608kB
Step 1/1 : FROM ubuntu:latest
 ---> 1e4467b07108
Successfully built 1e4467b07108
Successfully tagged chrisalbon/big-project:ubuntu
```

## Inspect Container

Inspect the Docker container (`docker inspect`) called `chrisalbon/big-project:ubuntu`.

{{< highlight bash >}}
docker inspect chrisalbon/big-project:ubuntu
{{< /highlight >}}
```
 [
    {
        "Id": "sha256:1e4467b07108685c38297025797890f0492c4ec509212e2e4b4822d367fe6bc8",
        "RepoTags": [
            "chrisalbon/big-project:dockerhub-example",
            "chrisalbon/big-project:ubuntu",
            "chrisalbon/dockerhub-example:latest",
            "ubuntu:latest"
        ],
        "RepoDigests": [
            "chrisalbon/dockerhub-example@sha256:60f560e52264ed1cb7829a0d59b1ee7740d7580e0eb293aca2d722136edb1e24",
            "ubuntu@sha256:5d1d5407f353843ecf8b16524bc5565aa332e9e6a1297c73a92d3e754b8a636d"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2020-07-24T14:38:35.464294608Z",
        "Container": "9d62e8d762827123636cb28eacfed9975890fd659cac66adee63fc3a969bb8a9",
        "ContainerConfig": {
            "Hostname": "9d62e8d76282",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"/bin/bash\"]"
            ],
            "ArgsEscaped": true,
            "Image": "sha256:905a090e9b85447aff61cda51518fc1ab45af28e185981b70bc73dc9c03abf13",
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
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/bash"
            ],
            "ArgsEscaped": true,
            "Image": "sha256:905a090e9b85447aff61cda51518fc1ab45af28e185981b70bc73dc9c03abf13",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": null
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 73859057,
        "VirtualSize": 73859057,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/2568093d144427fdc762ef28596ad952d949ea82c596aa51b341700148606cab/diff:/var/lib/docker/overlay2/e614c9bb494c15b6daeab3dfdb452856e3c86ed7907a309521f170d0493528f5/diff:/var/lib/docker/overlay2/6a8472af32276e3c219f107c4155c5ff4a3187252a59d60396baab024e2d947a/diff",
                "MergedDir": "/var/lib/docker/overlay2/5bd20ad48160ce6825b8a34a52f675550dd0131982367fc8bd8a2b8e8157fec5/merged",
                "UpperDir": "/var/lib/docker/overlay2/5bd20ad48160ce6825b8a34a52f675550dd0131982367fc8bd8a2b8e8157fec5/diff",
                "WorkDir": "/var/lib/docker/overlay2/5bd20ad48160ce6825b8a34a52f675550dd0131982367fc8bd8a2b8e8157fec5/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:ce30112909569cead47eac188789d0cf95924b166405aa4b71fb500d6e4ae08d",
                "sha256:8eeb4a14bcb4379021c215017c94800a848a8203a8ce76aa1bd211d4c995f792",
                "sha256:a37e74863e723df4ddd599ef1b7d9a68e2301794a8c37c2370f8c2c8993ef72c",
                "sha256:095624243293a7dfdb582f8471d6e2d9d7772dd621bc57906b034c59f388ebac"
            ]
        },
        "Metadata": {
            "LastTagTime": "2020-09-17T20:49:53.323821952-07:00"
        }
    }
]
```