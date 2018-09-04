---
title: "Concatenate Values"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to concatenate values in an SQL database."
type: technical_note
draft: false
---

Note: This code works in PostgreSQL databases, but might not work in other SQL database systems (e.g. MySQL).

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
-- Retrieve name and age values and concatenate together as a sentence
SELECT name||' is '||age||' years old.' FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>?column?</th></tr>
<tr><td>Fjoak Doom-Wife is 28 years old.</td></tr>
<tr><td>Alooneric Cortte is 29 years old.</td></tr>
<tr><td>Piperel Ramsay is 35 years old.</td></tr>
<tr><td>Casimir Yardley is 14 years old.</td></tr></table>