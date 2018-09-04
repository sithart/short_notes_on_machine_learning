---
title: "List Columns In Table"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to list columns in table in an SQL database."
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
       ('Colbat Nalor', 124, 'Elf', 'Yes')
{{< /highlight >}}

## View Columns Rows In Elf Table

{{< highlight sql >}}
-- Get name, data ype and column position
SELECT column_name, data_type, ordinal_position
-- From the column's metadata
FROM information_schema.columns
-- Where the table name is elves
WHERE table_name = 'elves'
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>column_name</th><th>data_type</th><th>ordinal_position</th></tr>
<tr><td>name</td><td>character varying</td><td>1</td></tr>
<tr><td>age</td><td>integer</td><td>2</td></tr>
<tr><td>race</td><td>character varying</td><td>3</td></tr>
<tr><td>alive</td><td>character varying</td><td>4</td></tr></table>