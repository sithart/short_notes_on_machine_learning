---
title: "Automatically Restart Containers"
date: 2020-07-22T00:00:00-07:00
description: "Automatically restart containers in Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/automatically_restart_containers/]
---

## Create Container

Create and run (`docker run`) a detacted container (`--detach`) that will automatically restart (`--restart`) using the `nginx:latest` Docker image.

{{< highlight bash >}}
docker run --detach --restart always nginx:latest
{{< /highlight >}}
```
[sudo] password for chris: 
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
```