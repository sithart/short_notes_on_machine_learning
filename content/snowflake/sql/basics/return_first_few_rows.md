---
title: "Return First Few Rows"
author: "Chris Albon"
date: 2019-01-28T00:00:00-07:00
description: "Return the first few rows of a table in Snowflake using SQL."
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

## Return First Rows

{{< highlight sql >}}
-- Select all columns from SUPERHEROES
SELECT * FROM SUPERHEROES
-- Return the first five rows
LIMIT 5;
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
            <td>The Bomber</td>
            <td>24</td>
            <td>Maine</td>
        </tr>
        <tr>
            <td>Mr. Money</td>
            <td>12</td>
            <td>Maine</td>
        </tr>
        <tr>
            <td>Nuke Miner</td>
            <td>59</td>
            <td>Maine</td>
        </tr>
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
    </tbody>
</table>