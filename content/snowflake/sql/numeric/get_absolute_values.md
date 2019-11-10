---
title: "Get Absolute Values"
author: "Chris Albon"
date: 2019-01-28T00:00:00-07:00
description: "How to get absolute values of a column using SQL in Snowflake."
type: technical_note
draft: false
---

## Create Temporary Table

{{< highlight sql >}}
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

## Add Rows, One For Each Superhero

{{< highlight sql >}}
-- Insert rows into SUPERHEROES
INSERT INTO SUPERHEROES 
    -- With the values
    VALUES
    ('XF6K4', 'Chris Maki', 'Diamond Ninja', '-100.20'),
    ('KD5SK', 'Donny Mav', 'The Dragoon', '200.30');
{{< /highlight >}}

## View Table

{{< highlight sql >}}
-- View the table
SELECT ALTER_EGO, BANK_BALANCE FROM SUPERHEROES;
{{< /highlight >}}
<table border=1>
    <thead>
        <tr>
            <th>ALTER_EGO</th>
            <th>BANK_BALANCE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Diamond Ninja</td>
            <td>-100.20</td>
        </tr>
        <tr>
            <td>The Dragoon</td>
            <td>200.30</td>
        </tr>
    </tbody>
</table>

## View Table With Absolute Values Of Bank Balance

{{< highlight sql >}}
-- View the table with absolute bank values
SELECT ALTER_EGO, ABS(BANK_BALANCE) FROM SUPERHEROES;
{{< /highlight >}}
<table border=1>
    <thead>
        <tr>
            <th>ALTER_EGO</th>
            <th>ABS(BANK_BALANCE)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Diamond Ninja</td>
            <td>100.20</td>
        </tr>
        <tr>
            <td>The Dragoon</td>
            <td>200.30</td>
        </tr>
    </tbody>
</table>