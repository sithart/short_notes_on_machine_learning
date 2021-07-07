---
title: "View Disk Information"
author: "Chris Albon"
date: 2018-07-16T00:00:00-07:00
description: "View disk information using the Linux command line."
type: technical_note
draft: false
aliases: [/linux/basics/view_disk_information/]
---

This is how you can view external hard drives on your Ubuntu system. `lshw` stands for ["list hardware"](https://linux.die.net/man/1/lshw).

## View Disk Information

{{< highlight markdown >}}
sudo lshw -C disk
{{< /highlight >}}
```
  *-disk                    
       description: ATA Disk
       product: Samsung SSD 850
       physical id: 0.0.0
       bus info: scsi@0:0.0.0
       logical name: /dev/sda
       version: 3B6Q
       serial: S3PJNF0JA08928L
       size: 931GiB (1TB)
       capabilities: gpt-1.00 partitioned partitioned:gpt
       configuration: ansiversion=5 guid=ef511d90-6a19-46f8-9510-08d164ad898a logicalsectorsize=512 sectorsize=512
```