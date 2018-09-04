---
title: "Self Join Table"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to self join tables in an SQL database."
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
    child_of varchar(255)
)
{{< /highlight >}}

## Insert Rows Into Adventurers Table

{{< highlight sql >}}
INSERT INTO adventurers (name, age, child_of)
VALUES ('Dallar Woodfoot', 25, NULL),
       ('Cordin Garner', 29, NULL),
       ('Keat Garner', 24, 'Cordin Garner'),
       ('Colbat Nalor', 124, NULL)
{{< /highlight >}}

## Inner Join Tables

{{< highlight sql >}}
-- Select name of copy1 and name of copy2 (renamed "parent")
SELECT copy1.name, copy2.name as parent
-- Where copy1 and copy2 are identical copies of the adventurers table
FROM adventurers copy1, adventurers copy2
-- Merge copy1 and copy2 where the name of copy1 matches the name of child_of field in copy2
WHERE copy1.name = copy2.child_of
{{< /highlight >}}
<!DOCTYPE html>
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>parent</th></tr>
<tr><td>Cordin Garner</td><td>Keat Garner</td></tr></table>