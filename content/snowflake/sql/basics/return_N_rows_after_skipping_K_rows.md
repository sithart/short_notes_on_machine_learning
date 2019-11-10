---
title: "Return N Rows After Skipping First K Rows"
author: "Chris Albon"
date: 2019-01-28T00:00:00-07:00
description: "Return the rows of a table after skipping some rows in Snowflake using SQL."
type: technical_note
draft: false
---

## Create Table Of Superheroes

{{< highlight sql >}}
-- Create a table called SUPERHEROES.
CREATE OR REPLACE TABLE SUPERHEROES (
  -- Column called ALTER_EGO allowing up to 100 characters
  "ALTER_EGO" VARCHAR(100),
  -- Column called BANK_BALANCE allowing 38 digits with 2 after the decimal point
  "AGE" INT,
  -- Column called STATE allowing up to 100 characters
  "STATE" VARCHAR(100)
);
{{< /highlight >}}

## Insert Rows For Each Superhero

{{< highlight sql >}}
-- Insert rows into SUPERHEROES
INSERT INTO SUPERHEROES 
    -- With the values
    VALUES
    ('The Bomber', '24', 'Maine'),
    ('Mr. Money', '12', 'Maine'),
    ('Nuke Miner', '59', 'Maine'),
    ('The Knife', '43', 'Maine'),
    ('Ninka Baker', '32', 'California'),
    ('Banana Bomber', '34', 'California'),
    ('Augustine', '12', 'California'),
    ('The Kid', '21', 'New York'),
    ('The Viking', NULL, 'New York'),
    ('Skull Hustle', NULL, 'New York');
{{< /highlight >}}

## Return Rows After Skipping Rows

{{< highlight sql >}}
-- Select all columns from SUPERHEROES
SELECT * FROM SUPERHEROES
-- Skip 3 rows, then return the next 5 rows
LIMIT 5 OFFSET 3;
{{< /highlight >}}
<table border=1>
    <thead>
        <tr>
            <th>ALTER_EGO</th>
            <th>AGE</th>
            <th>STATE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>The Knife</td>
            <td>43</td>
            <td>Maine</td>
        </tr>
        <tr>
            <td>Ninka Baker</td>
            <td>32</td>
            <td>California</td>
        </tr>
        <tr>
            <td>Banana Bomber</td>
            <td>34</td>
            <td>California</td>
        </tr>
        <tr>
            <td>Augustine</td>
            <td>12</td>
            <td>California</td>
        </tr>
        <tr>
            <td>The Kid</td>
            <td>21</td>
            <td>New York</td>
        </tr>
    </tbody>
</table>