---
title: "Sort Rows In Groups"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to sort rows in an SQL database."
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

## Sort Rows By One Column

{{< highlight sql >}}
-- Retrieve rows
SELECT * FROM adventurers
-- Order rows by age in ascending order
ORDER BY age ASC
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th><th>weapon</th></tr>
<tr><td>Casimir Yardley</td><td>14</td><td>Elf</td><td>Magic</td></tr>
<tr><td>Fjoak Doom-Wife</td><td>28</td><td>Human</td><td>Axe</td></tr>
<tr><td>Alooneric Cortte</td><td>29</td><td>Elf</td><td>Bow</td></tr>
<tr><td>Piperel Ramsay</td><td>35</td><td>Elf</td><td>Sword</td></tr></table>

## Sort Rows By Two Columns


{{< highlight sql >}}
-- Retrieve rows
SELECT * FROM adventurers
-- Order rows, when race is elf, sort by name
ORDER BY CASE WHEN race = 'Elf' THEN name
              -- Otherwise sort by weapon
              ELSE weapon
         END
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th><th>weapon</th></tr>
<tr><td>Alooneric Cortte</td><td>29</td><td>Elf</td><td>Bow</td></tr>
<tr><td>Fjoak Doom-Wife</td><td>28</td><td>Human</td><td>Axe</td></tr>
<tr><td>Casimir Yardley</td><td>14</td><td>Elf</td><td>Magic</td></tr>
<tr><td>Piperel Ramsay</td><td>35</td><td>Elf</td><td>Sword</td></tr></table>