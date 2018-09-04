---
title: "Replace Missing Values"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to replace missing values in an SQL database."
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

## Insert Rows With Missing Values

{{< highlight sql >}}
-- Insert into the table adventurers
INSERT INTO adventurers (name, age, race, weapon)
VALUES ('Fjoak Doom-Wife', 28, 'Human', 'Axe'),
       ('Alooneric Cortte', 29, 'Elf', 'Bow'),
       ('Piperel Ramsay', 35, 'Elf', NULL),
       ('Casimir Yardley', 14, 'Elf', NULL)
{{< /highlight >}}

## Retrieve Missing Values

In SQL, missing values are denoted as `NULL`.

{{< highlight sql >}}
-- Return values where value is the weapon if not missing, but "Unknown" if missing
SELECT name, COALESCE(weapon, 'Unknown') FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>coalesce</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>Axe</td></tr>
<tr><td>Alooneric Cortte</td><td>Bow</td></tr>
<tr><td>Piperel Ramsay</td><td>Unknown</td></tr>
<tr><td>Casimir Yardley</td><td>Unknown</td></tr></table>