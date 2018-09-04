---
title: "Search Filenames"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to search file names using the Linux command line."
type: technical_note
draft: false
---

Often we want to find a file on our system. The `locate` command offers a quick method for searching for all files in the system containing a string. In our example, we look for all files with `bashrc` in the name.

## Search Filenames In System

{{< highlight markdown >}}
locate bashrc
{{< /highlight >}}
```
/etc/bash.bashrc
/etc/skel/.bashrc
/home/chris/.bashrc
/home/chris/.bashrc-anaconda3.bak
/home/chris/anaconda3/lib/python3.6/site-packages/pexpect/bashrc.sh
/home/chris/anaconda3/pkgs/pexpect-4.2.1-py36h3b9d41b_0/lib/python3.6/site-packages/pexpect/bashrc.sh
/usr/share/base-files/dot.bashrc
/usr/share/doc/adduser/examples/adduser.local.conf.examples/bash.bashrc
/usr/share/doc/adduser/examples/adduser.local.conf.examples/skel/dot.bashrc
```

Note that `locate` might not find recently created files. This is because the database of filenames `locate` uses is only generated periodically. We can update this database manually using `sudo updatedb`.