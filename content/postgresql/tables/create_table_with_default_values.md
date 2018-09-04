---
title: "Create Table With Default Values"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to create column with default values in an SQL database."
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
    -- string variable with default value of 'no weapon'
    weapon varchar(255) DEFAULT 'no weapon'
)
{{< /highlight >}}

## Insert Row

{{< highlight sql >}}
-- Insert rows into the table adventurers
-- Notice we don't provide value for weapon column
INSERT INTO adventurers (name, age, race)
VALUES ('Piperel Ramsay', 35, 'Elf'),
       ('Casimir Yardley', 14, 'Elf')
{{< /highlight >}}

## Retrieve Rows

{{< highlight sql >}}
-- Retrieve all rows from table
SELECT * FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th><th>weapon</th></tr>
<tr><td>Piperel Ramsay</td><td>35</td><td>Elf</td><td>no weapon</td></tr>
<tr><td>Casimir Yardley</td><td>14</td><td>Elf</td><td>no weapon</td></tr></table>