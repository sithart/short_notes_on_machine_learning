---
title: "Create Table If It Doesn't Already Exist"
author: "Chris Albon"
date: 2019-01-28T00:00:00-07:00
description: "How to create a table using SQL in Snowflake if it doesn't already exist."
type: technical_note
draft: false
---

## Create Table

`IF NOT EXISTS` tells Snowflake to only create the table if another table with the same name does not already exist. This can be useful if you don't want to run an expensive operation if the data is already there.

{{< highlight sql >}}
-- Create a table called SUPERHEROES.
CREATE TABLE IF NOT EXISTS SUPERHEROES (
  -- Column called ID allowing up to five characters
  "ID" VARCHAR (5), 
  -- Column called NAME allowing up to 100 characters
  "NAME" VARCHAR(100),
  -- Column called ALTER_EGO allowing up to 100 characters
  "ALTER_EGO" VARCHAR(100),
  -- Column called BANK_BALANCE allowing 38 digits with 2 after the decimal point
  "BANK_BALANCE" NUMBER(38, 2)
);
{{< /highlight >}}