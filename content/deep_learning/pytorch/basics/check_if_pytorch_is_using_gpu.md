---
title: "Check If PyTorch Is Using The GPU"
author: "Chris Albon"
date: 2020-02-01T00:00:00-07:00
description: "Check if PyTorch is using the GPU instead of a CPU"
type: technical_note
draft: false
---

I find this is always the first thing I want to run when setting up a deep learning environment, whether a desktop machine or on AWS. These commands simply load PyTorch and check to make sure PyTorch can use the GPU.

## Preliminaries

{{< highlight python >}}
# Import PyTorch
import torch
{{< /highlight >}}

## Check If There Are Multiple Devices (i.e. GPU cards)

{{< highlight python >}}
# How many GPUs are there?
print(torch.cuda.device_count())
{{< /highlight >}}
```
1
```

## Check Which Is The Current GPU?

{{< highlight python >}}
# Which GPU Is The Current GPU?
print(torch.cuda.current_device())
{{< /highlight >}}
```
0
```

## What Is The Name Of The Current GPU?

{{< highlight python >}}
# Get the name of the current GPU
print(torch.cuda.get_device_name(torch.cuda.current_device()))
{{< /highlight >}}
```
GeForce GTX 1080 Ti
```

## Is PyTorch Using A GPU?

{{< highlight python >}}
# Is PyTorch using a GPU?
print(torch.cuda.is_available())
{{< /highlight >}}
```
True
```