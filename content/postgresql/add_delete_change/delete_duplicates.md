---
title: "Delete Duplicates"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to duplicate rows in an SQL database."
type: technical_note
draft: false
---

## Create Table Of Elves

{{< highlight sql >}}
-- Create table called elves
CREATE TABLE elves (
    -- string variable
    name varchar(255),
    -- integer variable
    age int,
    -- string variable
    race varchar(255),
    -- string variable
    alive varchar(255)
)
{{< /highlight >}}

## Insert Rows Into Elf Table

{{< highlight sql >}}
INSERT INTO elves (name, age, race, alive)
VALUES ('Dallar Woodfoot', 25, 'Elf', 'Yes'),
       ('Cordin Garner', 29, 'Elf', 'Yes'),
       ('Keat Knigh', 24, 'Elf', 'Yes'),
       ('Keat Knigh', 24, 'Elf', 'Yes'),
       ('Keat Knigh', 24, 'Elf', 'Yes'),
       ('Keat Knigh', 24, 'Elf', 'Yes'),
       ('Colbat Nalor', 124, 'Elf', 'Yes')
{{< /highlight >}}

## View Elves Table

{{< highlight sql >}}
-- Retrieve all rows from the view Elf
SELECT * FROM elves
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th><th>alive</th></tr>
<tr><td>Dallar Woodfoot</td><td>25</td><td>Elf</td><td>Yes</td></tr>
<tr><td>Cordin Garner</td><td>29</td><td>Elf</td><td>Yes</td></tr>
<tr><td>Keat Knigh</td><td>24</td><td>Elf</td><td>Yes</td></tr>
<tr><td>Keat Knigh</td><td>24</td><td>Elf</td><td>Yes</td></tr>
<tr><td>Keat Knigh</td><td>24</td><td>Elf</td><td>Yes</td></tr>
<tr><td>Keat Knigh</td><td>24</td><td>Elf</td><td>Yes</td></tr>
<tr><td>Colbat Nalor</td><td>124</td><td>Elf</td><td>Yes</td></tr></table>

## Drop Duplicates

Note: Normally we would use a unique identify column (e.g. person ID, product ID, etc.). However, since we don't have a unique ID column we can use PostgreSQL's internal system column, `ctid`. Full documentation on `ctid` and other system columns in avaliable [here](https://www.postgresql.org/docs/9.2/static/ddl-system-columns.html).

{{< highlight sql >}}
-- Delete from the elves, calling it copy1
DELETE FROM elves copy1
-- Using a second copy of elves, called copy2
USING elves copy2
-- Where the internal PostgreSQL system column, ctid is smaller
WHERE copy1.ctid < copy2.ctid
  -- And all other columns are the same
  AND copy1.name = copy2.name
  AND copy1.age = copy2.age
  AND copy1.race = copy2.race
  AND copy1.alive = copy2.alive
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th><th>alive</th></tr>
<tr><td>Dallar Woodfoot</td><td>25</td><td>Elf</td><td>Yes</td></tr>
<tr><td>Cordin Garner</td><td>29</td><td>Elf</td><td>Yes</td></tr>
<tr><td>Keat Knigh</td><td>24</td><td>Elf</td><td>Yes</td></tr>
<tr><td>Colbat Nalor</td><td>124</td><td>Elf</td><td>Yes</td></tr></table>