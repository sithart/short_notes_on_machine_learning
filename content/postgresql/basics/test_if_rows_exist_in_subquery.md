---
title: "Test If Rows Exist In Subquery"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to test if there are any rows in a subquery in a table in an SQL database."
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

## Test If Rows Exist In Subquery

{{< highlight sql >}}
-- Retrieve all the rows in adventurers
SELECT * FROM adventurers
-- Where rows exist in
WHERE EXISTS
-- A subquery that will
(
    -- Select all the names in adventurers
    SELECT name FROM adventurers
    -- Where race is elf
    WHERE race = 'Elf'
)
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>28</td><td>Human</td></tr>
<tr><td>Alooneric Cortte</td><td>29</td><td>Elf</td></tr>
<tr><td>Piperel Ramsay</td><td>35</td><td>Elf</td></tr>
<tr><td>Casimir Yardley</td><td>14</td><td>Elf</td></tr></table>

## Test If Rows Do Not Exist In Subquery

{{< highlight sql >}}
-- Retrieve all the rows in adventurers
SELECT * FROM adventurers
-- Where the name of the adventurer is in
WHERE NOT EXISTS
-- A subquery that will
(
    -- Select all the names in adventurers
    SELECT name FROM adventurers
    -- Where race is dwarf
    WHERE race = 'Dwarf'
)
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>28</td><td>Human</td></tr>
<tr><td>Alooneric Cortte</td><td>29</td><td>Elf</td></tr>
<tr><td>Piperel Ramsay</td><td>35</td><td>Elf</td></tr>
<tr><td>Casimir Yardley</td><td>14</td><td>Elf</td></tr></table>