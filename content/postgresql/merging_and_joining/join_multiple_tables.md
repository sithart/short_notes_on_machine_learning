---
title: "Join Multiple Table"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to join multiple tables in an SQL database."
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
    race varchar(255)
)
{{< /highlight >}}

## Create Table Of Weapons

{{< highlight sql >}}
-- Create table called weapons
CREATE TABLE weapons (
    -- string variable
    name varchar(255),
    -- string variable
    weapon varchar(255),
    -- integer variable
    weight int
)
{{< /highlight >}}

## Create Table Of Armor

{{< highlight sql >}}
-- Create table called armor
CREATE TABLE armor (
    -- string variable
    name varchar(255),
    -- string variable
    body varchar(255),
    -- string variable
    helm varchar(255)
)
{{< /highlight >}}

## Insert Rows Into Elf Table

{{< highlight sql >}}
INSERT INTO elves (name, age, race)
VALUES ('Dallar Woodfoot', 25, 'Elf'),
       ('Cordin Garner', 29, 'Elf'),
       ('Keat Knigh', 24, 'Elf'),
       ('Colbat Nalor', 124, 'Elf')
{{< /highlight >}}

## Insert Rows Into Weapon Table

{{< highlight sql >}}
INSERT INTO weapons (name, weapon, weight)
VALUES ('Dallar Woodfoot','Axe', 2),
       ('Cordin Garner', 'Halberd', 3),
       ('Keat Knigh', 'Dagger', 4),
       ('Colbat Nalor', 'Dagger', 5)
{{< /highlight >}}

## Insert Rows Into Armor Table

{{< highlight sql >}}
INSERT INTO armor (name, body, helm)
VALUES ('Dallar Woodfoot', 'Leather', 'Leather'),
       ('Cordin Garner', 'Leather', NULL),
       ('Keat Knigh', 'Plate', 'Plate'),
       ('Colbat Nalor', 'Plate', 'Plate')
{{< /highlight >}}

## Join All Tables

{{< highlight sql >}}
-- All rows from table
SELECT elves.name, age, weapon, weight, body, helm FROM elves
-- Join with weapon table using name as key
LEFT JOIN weapons ON (elves.name = weapons.name)
-- Join with armor table using name as key
LEFT JOIN armor ON (elves.name = armor.name)
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>weapon</th><th>weight</th><th>body</th><th>helm</th></tr>
<tr><td>Dallar Woodfoot</td><td>25</td><td>Axe</td><td>2</td><td>Leather</td><td>Leather</td></tr>
<tr><td>Cordin Garner</td><td>29</td><td>Halberd</td><td>3</td><td>Leather</td><td>NULL</td></tr>
<tr><td>Keat Knigh</td><td>24</td><td>Dagger</td><td>4</td><td>Plate</td><td>Plate</td></tr>
<tr><td>Colbat Nalor</td><td>124</td><td>Dagger</td><td>5</td><td>Plate</td><td>Plate</td></tr></table>