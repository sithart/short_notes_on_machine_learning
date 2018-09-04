---
title: "Calculate Running Total"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to calculate a running total of a column in an SQL database."
type: technical_note
draft: false
---

## Create Table

{{< highlight sql >}}
-- Create table called adventurers
CREATE TABLE adventurers (
    -- integer variable
    id int,
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
INSERT INTO adventurers (id, name, age, race, weapon)
VALUES (1, 'Fjoak Doom-Wife', 28, 'Human', 'Axe'),
       (2, 'Alooneric Cortte', 29, 'Elf', 'Bow'),
       (3, 'Piperel Ramsay', 35, 'Elf', 'Sword'),
       (4, 'Casimir Yardley', 14, 'Elf', 'Magic')
{{< /highlight >}}

## Create Running Total

{{< highlight sql >}}
-- Get name, age, and...
SELECT copy1.name, copy1.age, 
-- a sum of age from a copy of adventurers table called copy2 
-- Where the id of the copy2 is less than or equal to the id of copy1
-- and call it running_total
(SELECT sum(copy2.age) FROM adventurers copy2 WHERE copy2.id <= copy1.id) AS running_total
-- From the adventurer's table, calling it copy1  
FROM adventurers copy1
-- Sort by running total
ORDER BY running_total
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>running_total</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>28</td><td>28</td></tr>
<tr><td>Alooneric Cortte</td><td>29</td><td>57</td></tr>
<tr><td>Piperel Ramsay</td><td>35</td><td>92</td></tr>
<tr><td>Casimir Yardley</td><td>14</td><td>106</td></tr></table>