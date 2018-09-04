---
title: "Create Column Aliases"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to create column aliases for columns in an SQL database."
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

## Retrieve Two Columns

{{< highlight sql >}}
-- Retrieve name and weapon column, renamed full_name and primary_weapon
SELECT name as full_name, weapon as primary_weapon FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>full_name</th><th>primary_weapon</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>Axe</td></tr>
<tr><td>Alooneric Cortte</td><td>Bow</td></tr>
<tr><td>Piperel Ramsay</td><td>Sword</td></tr>
<tr><td>Casimir Yardley</td><td>Magic</td></tr></table>