---
title: "View Container Logs"
date: 2020-07-22T00:00:00-07:00
description: "View Container Logs In Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/view_container_logs/]
---

## Run Container

# With root privileges, run the docker image nginx:latest as a detached container and call it www

Create and start (`docker run`) a detached (`--detach`) Docker container called www (`--name www`) based on the image `nginx:latest`.

{{< highlight bash >}}
docker run --detach --name www nginx:latest
{{< /highlight >}}

## View Logs Of That Container

View the logs (`docker log`) of the container called `www`.

Anything written to stdout or stderr streams will appear in logs.

{{< highlight bash >}}
docker log www
{{< /highlight >}}
```
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
172.17.0.4 - - [25/Jul/2020:19:37:16 +0000] "GET / HTTP/1.1" 200 612 "-" "Wget" "-"
172.17.0.5 - - [25/Jul/2020:19:42:23 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:24 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:25 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:26 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:27 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:28 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:29 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:30 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:31 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:32 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:33 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:34 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:35 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:36 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:37 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:38 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:39 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:40 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:41 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:42 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:43 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:44 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:45 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:46 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:47 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:48 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:49 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:50 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:51 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:52 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:53 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:54 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:55 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:56 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:57 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:58 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:42:59 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:43:00 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:43:01 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:43:02 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:43:03 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:43:04 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
172.17.0.5 - - [25/Jul/2020:19:43:05 +0000] "GET / HTTP/1.0" 200 612 "-" "-" "-"
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: error: IPv6 listen already enabled
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Configuration complete; ready for start up

```