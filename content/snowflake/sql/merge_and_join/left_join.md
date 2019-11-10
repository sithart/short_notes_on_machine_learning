---
title: "Left Join"
author: "Chris Albon"
date: 2019-01-28T00:00:00-07:00
description: "How to left join two tables in Snowflake using SQL."
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
-- View the table
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

## Create Table Of Superhero Powers

{{< highlight sql >}}
-- Create a table called POWERS. If it already exists, replace it.
CREATE OR REPLACE TABLE POWERS (
  -- Column called ID allowing up to five characters
  "ID" VARCHAR(5), 
  -- Column called SUPER_POWER allowing up to 100 characters
  "SUPER_POWER" VARCHAR(100)
);
{{< /highlight >}}

## Insert Rows For Each Superpower

{{< highlight sql >}}
-- Insert rows into POWERS
INSERT INTO POWERS 
    -- With the values
    VALUES
    ('XF6K4', 'invisibility'),
    ('KD5SK', 'fire blast'),
    ('TKSI1', 'mind control') -- Note that this ID doesn't appear in the SUPERHEROES table
;
{{< /highlight >}}

## Merge Superhero And Superpower Tables

Notice that after this merge there are two `ID` columns. This is because both tables contained an ID column and therefore they both will appear in the final table.

{{< highlight sql >}}
-- Select all columns
SELECT * 
-- From SUPERHEROES table
FROM SUPERHEROES 
-- After left joining in the POWERS table
LEFT JOIN POWERS
-- Where the ID's in both tables are the same
ON SUPERHEROES.ID = POWERS.ID
;
{{< /highlight >}}
<table border=1>
    <thead>
        <tr>
            <th>ID</th>
            <th>NAME</th>
            <th>ALTER_EGO</th>
            <th>BANK_BALANCE</th>
            <th>ID</th>
            <th>SUPER_POWER</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>XF6K4</td>
            <td>Chris Maki</td>
            <td>The Bomber</td>
            <td>-100.20</td>
            <td>XF6K4</td>
            <td>invisibility</td>
        </tr>
        <tr>
            <td>KD5SK</td>
            <td>Donny Mav</td>
            <td>Nuke Miner</td>
            <td>200.30</td>
            <td>KD5SK</td>
            <td>fire blast</td>
        </tr>
    </tbody>
</table>