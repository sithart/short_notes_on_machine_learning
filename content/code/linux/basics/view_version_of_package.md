---
title: "View The Version Of A Package"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to view the version of a package using the Linux command line."
type: technical_note
draft: false
aliases: [/linux/basics/view_version_of_package/]
---

## View Version Of Package

From the internal database, show (`apt-cache show`) the version (`grep ^Version`) of `docker`.

{{< highlight markdown >}}
apt-cache show docker | grep ^Version
{{< /highlight >}}
```
Version: 1.5-1build1
```