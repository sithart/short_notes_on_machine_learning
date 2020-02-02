---
title: "Prevent Ubuntu 18.06 And Nvidia Drivers From Updating"
author: "Chris Albon"
date: 2020-02-01T00:00:00-07:00
description: "Prevent Ubuntu 18.06 And Nvidia Drivers From Updating"
type: technical_note
draft: false
---

Ubuntu and NVIDIA's drivers are continually being developed. Normally this is a good thing, however an update from either can break a working deep learning environment and by default these updates are automatic.

After successfully setting up your deep learning system and testing that it works, it is recommended to freeze the system in place by preventing automatic updates of both the NVIDIA drivers and Ubuntu.

## Check NVIDIA Driver Version

`nvidia-smi`
```
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 440.44       Driver Version: 440.44       CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 108...  Off  | 00000000:41:00.0 Off |                  N/A |
|  0%   28C    P8    11W / 250W |    112MiB / 11176MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      1310      G   /usr/lib/xorg/Xorg                            41MiB |
|    0      1608      G   /usr/bin/gnome-shell                          67MiB |
+-----------------------------------------------------------------------------+
```

## View List Of All Installed Packages

`apt list --installed`
```
...
yelp/bionic,now 3.26.0-1ubuntu2 amd64 [installed]
yelp-xsl/bionic,bionic,now 3.20.1-4 all [installed]
zeitgeist-core/bionic,now 1.0-0.1ubuntu1 amd64 [installed]
zenity/bionic,now 3.28.1-1 amd64 [installed]
zenity-common/bionic,bionic,now 3.28.1-1 all [installed]
zip/bionic,now 3.0-11build1 amd64 [installed]
zlib1g/bionic,now 1:1.2.11.dfsg-0ubuntu2 amd64 [installed]
zlib1g-dev/bionic,now 1:1.2.11.dfsg-0ubuntu2 amd64 [installed,automatic]
```

## Freeze NVIDIA Drivers

Using The Package Names Found In The Output Above, Hold The NVIDIA Drivers At Current Version. The `440` seen below is the current version of the NVIDIA packages, yours will be different.

`sudo apt-mark hold nvidia-compute-utils-440 nvidia-dkms-440 nvidia-driver-440 nvidia-kernel-common-440 nvidia-kernel-source-440 nvidia-modprobe nvidia-prime nvidia-settings nvidia-utils-440`

## Prevent Ubuntu From Updating

Edit `/etc/apt/apt.conf.d/20auto-upgrades` in `sudo`. Then change

```
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Download-Upgradeable-Packages "1";
APT::Periodic::AutocleanInterval "0";
APT::Periodic::Unattended-Upgrade "1";
```

to 

```
APT::Periodic::Update-Package-Lists "0";
APT::Periodic::Download-Upgradeable-Packages "1";
APT::Periodic::AutocleanInterval "0";
APT::Periodic::Unattended-Upgrade "0";
```