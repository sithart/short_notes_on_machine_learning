---
title: "Delete Rows That Don't Exist In Another Table"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to delete rows that don't exist in another table in an SQL database."
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

## Create Table Of Alive

{{< highlight sql >}}
-- Create table called alive
CREATE TABLE alive (
    -- string variable
    name varchar(255)
)
{{< /highlight >}}

## Insert Rows Into Elf Table

{{< highlight sql >}}
INSERT INTO elves (name, age, race, alive)
VALUES ('Dallar Woodfoot', 25, 'Elf', 'Yes'),
       ('Cordin Garner', 29, 'Elf', 'Yes'),
       ('Keat Knigh', 24, 'Elf', 'Yes'),
       ('Colbat Nalor', 124, 'Elf', 'Yes')
{{< /highlight >}}

## Insert Rows Into Alive Table

{{< highlight sql >}}
INSERT INTO alive (name)
VALUES ('Keat Knigh'),
       ('Colbat Nalor')
{{< /highlight >}}

## Delete Rows In Elf Table That Don't Exist In Alive Table

{{< highlight sql >}}
-- Delete in elf table
DELETE FROM elves
-- Where the name in elves is not in the list of names in alive.
WHERE elves.name NOT IN (SELECT name FROM alive)
{{< /highlight >}}

## View Elves Table

{{< highlight sql >}}
-- Retrieve all rows from the view Elf
SELECT * FROM elves
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th><th>alive</th></tr>
<tr><td>Keat Knigh</td><td>24</td><td>Elf</td><td>Yes</td></tr>
<tr><td>Colbat Nalor</td><td>124</td><td>Elf</td><td>Yes</td></tr></table>