---
title: "Save Queries As Variables"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to save queries as variables an SQL database."
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

## Create Two Subqueries, Save As Variables, Use In Another Query

Note that there are better ways to run this particular query. The code below is used as a simple example of how we can create variables out of subqueries and use them.

{{< highlight sql >}}
-- With variables called...
WITH

-- Create variable called "elves" containing 
-- all rows where race is elf
elves AS (
    SELECT * FROM adventurers
    WHERE race = 'Elf'
),

-- Create variable called "adults" containing 
-- all rows where age is greater than 18
adults AS (
    SELECT name FROM adventurers
    WHERE age > 18
)

-- Retrieve all columns in elves
SELECT * FROM elves
-- Where the name in elves is a member of the list of names in adults
WHERE elves.name IN (SELECT name FROM adults)
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th></tr>
<tr><td>Alooneric Cortte</td><td>29</td><td>Elf</td></tr>
<tr><td>Piperel Ramsay</td><td>35</td><td>Elf</td></tr></table>