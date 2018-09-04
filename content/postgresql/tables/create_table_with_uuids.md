---
title: "Create Table With UUIDs"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to create table with uuids in an SQL database."
type: technical_note
draft: false
---

## Install UUID Extension

{{< highlight sql >}}
-- Install uuid extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp"
{{< /highlight >}}

## Create Table

{{< highlight sql >}}
-- Create table called adventurers
CREATE TABLE adventurers (
    -- uuid variable
    adventurer_id uuid DEFAULT uuid_generate_v4(),
    -- string variable
    name varchar(255),
    -- integer variable
    age int,
    -- string variable
    race varchar(255),
    -- string variable
    weapon varchar(255),
    -- Assign adventurer_id as primary key
    PRIMARY KEY (adventurer_id)
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

## View Table

{{< highlight sql >}}
-- Retrieve all rows in table
SELECT * FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>adventurer_id</th><th>name</th><th>age</th><th>race</th><th>weapon</th></tr>
<tr><td>61bf9084-2fcc-40dd-bbec-08de205e7877</td><td>Fjoak Doom-Wife</td><td>28</td><td>Human</td><td>Axe</td></tr>
<tr><td>495c81ca-a49d-4848-84bc-01bfa27916cc</td><td>Alooneric Cortte</td><td>29</td><td>Human</td><td>Bow</td></tr>
<tr><td>1533f42e-e64b-4aa2-8432-926defe3d248</td><td>Piperel Ramsay</td><td>35</td><td>Elf</td><td>Bow</td></tr>
<tr><td>090420af-372c-43b8-9eda-763a76eb692f</td><td>Casimir Yardley</td><td>14</td><td>Elf</td><td>Bow</td></tr></table>