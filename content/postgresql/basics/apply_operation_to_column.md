---
title: "Apply Operation To Column"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to copy rows from one table to another in an SQL database."
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
       ('Alooneric Cortte', 29, 'Elf'),
       ('Piperel Ramsay', 35, 'Elf'),
       ('Casimir Yardley', 14, 'Elf')
{{< /highlight >}}

## Apply Operation To Column

{{< highlight sql >}}
-- Update the age column, multiplying all age values by 10
UPDATE adventurers SET age = age * 10
{{< /highlight >}}

## Apply Operation To Column With Conditions

{{< highlight sql >}}
-- Update the name column where the race column is 'Elf'
UPDATE adventurers SET name = 'Some Elf'
WHERE race = 'Elf'
{{< /highlight >}}

## View Table

{{< highlight sql >}}
-- Retrieve data
SELECT * FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>280</td><td>Human</td></tr>
<tr><td>Some Elf</td><td>290</td><td>Elf</td></tr>
<tr><td>Some Elf</td><td>350</td><td>Elf</td></tr>
<tr><td>Some Elf</td><td>140</td><td>Elf</td></tr></table>