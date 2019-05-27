---
title: "Adding Or Substracting Time"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to add or substract time in an SQL database."
type: technical_note
draft: false
---

## Create Table

{{< highlight sql >}}
-- Create table called dead_adventurers
CREATE TABLE dead_adventurers (
    -- string variable
    name varchar(255),
    -- integer variable
    age int,
    -- string variable
    race varchar(255),
    -- string variable
    weapon varchar(255),
    -- date variable
    died date
)
{{< /highlight >}}

## Insert Rows

{{< highlight sql >}}
-- Insert into the table dead_adventurers
INSERT INTO dead_adventurers (name, age, race, weapon, died)
VALUES ('Fjoak Doom-Wife', 28, 'Human', 'Axe', '09-Nov-2017'),
       ('Alooneric Cortte', 29, 'Elf', 'Bow', '10-JAN-2017'),
       ('Piperel Ramsay', 35, 'Elf', 'Sword', '12-APR-2016'),
       ('Casimir Yardley', 14, 'Elf', 'Magic', '06-MAY-2017')
{{< /highlight >}}

## Create New Column Three Days Later 

{{< highlight sql >}}
-- Create a column called three_days_laters that takes the value
-- of died and adds three days to it
SELECT died + INTERVAL '3 day' AS three_days_later
-- From adventurers table
FROM dead_adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>three_days_later</th></tr>
<tr><td>2017-11-12 00:00:00.000000</td></tr>
<tr><td>2017-01-13 00:00:00.000000</td></tr>
<tr><td>2016-04-15 00:00:00.000000</td></tr>
<tr><td>2017-05-09 00:00:00.000000</td></tr></table>