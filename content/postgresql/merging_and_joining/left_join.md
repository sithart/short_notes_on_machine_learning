---
title: "Left Join Tables"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to left join tables in an SQL database."
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

## Create Table Of Adventurer's Equipment

{{< highlight sql >}}
-- Create table called equipment
CREATE TABLE equipment (
    -- string variable
    name varchar(255),
    -- string variable
    clothes varchar(255),
    -- string variable
    weapon varchar(255)
)
{{< /highlight >}}

## Insert Rows Into Adventurers Table

{{< highlight sql >}}
INSERT INTO adventurers (name, age, race)
VALUES ('Dallar Woodfoot', 25, 'Elf'),
       ('Cordin Garner', 29, 'Elf'),
       ('Keat Knigh', 24, 'Dwarf'),
       ('Colbat Nalor', 124, 'Dwarf')
{{< /highlight >}}

## Insert Rows Into Equipment Table
{{< highlight sql >}}
INSERT INTO equipment (name, clothes, weapon)
VALUES ('Dallar Woodfoot', 'Leather Armor', 'Axe'),
       ('Keat Knigh', 'Robe', 'Bow'),
       ('Tasar Keynelis', 'Tunic', 'Axe'),
       ('Sataleeti Iarroris','Chainmail', 'Axe')
{{< /highlight >}}

## Left Join Tables

{{< highlight sql >}}
-- Return the name of people from the adventurers table, age, race, clothes, and weapon
SELECT adventurers.name, age, race, clothes, weapon FROM adventurers
-- Left join with the equipment table
LEFT OUTER JOIN equipment
    -- Using the name as the merge key contained in both tables
    ON (adventurers.name = equipment.name)
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th><th>clothes</th><th>weapon</th></tr>
<tr><td>Dallar Woodfoot</td><td>25</td><td>Elf</td><td>Leather Armor</td><td>Axe</td></tr>
<tr><td>Cordin Garner</td><td>29</td><td>Elf</td><td>NULL</td><td>NULL</td></tr>
<tr><td>Keat Knigh</td><td>24</td><td>Dwarf</td><td>Robe</td><td>Bow</td></tr>
<tr><td>Colbat Nalor</td><td>124</td><td>Dwarf</td><td>NULL</td><td>NULL</td></tr></table>