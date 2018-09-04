---
title: "Select Highest Value In Each Group"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to selected the highest value in each group in an SQL database."
type: technical_note
draft: false
---

## Create Table Of Adventurers

{{< highlight sql >}}
-- Create table called adventurers
CREATE TABLE adventurers (
    -- string variable
    name varchar(255),
    -- integer variable
    age int,
    -- string variable
    race varchar(255)
)
{{< /highlight >}}

## Insert Rows

{{< highlight sql >}}
-- Insert into the table adventurers
INSERT INTO adventurers (name, age, race)
VALUES ('Fjoak Doom-Wife', 28, 'Human'),
       ('Alooneric Cortte', 29, 'Human'),
       ('Piperel Ramsay', 35, 'Elf'),
       ('Casimir Yardley', 14, 'Elf')
{{< /highlight >}}

## Select The Oldest Adventurer In Each Race

{{< highlight sql >}}
-- Get the name, race, age of the first row in each group, 
-- when grouped by race
SELECT DISTINCT ON (race) name, race, age FROM adventurers
-- Order by race, then age, in descending order 
-- (so the oldest person is the top of each group)
ORDER BY race, age DESC
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>race</th><th>age</th></tr>
<tr><td>Piperel Ramsay</td><td>Elf</td><td>35</td></tr>
<tr><td>Alooneric Cortte</td><td>Human</td><td>29</td></tr></table>