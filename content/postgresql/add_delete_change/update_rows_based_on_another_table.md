---
title: "Update Rows Based On Another Table"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to update rows based on values in another table in an SQL database."
type: technical_note
draft: false
---

## Create Table Of Elves

{{< highlight sql >}}
-- Create table called elves
CREATE TABLE elves (
    -- string variable
    name varchar(255),
    -- integer variable
    age int,
    -- string variable
    race varchar(255),
    -- string variable
    alive varchar(255)
)
{{< /highlight >}}

## Create Table Of Deaths

{{< highlight sql >}}
-- Create table called deaths
CREATE TABLE deaths (
    -- string variable
    name varchar(255)
)
{{< /highlight >}}

## Insert Rows Into Elf Table

{{< highlight sql >}}
INSERT INTO elves (name, age, race, alive)
VALUES ('Dallar Woodfoot', 25, 'Elf', 'Yes'),
       ('Cordin Garner', 29, 'Elf', 'Yes'),
       ('Keat Knigh', 24, 'Elf', 'Yes'),
       ('Colbat Nalor', 124, 'Elf', 'Yes')
{{< /highlight >}}

## Insert Rows Into Deaths Table

{{< highlight sql >}}
INSERT INTO deaths (name)
VALUES ('Keat Knigh'),
       ('Colbat Nalor')
{{< /highlight >}}

## View Elves Table

{{< highlight sql >}}
-- Retrieve all rows from the view Elf
SELECT * FROM elves
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th><th>alive</th></tr>
<tr><td>Dallar Woodfoot</td><td>25</td><td>Elf</td><td>Yes</td></tr>
<tr><td>Cordin Garner</td><td>29</td><td>Elf</td><td>Yes</td></tr>
<tr><td>Keat Knigh</td><td>24</td><td>Elf</td><td>Yes</td></tr>
<tr><td>Colbat Nalor</td><td>124</td><td>Elf</td><td>Yes</td></tr></table>

## Update Rows Based On Another Table

{{< highlight sql >}}
-- Change the value in elves
UPDATE elves
-- to set alive to "No"
SET alive = 'No'
-- Where the name of the elf is in the list of deaths
WHERE elves.name in (SELECT deaths.name FROM deaths)
{{< /highlight >}}

## View Elves Table

{{< highlight sql >}}
-- Retrieve all rows from the view Elf
SELECT * FROM elves
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th><th>alive</th></tr>
<tr><td>Dallar Woodfoot</td><td>25</td><td>Elf</td><td>Yes</td></tr>
<tr><td>Cordin Garner</td><td>29</td><td>Elf</td><td>Yes</td></tr>
<tr><td>Keat Knigh</td><td>24</td><td>Elf</td><td>No</td></tr>
<tr><td>Colbat Nalor</td><td>124</td><td>Elf</td><td>No</td></tr></table>