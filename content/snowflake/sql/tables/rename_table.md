---
title: "Rename Table"
author: "Chris Albon"
date: 2019-01-28T00:00:00-07:00
description: "How to rename a table in Snowflake using SQL."
type: technical_note
draft: false
---

## Create Table Of Superheroes

{{< highlight sql >}}
-- Create a table called SUPERHEROES. If it already exists, replace it.
CREATE OR REPLACE TABLE SUPERHEROES (
  -- Column called ID allowing up to five characters
  "ID" VARCHAR(5), 
  -- Column called NAME allowing up to 100 characters
  "NAME" VARCHAR(100),
  -- Column called ALTER_EGO allowing up to 100 characters
  "ALTER_EGO" VARCHAR(100),
  -- Column called BANK_BALANCE allowing 38 digits with 2 after the decimal point
  "BANK_BALANCE" NUMBER(38, 2)
);
{{< /highlight >}}

## Insert Rows For Each Superhero

{{< highlight sql >}}
-- Insert rows into SUPERHEROES
INSERT INTO SUPERHEROES 
    -- With the values
    VALUES
    ('XF6K4', 'Chris Maki', 'The Bomber', '-100.20'),
    ('KD5SK', 'Donny Mav', 'Nuke Miner', '200.30');
{{< /highlight >}}

## View Table Of Superheroes

{{< highlight sql >}}
-- View the SUPERHEROES table
SELECT * FROM SUPERHEROES;
{{< /highlight >}}
<table border=1>
    <thead>
        <tr>
            <th>ID</th>
            <th>NAME</th>
            <th>ALTER_EGO</th>
            <th>BANK_BALANCE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>XF6K4</td>
            <td>Chris Maki</td>
            <td>The Bomber</td>
            <td>-100.20</td>
        </tr>
        <tr>
            <td>KD5SK</td>
            <td>Donny Mav</td>
            <td>Nuke Miner</td>
            <td>200.30</td>
        </tr>
    </tbody>
</table>

## Rename Table

{{< highlight sql >}}
-- Alter the SUPERHEROES table...
ALTER TABLE IF EXISTS SUPERHEROES 
-- By renaming it to HEROES
RENAME TO HEROES;
{{< /highlight >}}

## View Renamed Table

{{< highlight sql >}}
-- View the HEROES table
SELECT * FROM HEROES;
{{< /highlight >}}
<table border=1>
    <thead>
        <tr>
            <th>ID</th>
            <th>NAME</th>
            <th>ALTER_EGO</th>
            <th>BANK_BALANCE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>XF6K4</td>
            <td>Chris Maki</td>
            <td>The Bomber</td>
            <td>-100.20</td>
        </tr>
        <tr>
            <td>KD5SK</td>
            <td>Donny Mav</td>
            <td>Nuke Miner</td>
            <td>200.30</td>
        </tr>
    </tbody>
</table>