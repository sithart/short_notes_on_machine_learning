---
title: "Retrieve Subset Of Columns"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to retrieve a subset of columns in an SQL database."
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
-- Retrieve name and age columns
SELECT name, age FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>28</td></tr>
<tr><td>Alooneric Cortte</td><td>29</td></tr>
<tr><td>Piperel Ramsay</td><td>35</td></tr>
<tr><td>Casimir Yardley</td><td>14</td></tr></table>