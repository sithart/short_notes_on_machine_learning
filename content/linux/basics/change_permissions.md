---
title: "Change Permissions"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to change the permissions of a file or directory using the Linux command line."
type: technical_note
draft: false
---

To change the permissions of a file or directory we use the `chmod` command. `chmod` takes three digits, each one representing the permissions for the user, group, and everyone. Thus, `741` would mean:

- The user can read, write, and execute (`7`)
- The group can read only (`4`)
- Everyone can execute (`1`)

Here is a handy list translating the octal numbering system to permissions:

- `0` - no permission
- `1` - execute
- `2` - write
- `3` - write and execute
- `4` - read
- `5` - read and execute
- `6` - read and write
- `7` - read, write, and execute

## Create File

{{< highlight markdown >}}
touch company_data.csv
{{< /highlight >}}

## View File Permissions

{{< highlight markdown >}}
ls -l company_data.csv
{{< /highlight >}}
```
-rw-rw-r-- 1 chris chris 0 Jul 29 12:55 company_data.csv
```

## Change File Permissions

`chmod 600` means the user can read and write, but the group and everyone else has no permission.

{{< highlight markdown >}}
chmod 600 company_data.csv
{{< /highlight >}}

## View File Permissions

{{< highlight markdown >}}
ls -l company_data.csv
{{< /highlight >}}
```
-rw------- 1 chris chris 0 Jul 29 12:55 company_data.csv
```