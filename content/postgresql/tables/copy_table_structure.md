---
title: "Copy Table Structure"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to copy a table's structure in an SQL database."
type: technical_note
draft: false
---

## Create Table

{{< highlight sql >}}
-- Create table called adventurers
CREATE TABLE adventurers (
    -- string variable
    name varchar(255),
    -- integer variable
    age int,
    -- string variable
    race varchar(255),
    -- string variable
    weapon varchar(255)
)
{{< /highlight >}}

## Create New Table Using Existing Table's Structure

{{< highlight sql >}}
-- Create table called adventurers_copy using the same columns as...
CREATE TABLE adventurers_copy AS (
    -- The adventurers table
    SELECT * FROM adventurers
)
{{< /highlight >}}