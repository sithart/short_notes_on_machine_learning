---
title: "Change Values"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to change values in a table in an SQL database."
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

## Update Row Values

{{< highlight sql >}}
-- Update the elves table
UPDATE elves
-- To set age to the current age plus 1
SET age = age + 1
{{< /highlight >}}

## View Elves Table

{{< highlight sql >}}
-- Retrieve all rows from the view Elf
SELECT * FROM elves
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th><th>alive</th></tr>
<tr><td>Dallar Woodfoot</td><td>26</td><td>Elf</td><td>Yes</td></tr>
<tr><td>Cordin Garner</td><td>30</td><td>Elf</td><td>Yes</td></tr>
<tr><td>Keat Knigh</td><td>25</td><td>Elf</td><td>Yes</td></tr>
<tr><td>Colbat Nalor</td><td>125</td><td>Elf</td><td>Yes</td></tr></table>