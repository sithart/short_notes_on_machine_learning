---
title: "Zip And Unzip Directories"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to zip and unzip Directories using the Linux command line."
type: technical_note
draft: false
---

## Make Directory

{{< highlight markdown >}}
mkdir regiment_data
{{< /highlight >}}

## Make Files In Directory

{{< highlight markdown >}}
touch regiment_data/battles.txt regiment_data/regiment.txt
{{< /highlight >}}

## Zip Directory

In the code below, we compress (`zip`) the `regiment_data` directory into the file `regiment.zip`. Note that `-r` means that we want to not only zip the directory but also its contents (which is almost always the case)
.
{{< highlight markdown >}}
zip -r regiment.zip regiment_data
{{< /highlight >}}
```
  adding: regiment_data/ (stored 0%)
  adding: regiment_data/battles.txt (stored 0%)
  adding: regiment_data/regiment.txt (stored 0%)
```

## View Directory Contents

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 8
drwxrwxr-x 2 chris chris 4096 Jul 31 13:39 regiment_data
-rw-rw-r-- 1 chris chris  536 Jul 31 13:39 regiment.zip
```

## Delete Directory

{{< highlight markdown >}}
rm -rf regiment_data
{{< /highlight >}}
```
total 8
drwxrwxr-x 2 chris chris 4096 Jul 31 13:39 regiment_data
-rw-rw-r-- 1 chris chris  536 Jul 31 13:39 regiment.zip
```

## Unzip Directory

{{< highlight markdown >}}
unzip regiment.zip
{{< /highlight >}}
```
Archive:  regiment.zip
   creating: regiment_data/
 extracting: regiment_data/battles.txt
 extracting: regiment_data/regiment.txt
```

## View Directory Contents

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 8
drwxrwxr-x 2 chris chris 4096 Jul 31 13:39 regiment_data
-rw-rw-r-- 1 chris chris  536 Jul 31 13:39 regiment.zip
```