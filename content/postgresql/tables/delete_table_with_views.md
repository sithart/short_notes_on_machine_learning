---
title: "Delete Table With Views"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to delete table with views in an SQL database."
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
       ('Alooneric Cortte', 29, 'Human', 'Bow'),
       ('Piperel Ramsay', 35, 'Elf', 'Bow'),
       ('Casimir Yardley', 14, 'Elf', 'Bow')
{{< /highlight >}}

## Create View
{{< highlight sql >}}
-- Create view called elves containing
CREATE VIEW elves AS (
                        -- Select all rows from adventurers table
                        SELECT * FROM adventurers
                        -- Where the race is elf
                        WHERE race = 'Elf'
                      )
{{< /highlight >}}

## Delete Table

{{< highlight sql >}}
-- Delete table and dependent views
DROP TABLE adventurers CASCADE
{{< /highlight >}}