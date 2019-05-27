---
title: "Create Column Of Values"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to create a column of values for columns in an SQL database."
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

## Create Column Of Values

{{< highlight sql >}}
-- Get all rows and add a column called training where all values are 'elite'
SELECT *, 'elite' as training FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th><th>weapon</th><th>training</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>28</td><td>Human</td><td>Axe</td><td>elite</td></tr>
<tr><td>Alooneric Cortte</td><td>29</td><td>Elf</td><td>Bow</td><td>elite</td></tr>
<tr><td>Piperel Ramsay</td><td>35</td><td>Elf</td><td>Sword</td><td>elite</td></tr>
<tr><td>Casimir Yardley</td><td>14</td><td>Elf</td><td>Magic</td><td>elite</td></tr></table>