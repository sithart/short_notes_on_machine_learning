---
title: "List Index Columns"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to list indexed columns in an SQL database."
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

## Insert Rows Into Elf Table

{{< highlight sql >}}
INSERT INTO elves (name, age, race, alive)
VALUES ('Dallar Woodfoot', 25, 'Elf', 'Yes'),
       ('Cordin Garner', 29, 'Elf', 'Yes'),
       ('Keat Knigh', 24, 'Elf', 'Yes'),
       ('Colbat Nalor', 124, 'Elf', 'Yes')
{{< /highlight >}}

## Create Index

{{< highlight sql >}}
-- Index the names column in the elves table
CREATE INDEX ON elves (name)
{{< /highlight >}}

## View All Indexes In Database

{{< highlight sql >}}
SELECT indexes.tablename, indexes.indexname, columns.column_name
FROM pg_catalog.pg_indexes indexes, information_schema.columns columns
WHERE indexes.schemaname = 'public'
AND indexes.tablename  = columns.table_name
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>tablename</th><th>indexname</th><th>column_name</th></tr>
<tr><td>elves</td><td>elves_name_idx</td><td>name</td></tr>
<tr><td>elves</td><td>elves_name_idx</td><td>age</td></tr>
<tr><td>elves</td><td>elves_name_idx</td><td>race</td></tr>
<tr><td>elves</td><td>elves_name_idx</td><td>alive</td></tr></table>