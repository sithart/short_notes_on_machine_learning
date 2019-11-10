---
title: "Create Dummy Columns"
author: "Chris Albon"
date: 2019-01-28T00:00:00-07:00
description: "How to create a set of dummy columns from a single category column in Snowflake using SQL."
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
    ('The Viking', '291', 'New York'),
    ('Skull Hustle', '10', 'New York');
{{< /highlight >}}

## Dummy Columns

Notice that the `ALTER_EGO` column does not appear because it is a string. We'd need to join that column back in to regain it.

{{< highlight sql >}}
-- Select all columns from SUPERHEROES
SELECT * FROM SUPERHEROES
     -- Create three columns (Maine, Arizona, and California) with a 1 if a row is a member
     -- of that category and a zero otherwise.
     PIVOT(count(ALTER_EGO) FOR STATE IN ('Maine', 'Arizona', 'California'));
{{< /highlight >}}
<table border=1>
    <thead>
        <tr>
            <th>AGE</th>
            <th>'Maine'</th>
            <th>'Arizona'</th>
            <th>'California'</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>24</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
        </tr>
        <tr>
            <td>12</td>
            <td>1</td>
            <td>0</td>
            <td>1</td>
        </tr>
        <tr>
            <td>59</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
        </tr>
        <tr>
            <td>43</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
        </tr>
        <tr>
            <td>32</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
        </tr>
        <tr>
            <td>34</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
        </tr>
        <tr>
            <td>291</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
        </tr>
        <tr>
            <td>10</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
        </tr>
        <tr>
            <td>21</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
        </tr>
    </tbody>
</table>