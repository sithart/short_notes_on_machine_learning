---
title: "Create Column Conditional On Another Column"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to create a column conditional on another column in an SQL database."
type: technical_note
draft: false
---

## Create Table

{{< highlight sql >}}
-- Create table called adventurers
CREATE TABLE adventurers (
    -- string variable
    name varchar(255),
    -- integer variable
    age int,
    -- string variable
    race varchar(255),
    -- string variable
    weapon varchar(255)
)
{{< /highlight >}}

## Insert Rows

{{< highlight sql >}}
-- Insert into the table adventurers
INSERT INTO adventurers (name, age, race, weapon)
VALUES ('Fjoak Doom-Wife', 28, 'Human', 'Axe'),
       ('Alooneric Cortte', 29, 'Elf', 'Bow'),
       ('Piperel Ramsay', 35, 'Elf', 'Sword'),
       ('Casimir Yardley', 14, 'Elf', 'Magic')
{{< /highlight >}}

## Create An If Else Statement

There are a number of ways to do if-else in SQL, my prefered way is the `CASE` statement.

{{< highlight sql >}}
-- Retrieve all rows
SELECT *,
    -- The case when race = elf, return "Elvish"
    CASE WHEN race = 'Elf' THEN 'Elvish'
         -- When race = human, return "Human"
         WHEN race = 'Human' THEN 'Human'
    -- Call this column "race"
    END AS race
-- Do this from the adventurers table
FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th><th>weapon</th><th>race</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>28</td><td>Human</td><td>Axe</td><td>Human</td></tr>
<tr><td>Alooneric Cortte</td><td>29</td><td>Elf</td><td>Bow</td><td>Elvish</td></tr>
<tr><td>Piperel Ramsay</td><td>35</td><td>Elf</td><td>Sword</td><td>Elvish</td></tr>
<tr><td>Casimir Yardley</td><td>14</td><td>Elf</td><td>Magic</td><td>Elvish</td></tr></table>