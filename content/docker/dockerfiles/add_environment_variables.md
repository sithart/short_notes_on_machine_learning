---
title: "Add Environment Variables"
date: 2020-07-22T00:00:00-07:00
description: "Add environment variables in Dockerfiles."
type: technical_note
draft: False
---

## Create Dockerfile

{{< highlight docker >}}
# Build from ubuntu:latest
FROM ubuntu:latest

# Create a environment variable called db_name
ENV db_name="staff_database"

# Create a environment variable called db_password
ENV db_password "legendofkorra"
{{< /highlight >}}

## Build Image From Dockerfile

Build the Dockerfile (`docker build`) in the current directory (`.`) and call the image chrisalbon/big-project:v4 (`--tag chrisalbon/big-project:v4`).

{{< highlight bash >}}
docker build --tag chrisalbon/big-project:v4 .
{{< /highlight >}}
```
Sending build context to Docker daemon  2.048kB
Step 1/3 : FROM ubuntu:latest
 ---> 1e4467b07108
Step 2/3 : ENV db_name="staff_database"
 ---> Running in 6dfe7174912d
Removing intermediate container 6dfe7174912d
 ---> 7ae6665fd84c
Step 3/3 : ENV db_password "legendofkorra"
 ---> Running in f37d4ad7408b
Removing intermediate container f37d4ad7408b
 ---> f4ac811b0c45
Successfully built f4ac811b0c45
Successfully tagged chrisalbon/big-project:v4
```

## Run Docker Container From Image

Create and start (`docker container run`) an interactive (`-it`) container named project_v4 (`--name project_v4`) from the image called `chrisalbon/big-project:v4` and then run `/bin/bash`.

{{< highlight bash >}}
docker container run -it --name project_v4 chrisalbon/big-project:v4 /bin/bash
{{< /highlight >}}
```
root@20b64531c6c9:/#
```

## View Environment Variable

Print (`echo`) the variable `$db_name`.

{{< highlight bash >}}
echo $db_name
{{< /highlight >}}
```
staff_database
```