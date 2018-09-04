---
title: "Select Values Between Two Values"
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

## Get Values Between Two Values, Method 1

{{< highlight sql >}}
-- Get all rows from adventurers
SELECT * FROM adventurers
-- Where age is between 20 and 30
WHERE age BETWEEN 20 AND 30
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>28</td><td>Human</td></tr>
<tr><td>Alooneric Cortte</td><td>29</td><td>Human</td></tr></table>

## Get Values Between Two Values, Method 2
{{< highlight sql >}}
-- Get all rows from adventurers
SELECT * FROM adventurers
-- Where age is between 20 and 30
WHERE age >= 20 AND age <= 30
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>28</td><td>Human</td></tr>
<tr><td>Alooneric Cortte</td><td>29</td><td>Human</td></tr></table>