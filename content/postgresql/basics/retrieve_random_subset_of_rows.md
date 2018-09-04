---
title: "Retrieve Random Subset Of Rows"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to retrieve random subset of rows."
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

## Retrieve Only Two Rows

{{< highlight sql >}}
-- Retrieve rows from table
SELECT * FROM adventurers
    -- Shuffle randomly
    ORDER BY RANDOM()
    -- Retrieve two rows
    LIMIT 2
{{< /highlight >}}
<!DOCTYPE html>
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th><th>weapon</th></tr>
<tr><td>Alooneric Cortte</td><td>29</td><td>Elf</td><td>Bow</td></tr>
<tr><td>Piperel Ramsay</td><td>35</td><td>Elf</td><td>Sword</td></tr></table>