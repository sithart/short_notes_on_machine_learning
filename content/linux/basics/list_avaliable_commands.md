---
title: "List Avaliable Commands"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "See list of avaliable commands in a system using the Linux command line."
type: technical_note
draft: false
---

We can see all avaliable commands for a system by listing the contents of the bin directory using `ls /bin`

## Show All Avaliable Commands
{{< highlight markdown >}}
ls /bin
{{< /highlight >}}
```
bash          cp                    fgrep       loadkeys    netcat            open                     setupcon         unicode_start
bunzip2       cpio                  findmnt     login       netstat           openvt                   sh               vdir
busybox       dash                  fuser       loginctl    nisdomainname     pidof                    sh.distrib       which
bzcat         date                  fusermount  lowntfs-3g  ntfs-3g           ping                     sleep            whiptail
bzcmp         dbus-cleanup-sockets  grep        ls          ntfs-3g.probe     ping6                    ss               ypdomainname
bzdiff        dbus-daemon           gunzip      lsblk       ntfs-3g.secaudit  plymouth                 static-sh        zcat
bzegrep       dbus-uuidgen          gzexe       lsmod       ntfs-3g.usermap   plymouth-upstart-bridge  stty             zcmp
bzexe         dd                    gzip        mkdir       ntfscat           ps                       su               zdiff
bzfgrep       df                    hostname    mknod       ntfsck            pwd                      sync             zegrep
bzgrep        dir                   ip          mktemp      ntfscluster       rbash                    tailf            zfgrep
bzip2         dmesg                 kbd_mode    more        ntfscmp           readlink                 tar              zforce
bzip2recover  dnsdomainname         kill        mount       ntfsdump_logfile  red                      tempfile         zgrep
bzless        domainname            kmod        mountpoint  ntfsfix           rm                       touch            zless
bzmore        dumpkeys              less        mt          ntfsinfo          rmdir                    true             zmore
cat           echo                  lessecho    mt-gnu      ntfsls            rnano                    udevadm          znew
chgrp         ed                    lessfile    mv          ntfsmftalloc      running-in-container     ulockmgr_server
chmod         egrep                 lesskey     nano        ntfsmove          run-parts                umount
chown         false                 lesspipe    nc          ntfstruncate      sed                      uname
chvt          fgconsole             ln          nc.openbsd  ntfswipe          setfont                  uncompress
```