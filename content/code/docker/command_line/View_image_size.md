---
title: "View Image Size"
date: 2020-07-22T00:00:00-07:00
description: "View image size in Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/View_image_size/]
---

## View Image Size

List (`ls`) all (`-a`) Docker images (`docker image`).

{{< highlight bash >}}
docker image ls -a
{{< /highlight >}}
```
REPOSITORY                                                         TAG                            IMAGE ID            CREATED             SIZE
new-application                                          latest                         ce5f6bd0eb9f        About an hour ago   73.9MB
new-project-with-analysis-file                           latest                         0684311a4db5        34 hours ago        113MB
...
```