---
title: "Lower And Upper Case"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to convert values into lower and upper case in an SQL database."
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
       ('Alooneric Cortte', 29, 'Human', 'Bow'),
       ('Piperel Ramsay', 35, 'Elf', 'Bow'),
       ('Casimir Yardley', 14, 'Elf', 'Bow')
{{< /highlight >}}

## Upper Case String Values

{{< highlight sql >}}
-- Upper case the values in the race column
SELECT UPPER(race) FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>upper</th></tr>
<tr><td>HUMAN</td></tr>
<tr><td>HUMAN</td></tr>
<tr><td>ELF</td></tr>
<tr><td>ELF</td></tr></table>

## Lower Case String Values

{{< highlight sql >}}
-- Lower case the values in the race column
SELECT lower(race) FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>lower</th></tr>
<tr><td>human</td></tr>
<tr><td>human</td></tr>
<tr><td>elf</td></tr>
<tr><td>elf</td></tr></table>
