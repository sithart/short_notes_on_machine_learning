---
title: "Create Or Replace Table"
author: "Chris Albon"
date: 2019-01-28T00:00:00-07:00
description: "How to create or replace a table using SQL in Snowflake."
type: technical_note
draft: false
---

## Create Table

This `CREATE OR REPLACE` method will create a table and if a table with the same name does already exists, will replace that existing table with the new table.

{{< highlight sql >}}
-- Create a table called SUPERHEROES. If it already exists, replace it.
CREATE OR REPLACE TABLE SUPERHEROES (
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