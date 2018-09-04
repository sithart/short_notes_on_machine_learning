---
title: "View Size Of Table"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How view the size of a table in an SQL database."
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

## Insert Row

{{< highlight sql >}}
-- Insert row into the table adventurers
INSERT INTO adventurers (name, age, race, weapon)
VALUES ('Fjoak Doom-Wife', 28, 'Human', 'Axe'),
       ('Alooneric Cortte', 29, 'Elf', 'Bow'),
       ('Piperel Ramsay', 35, 'Elf', 'Sword'),
       ('Casimir Yardley', 14, 'Elf', 'Magic')
{{< /highlight >}}

## View Size Of Table

Note: This is method only with in PostgreSQL databases

{{< highlight sql >}}
SELECT pg_size_pretty(pg_total_relation_size('adventurers'))
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>pg_size_pretty</th></tr>
<tr><td>16 kB</td></tr></table>