---
title: "Calculate Sum Of Column"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to calculate sum of column in an SQL database."
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

## Calculate Sum

{{< highlight sql >}}
-- Return total value of of age in adventurers
SELECT SUM(age) FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>sum</th></tr>
<tr><td>106</td></tr></table>