---
title: "Show Column Information"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to show column information in an SQL database."
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

## Show Column Information

{{< highlight sql >}}
-- Select column name, data type, and max character limit
SELECT column_name, data_type, character_maximum_length
-- From the database's schema
FROM INFORMATION_SCHEMA.COLUMNS
-- For the table adventurers
WHERE table_name = 'adventurers'
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>column_name</th><th>data_type</th><th>character_maximum_length</th></tr>
<tr><td>name</td><td>character varying</td><td>255</td></tr>
<tr><td>age</td><td>integer</td><td>NULL</td></tr>
<tr><td>race</td><td>character varying</td><td>255</td></tr>
<tr><td>weapon</td><td>character varying</td><td>255</td></tr></table>