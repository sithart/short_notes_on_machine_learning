---
title: "Create Primary Key"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to create view in an SQL database."
type: technical_note
draft: false
---

## Create Table

{{< highlight sql >}}
-- Create table called adventurers
CREATE TABLE adventurers (
    -- integer variable
    adventurer_id INT,
    -- string variable
    name varchar(255),
    -- integer variable
    age int,
    -- string variable
    race varchar(255),
    -- string variable
    weapon varchar(255),
    PRIMARY KEY (adventurer_id)
)
{{< /highlight >}}

## Insert Rows

{{< highlight sql >}}
-- Insert into the table adventurers
INSERT INTO adventurers (adventurer_id, name, age, race, weapon)
VALUES (1, 'Fjoak Doom-Wife', 28, 'Human', 'Axe'),
       (2, 'Alooneric Cortte', 29, 'Human', 'Bow'),
       (3, 'Piperel Ramsay', 35, 'Elf', 'Bow'),
       (4, 'Casimir Yardley', 14, 'Elf', 'Bow')
{{< /highlight >}}

## View Table

{{< highlight sql >}}
-- Retrieve all rows
SELECT * FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>adventurer_id</th><th>name</th><th>age</th><th>race</th><th>weapon</th></tr>
<tr><td>1</td><td>Fjoak Doom-Wife</td><td>28</td><td>Human</td><td>Axe</td></tr>
<tr><td>2</td><td>Alooneric Cortte</td><td>29</td><td>Human</td><td>Bow</td></tr>
<tr><td>3</td><td>Piperel Ramsay</td><td>35</td><td>Elf</td><td>Bow</td></tr>
<tr><td>4</td><td>Casimir Yardley</td><td>14</td><td>Elf</td><td>Bow</td></tr></table>