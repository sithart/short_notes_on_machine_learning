---
title: "Modify File Permissions"
author: "Chris Albon"
date: 2018-07-16T00:00:00-07:00
description: "Modify file permissions using the Linux command line."
type: technical_note
draft: false
aliases: [/linux/basics/modify_file_permissions/]
---

## Make File

{{< highlight markdown >}}
touch file.txt
{{< /highlight >}}

## View File Permissions

{{< highlight markdown >}}
ls -al file.txt
{{< /highlight >}}
```
-rw-r--r--  1 chris chris    0 Jul 18 16:59 file.txt
```

## Add Execute Permission To User

{{< highlight markdown >}}
chmod u+x file.txt
{{< /highlight >}}

## Add Write Permission To Group

{{< highlight markdown >}}
chmod g+w file.txt
{{< /highlight >}}

## Remove Read Permission From World

Note: "World" in this case means every user who isn't file's owner or in the file's owner usergroup.

{{< highlight markdown >}}
chmod o-r file.txt
{{< /highlight >}}

## View File Permissions

{{< highlight markdown >}}
ls -al file.txt
{{< /highlight >}}
```
-rwxrw---- 1 chris chris 0 Jul 18 16:59 file.txt
```