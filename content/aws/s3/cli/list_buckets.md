---
title: "List Buckets"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to list buckets on AWS S3."
type: technical_note
draft: false
---

## Create First Bucket

Make a bucket (`mb`) on AWS S3 called `kicks-pasta-steer`. The bucket name you choose must be _globally_ unique, meaning nobody else in the world must have used that bucket name before.

{{< highlight markdown >}}
aws s3 mb s3://kicks-pasta-steer
{{< /highlight >}}
```
make_bucket: kicks-pasta-steer
```

## Create Second Bucket

{{< highlight markdown >}}
aws s3 mb s3://assume-laser-rental
{{< /highlight >}}
```
make_bucket: assume-laser-rental
```

## List All Buckets

{{< highlight markdown >}}
aws s3 ls
{{< /highlight >}}
```
2018-09-23 18:48:46 assume-laser-rental
2018-09-23 18:36:23 kicks-pasta-steer
```