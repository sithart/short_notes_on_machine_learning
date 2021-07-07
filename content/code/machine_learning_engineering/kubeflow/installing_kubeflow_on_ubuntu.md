---
title: "Installing Kubeflow On Ubuntu"
author: "Chris Albon"
date: 2020-06-23T00:00:00-07:00
description: "How to install Kubeflow locally on Ubuntu."
type: technical_note
draft: false
aliases: [/machine_learning_engineering/kubeflow/installing_kubeflow_on_ubuntu/]
---

In 2017, I built this [deep learning machine](https://pcpartpicker.com/user/chrisalbon/saved/yzLJVn) as a solution to my growing AWS bill. In 2020, I struggled to get this machine to run Kubeflow locally. Here are the instructions that worked for me.

Some of these instructions are based on this [Ubuntu.com tutorial](https://ubuntu.com/tutorials/deploy-kubeflow-ubuntu-windows-mac#3-install-microk8s).

## Turn On Virtualization On AMD Chipset

In BIOS, go to:

1. `M.I.T.`
2. `Advanced Frequency Settings`
2. `Advanced CPU Core Settings`
3. Set `SVM Mode` to **Enabled**

## Install MicroK8s

MicroK8s is a small version of Kubernetes that will work well locally.

{{< highlight bash >}}
sudo snap install microk8s --classic
{{< /highlight >}}

## Check MicroK8s Is Working

{{< highlight bash >}}
sudo microk8s status --wait-ready
{{< /highlight >}}

## Inspect MicroK8s Install

If the above command takes a long time, you can debug using `inspect`:

{{< highlight bash >}}
sudo microk8s inspect
{{< /highlight >}}

## Add Your User To The Micro8Ks Group Created By Micro8Ks

{{< highlight bash >}}
sudo usermod -a -G microk8s $USER
sudo chown -f -R $USER ~/.kube
{{< /highlight >}}

### Deploy Kubeflow

{{< highlight bash >}}
sudo microk8s.enable dns dashboard storage
{{< /highlight >}}

### Start Kubeflow

{{< highlight bash >}}
microk8s.enable kubeflow
{{< /highlight >}}

This is what you should see:

{{< highlight bash >}}
(base) chris@deeplearning:~$ microk8s.enable kubeflow
Enabling dns...
Enabling storage...
Enabling dashboard...
Enabling ingress...
Enabling metallb:10.64.140.43-10.64.140.49...
Waiting for DNS and storage plugins to finish setting up
Deploying Kubeflow...
Kubeflow deployed.
Waiting for operator pods to become ready.
Waited 0s for operator pods to come up, 34 remaining.
Waited 15s for operator pods to come up, 34 remaining.
Waited 30s for operator pods to come up, 33 remaining.
Waited 45s for operator pods to come up, 33 remaining.
Waited 60s for operator pods to come up, 32 remaining.
Waited 75s for operator pods to come up, 31 remaining.
Waited 90s for operator pods to come up, 31 remaining.
Waited 105s for operator pods to come up, 30 remaining.
Waited 120s for operator pods to come up, 30 remaining.
Waited 135s for operator pods to come up, 30 remaining.
Waited 150s for operator pods to come up, 30 remaining.
Waited 165s for operator pods to come up, 30 remaining.
Waited 180s for operator pods to come up, 28 remaining.
Waited 195s for operator pods to come up, 27 remaining.
Waited 210s for operator pods to come up, 25 remaining.
Waited 225s for operator pods to come up, 21 remaining.
Waited 240s for operator pods to come up, 16 remaining.
Waited 255s for operator pods to come up, 16 remaining.
Waited 270s for operator pods to come up, 15 remaining.
Waited 285s for operator pods to come up, 14 remaining.
Waited 300s for operator pods to come up, 13 remaining.
Waited 315s for operator pods to come up, 13 remaining.
Waited 330s for operator pods to come up, 11 remaining.
Waited 345s for operator pods to come up, 9 remaining.
Waited 360s for operator pods to come up, 8 remaining.
Waited 375s for operator pods to come up, 6 remaining.
Waited 390s for operator pods to come up, 4 remaining.
Waited 405s for operator pods to come up, 3 remaining.
Waited 420s for operator pods to come up, 2 remaining.
Operator pods ready.
Waiting for service pods to become ready.

Congratulations, Kubeflow is now available.
The dashboard is available at http://10.64.140.43.xip.io/

    Username: admin
    Password: AKO0X8OOHDU211OQZ71MURFS9BU7UN

To see these values again, run:

    microk8s juju config dex-auth static-username
    microk8s juju config dex-auth static-password
{{< /highlight >}}

You can go to Kubeflow's UI using the link and login informatin presented above.

## Shut Down Kubeflow

{{< highlight bash >}}
sudo microk8s disable kubeflow
{{< /highlight >}}