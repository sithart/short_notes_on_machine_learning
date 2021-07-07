---
title: "Use Environment Variables"
date: 2020-07-22T00:00:00-07:00
description: "Use Environment Variables In Docker."
type: technical_note
draft: false
aliases: [/docker/command_line/use_environment_variables/]
---

This is how you can pass environment variables into Docker containers.

## Create Environment Variables

{{< highlight bash >}}
DB_NAME="staff_database"
DB_PASSWORD="funny cat dog mouse"
{{< /highlight >}}

## Create Container With Environment Variables

Create and start (`docker run`) Docker based on the Docker image `python:3.8-slim`. The container has access to two environment variables, DB_NAME and DB_PASSWORD (`--env DB_NAME --env DB_PASSWORD`).

{{< highlight bash >}}
docker run --env DB_NAME --env DB_PASSWORD python:3.8-slim
{{< /highlight >}}