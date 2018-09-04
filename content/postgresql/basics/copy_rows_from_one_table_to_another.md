---
title: "Copy Rows From One Table To Another"
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

## Create Table Of Villains
{{< highlight sql >}}
-- Create table called equipment
CREATE TABLE villains (
    -- string variable
    name varchar(255),
    -- integer variable
    age int,
    -- string variable
    race varchar(255)
)
{{< /highlight >}}

## Insert Row Into Adventurers

{{< highlight sql >}}
-- Insert into the table adventurers
INSERT INTO adventurers (name, age, race)
VALUES ('Fjoak Doom-Wife', 28, 'Human')
{{< /highlight >}}

## View Adventurers Table

{{< highlight sql >}}
-- Retrieve all rows
SELECT * FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>28</td><td>Human</td></tr></table>

## Copy Rows From Adventurers Table To Villains Table

{{< highlight sql >}}
-- Insert into the villains table
INSERT INTO villains
    (
        -- All rows from adventurers
        SELECT * FROM adventurers
    )
{{< /highlight >}}

## View Villains Table

{{< highlight sql >}}
-- Retrieve all rows
SELECT * FROM villains
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>28</td><td>Human</td></tr></table>