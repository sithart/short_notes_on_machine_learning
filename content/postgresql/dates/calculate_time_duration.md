---
title: "Calculate Time Duration"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to calculate time duration in an SQL database."
type: technical_note
draft: false
---

## Create Table

{{< highlight sql >}}
-- Create table called dead_adventurers
CREATE TABLE dead_adventurers (
    -- string variable
    name varchar(255),
    -- string variable
    race varchar(255),
    -- string variable
    weapon varchar(255),
    -- date variable
    started_adventure date,
    -- date variable
    died date
)
{{< /highlight >}}

## Insert Rows

{{< highlight sql >}}
-- Insert into the table dead_adventurers
INSERT INTO dead_adventurers (name, race, weapon, started_adventure, died)
VALUES ('Fjoak Doom-Wife', 'Human', 'Axe', '09-JAN-2017', '10-Nov-2017'),
       ('Alooneric Cortte', 'Elf', 'Bow', '10-JAN-2017', '11-JAN-2017'),
       ('Piperel Ramsay', 'Elf', 'Sword', '11-JAN-2017', '12-APR-2017'),
       ('Casimir Yardley', 'Elf', 'Magic', '23-JAN-2017', '06-MAY-2017')
{{< /highlight >}}

## Calculate Duration Between Two Date Values

{{< highlight sql >}}
-- Get all the columns, and add a new column called days_on_adventure
-- that is the number of days between the start of the adventurer and when they died
SELECT *, died - started_adventure AS days_on_adventure FROM dead_adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>race</th><th>weapon</th><th>started_adventure</th><th>died</th><th>days_on_adventure</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>Human</td><td>Axe</td><td>2017-01-09</td><td>2017-11-10</td><td>305</td></tr>
<tr><td>Alooneric Cortte</td><td>Elf</td><td>Bow</td><td>2017-01-10</td><td>2017-01-11</td><td>1</td></tr>
<tr><td>Piperel Ramsay</td><td>Elf</td><td>Sword</td><td>2017-01-11</td><td>2017-04-12</td><td>91</td></tr>
<tr><td>Casimir Yardley</td><td>Elf</td><td>Magic</td><td>2017-01-23</td><td>2017-05-06</td><td>103</td></tr></table>
