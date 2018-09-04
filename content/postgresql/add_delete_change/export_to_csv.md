---
title: "Export To CSV"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to export to CSV in an SQL database."
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

## Export To CSV

Note: Relative file paths are not allowed.

{{< highlight sql >}}
-- Export the adventurers table to that file path and 
-- name using the comma delimiter and with column headings
COPY adventurers TO '/Users/chrisalbon/example_file.csv' DELIMITER ',' CSV HEADER
{{< /highlight >}}
