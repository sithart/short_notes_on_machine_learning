---
title: "Create Bucket"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to create a bucket on AWS S3."
type: technical_note
draft: false
---

## Create Bucket

Make a bucket (`mb`) on AWS S3 called `kicks-pasta-steer`. The bucket name you choose must be _globally_ unique, meaning nobody else in the world must have used that bucket name before.

{{< highlight markdown >}}
aws s3 mb s3://kicks-pasta-steer
{{< /highlight >}}
```
make_bucket: kicks-pasta-steer
```