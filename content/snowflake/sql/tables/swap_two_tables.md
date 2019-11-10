---
title: "Swap Two Tables"
author: "Chris Albon"
date: 2019-01-28T00:00:00-07:00
description: "How to swap two tables in Snowflake using SQL."
type: technical_note
draft: false
---

`SWAP` will swap all contents, metadata, and access permissions between two tables. This can be useful by allowing you to build a new version of the table over time and then when you are ready, swapping out the old verison for the new version.

## Create Table Of Superheroes

{{< highlight sql >}}
-- Create a table called SUPERHEROES. If it already exists, replace it.
CREATE OR REPLACE TABLE SUPERHEROES (
  -- Column called ID allowing up to five characters
  "ID" VARCHAR(5), 
  -- Column called NAME allowing up to 100 characters
  "NAME" VARCHAR(100),
  -- Column called ALTER_EGO allowing up to 100 characters
  "ALTER_EGO" VARCHAR(100)
);
{{< /highlight >}}

## Insert Rows For Each Superhero

{{< highlight sql >}}
-- Insert rows into SUPERHEROES
INSERT INTO SUPERHEROES 
    -- With the values
    VALUES
    ('XF6K4', 'Chris Maki', 'The Bomber'),
    ('KD5SK', 'Donny Mav', 'Nuke Miner');
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
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>XF6K4</td>
            <td>Chris Maki</td>
            <td>The Bomber</td>
        </tr>
        <tr>
            <td>KD5SK</td>
            <td>Donny Mav</td>
            <td>Nuke Miner</td>
        </tr>
    </tbody>
</table>

## Create Table Of Villans

{{< highlight sql >}}
-- Create a table called VILLANS. If it already exists, replace it.
CREATE OR REPLACE TABLE VILLANS (
  -- Column called ID allowing up to five characters
  "ID" VARCHAR(5), 
  -- Column called NAME allowing up to 100 characters
  "NAME" VARCHAR(100),
  -- Column called ALTER_EGO allowing up to 100 characters
  "ALTER_EGO" VARCHAR(100)
);
{{< /highlight >}}

## Insert Rows For Each Villan

{{< highlight sql >}}
-- Insert rows into VILLANS
INSERT INTO VILLANS 
    -- With the values
    VALUES
    ('KXD33', 'Millie Macoon', 'Slasher'),
    ('LKD92', 'Jason Jones', 'The Blade');
{{< /highlight >}}

## View Table Of Villans

{{< highlight sql >}}
-- View the VILLANS table
SELECT * FROM VILLANS;
{{< /highlight >}}
<table border=1>
    <thead>
        <tr>
            <th>ID</th>
            <th>NAME</th>
            <th>ALTER_EGO</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>KXD33</td>
            <td>Millie Macoon</td>
            <td>Slasher</td>
        </tr>
        <tr>
            <td>LKD92</td>
            <td>Jason Jones</td>
            <td>The Blade</td>
        </tr>
    </tbody>
</table>

## Swap Superhero and Villan Tables

{{< highlight sql >}}
-- Swap the SUPERHEROES and VILLANS tables
ALTER TABLE IF EXISTS SUPERHEROES SWAP WITH VILLANS;
{{< /highlight >}}

## View New Table Of Superheroes

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
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>KXD33</td>
            <td>Millie Macoon</td>
            <td>Slasher</td>
        </tr>
        <tr>
            <td>LKD92</td>
            <td>Jason Jones</td>
            <td>The Blade</td>
        </tr>
    </tbody>
</table>

## View New Table Of Villans

{{< highlight sql >}}
-- View the VILLANS table
SELECT * FROM VILLANS;
{{< /highlight >}}
<table border=1>
    <thead>
        <tr>
            <th>ID</th>
            <th>NAME</th>
            <th>ALTER_EGO</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>XF6K4</td>
            <td>Chris Maki</td>
            <td>The Bomber</td>
        </tr>
        <tr>
            <td>KD5SK</td>
            <td>Donny Mav</td>
            <td>Nuke Miner</td>
        </tr>
    </tbody>
</table>
