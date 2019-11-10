---
title: "Give Column An Alias"
author: "Chris Albon"
date: 2019-01-28T00:00:00-07:00
description: "Give a column an alias in Snowflake using SQL."
type: technical_note
draft: false
---

## Create Table Of Superheroes

{{< highlight sql >}}
-- Create a table called SUPERHEROES.
CREATE OR REPLACE TABLE SUPERHEROES (
  -- Column called ID allowing up to five characters
  "ID" VARCHAR (5), 
  -- Column called NAME allowing up to 100 characters
  "NAME" VARCHAR(100),
  -- Column called ALTER_EGO allowing up to 100 characters
  "ALTER_EGO" VARCHAR(100),
  -- Column called BANK_BALANCE allowing 38 digits with 2 after the decimal point
  "BANK_BALANCE" NUMBER(38, 2),
  -- Column called AGE allowing 3 digits with 0 after the decimal point
  "AGE" NUMBER(3, 0)
);
{{< /highlight >}}

## Insert Rows For Each Superhero

{{< highlight sql >}}
-- Insert rows into SUPERHEROES
INSERT INTO SUPERHEROES 
    -- With the values
    VALUES
    ('XF6K4', 'Chris Maki', 'The Bomber', '-100.20', '14'),
    ('KDEJ4', 'Rich Richardson', 'Mr. Money', '233.20', '12'),
    ('KD5SK', 'Donny Mav', 'Nuke Miner', '200.30', '59');
{{< /highlight >}}

## Create An Alias For Column

{{< highlight sql >}}
-- Select... 
SELECT 
-- the NAME column from the table, call it REAL_NAME
NAME AS REAL_NAME, 
-- the AGE column
AGE 
-- From the SUPERHEROES table
FROM SUPERHEROES
{{< /highlight >}}
<table border=1>
    <thead>
        <tr>
            <th>REAL_NAME</th>
            <th>AGE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Chris Maki</td>
            <td>14</td>
        </tr>
        <tr>
            <td>Rich Richardson</td>
            <td>12</td>
        </tr>
        <tr>
            <td>Donny Mav</td>
            <td>59</td>
        </tr>
    </tbody>
</table>

## Create An Alias For Column (Alternative)

{{< highlight sql >}}
-- Select... 
SELECT 
-- the NAME column from the table, call it REAL_NAME
NAME REAL_NAME, 
-- the AGE column
AGE 
-- From the SUPERHEROES table
FROM SUPERHEROES
{{< /highlight >}}
<table border=1>
    <thead>
        <tr>
            <th>REAL_NAME</th>
            <th>AGE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Chris Maki</td>
            <td>14</td>
        </tr>
        <tr>
            <td>Rich Richardson</td>
            <td>12</td>
        </tr>
        <tr>
            <td>Donny Mav</td>
            <td>59</td>
        </tr>
    </tbody>
</table>