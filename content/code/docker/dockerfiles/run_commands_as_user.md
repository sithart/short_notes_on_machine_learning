---
title: "Run Commands As A User"
date: 2020-07-22T00:00:00-07:00
description: "Run commands as a user using Dockerfiles."
type: technical_note
draft: False
---

## Create Dockerfile

{{< highlight bash >}}
# Build from base image
FROM ubuntu:latest

# Add a user named chris
RUN useradd -ms /bin/bash  chris

# Create a file
RUN touch before_user_command.txt

# Change to user "Chris"
USER chris

# Create a file
RUN touch ~/after_user_command.txt
{{< /highlight >}}

## Build Image From Dockerfile

Build the Dockerfile (`docker build`) in the current directory (`.`) and call the image chrisalbon/big-project:user-example (`--tag chrisalbon/big-project:user-example`).

{{< highlight bash >}}
docker build --tag chrisalbon/big-project:user-example .
{{< /highlight >}}
```
Sending build context to Docker daemon  4.608kB
Step 1/5 : FROM ubuntu:latest
 ---> 1e4467b07108
Step 2/5 : RUN useradd -ms /bin/bash  chris
 ---> Using cache
 ---> e4b9e6ef4c5a
Step 3/5 : RUN touch before_user_command.txt
 ---> Using cache
 ---> e1e32b44be33
Step 4/5 : USER chris
 ---> Using cache
 ---> 069afa90c79d
Step 5/5 : RUN touch ~/after_user_command.txt
 ---> Running in bb67374528f9
Removing intermediate container bb67374528f9
 ---> 2fb9292fcd9b
Successfully built 2fb9292fcd9b
Successfully tagged chrisalbon/big-project:user-example
```

## Run Docker Container From Image

Start and create (`docker run`) an interative (`-it`) Docker container from the image called `chrisalbon/big-project:user-example`. Remove the container after it stops (`-rm`)

{{< highlight bash >}}
docker run --rm -it chrisalbon/big-project:user-example
{{< /highlight >}}
```
chris@e0d25c2a9195:/$
```

## View Root Directory

View all files and folders (`ls`) that displays using long format and shows hidden files (`-al`) in the root directory.

{{< highlight bash >}}
ls -al
{{< /highlight >}}
```
total 56
drwxr-xr-x   1 root root 4096 Aug 25 02:10 .
drwxr-xr-x   1 root root 4096 Aug 25 02:10 ..
-rwxr-xr-x   1 root root    0 Aug 25 02:10 .dockerenv
-rw-r--r--   1 root root    0 Aug 25 02:04 before_user_command.txt
lrwxrwxrwx   1 root root    7 Jul 20 14:43 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 15 11:09 boot
drwxr-xr-x   5 root root  360 Aug 25 02:10 dev
drwxr-xr-x   1 root root 4096 Aug 25 02:10 etc
drwxr-xr-x   1 root root 4096 Aug 25 02:04 home
lrwxrwxrwx   1 root root    7 Jul 20 14:43 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Jul 20 14:43 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Jul 20 14:43 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Jul 20 14:43 libx32 -> usr/libx32
drwxr-xr-x   2 root root 4096 Jul 20 14:43 media
drwxr-xr-x   2 root root 4096 Jul 20 14:43 mnt
drwxr-xr-x   2 root root 4096 Jul 20 14:43 opt
dr-xr-xr-x 711 root root    0 Aug 25 02:10 proc
drwx------   2 root root 4096 Jul 20 14:57 root
drwxr-xr-x   1 root root 4096 Jul 24 14:38 run
lrwxrwxrwx   1 root root    8 Jul 20 14:43 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Jul 20 14:43 srv
dr-xr-xr-x  13 root root    0 Aug 25 02:07 sys
drwxrwxrwt   2 root root 4096 Jul 20 14:57 tmp
drwxr-xr-x   1 root root 4096 Jul 20 14:43 usr
drwxr-xr-x   1 root root 4096 Jul 20 14:57 var
```

Notice that `root` owns `before_user_command.txt`.

## View User Home Directory

View all files and folders (`ls`) that displays using long format and shows hidden files (`-al`)  in the directory `home/chris/`.

{{< highlight bash >}}
ls -al home/chris/
{{< /highlight >}}
```
total 20
drwxr-xr-x 1 chris chris 4096 Aug 25 02:10 .
drwxr-xr-x 1 root  root  4096 Aug 25 02:04 ..
-rw-r--r-- 1 chris chris  220 Feb 25 12:03 .bash_logout
-rw-r--r-- 1 chris chris 3771 Feb 25 12:03 .bashrc
-rw-r--r-- 1 chris chris  807 Feb 25 12:03 .profile
-rw-r--r-- 1 chris chris    0 Aug 25 02:10 after_user_command.txt
```

Notice that `chris` owns `after_user_command.txt`.