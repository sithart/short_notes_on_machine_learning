---
title: "Set Container To Run A Bash Command On Start"
date: 2020-07-22T00:00:00-07:00
description: "Set a Docker container to run a bash command upon launch in Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/set_container_to_run_a_bash_command_on_start/]
---

## Create Docker Container With Entrypoint And Default Command

Create a Docker container (`docker container create`) called application (`--name application`) built of the `ubuntu:latest` image. Upon starting the container launches bash (`--entrypoint "/bin/bash"`) and runs `-c "echo 'hello world'"`.

{{< highlight bash >}}
docker container create --name application --entrypoint "/bin/bash" ubuntu:latest -c "echo 'hello world'"
{{< /highlight >}}
```
70a1a028a374e5c61007c01062c8be0f59a4406a89000ea0a59451553628a0bf
```

## Create New Image

Create a new image (`docker container commit`) from the `application` container called `new-application`. Add author info (`-a "Chris Albon"`) and a commit message (`-m "Added analysis file"`).

{{< highlight bash >}}
docker container commit -a "Chris Albon" -m "Added entrypoint and command" application new-application
{{< /highlight >}}
```
sha256:ce5f6bd0eb9f474ee8491d0e49e356260ef8daf591946539cf84201fd6253168
```

## Run New Image

Run the docker container (`docker container run`) called `new-application`.

{{< highlight bash >}}
docker container run new-application
{{< /highlight >}}
```
hello world
```