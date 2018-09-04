---
title: "List Tables In Database"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to create table in an SQL database."
type: technical_note
draft: false
---

## Create Table

{{< highlight sql >}}
-- Create table called villains
CREATE TABLE villains (
    -- string variable
    name varchar(255)
)
{{< /highlight >}}

## Create Table

{{< highlight sql >}}
-- Create table called heroes
CREATE TABLE heroes (
    -- string variable
    name varchar(255)
)
{{< /highlight >}}

## Create Table

{{< highlight sql >}}
-- Create table called battles
CREATE TABLE battles (
    -- string variable
    name varchar(255)
)
{{< /highlight >}}

## List Tables In Database

{{< highlight sql >}}
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
AND table_type = 'BASE TABLE'
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>table_name</th></tr>
<tr><td>battles</td></tr>
<tr><td>heroes</td></tr>
<tr><td>villians</td></tr></table>