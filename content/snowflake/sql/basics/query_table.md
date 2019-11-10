---
title: "Query A Table"
author: "Chris Albon"
date: 2019-01-28T00:00:00-07:00
description: "How to query a table in Snowflake using SQL."
type: technical_note
draft: false
---

## Create A Table For Superheroes

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

## Insert One Row Per Superhero

{{< highlight sql >}}
-- Insert rows into SUPERHEROES
INSERT INTO SUPERHEROES 
    -- With the values
    VALUES
    ('XF6K4', 'Chris Maki', 'The Bomber', '-100.20', '14'),
    ('KDEJ4', 'Rich Richardson', 'Mr. Money', '233.20', '12'),
    ('KD5SK', 'Donny Mav', 'Nuke Miner', '200.30', '59');
{{< /highlight >}}

## Query Superhero Table

{{< highlight sql >}}
-- Select all columns
SELECT * 
-- From the SUPERHEROES table
FROM SUPERHEROES
{{< /highlight >}}
<table border=1>
    <thead>
        <tr>
            <th>ID</th>
            <th>NAME</th>
            <th>ALTER_EGO</th>
            <th>BANK_BALANCE</th>
            <th>AGE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>XF6K4</td>
            <td>Chris Maki</td>
            <td>The Bomber</td>
            <td>-100.20</td>
            <td>14</td>
        </tr>
        <tr>
            <td>KDEJ4</td>
            <td>Rich Richardson</td>
            <td>Mr. Money</td>
            <td>233.20</td>
            <td>12</td>
        </tr>
        <tr>
            <td>KD5SK</td>
            <td>Donny Mav</td>
            <td>Nuke Miner</td>
            <td>200.30</td>
            <td>59</td>
        </tr>
    </tbody>
</table>