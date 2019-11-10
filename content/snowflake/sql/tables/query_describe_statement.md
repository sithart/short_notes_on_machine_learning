---
title: "Query DESCRIBE TABLE like a table"
author: "Chris Albon"
date: 2019-01-28T00:00:00-07:00
description: "How to treat a DESCRIBE statement like a table in Snowflake using SQL."
type: technical_note
draft: false
---

`DESCRIBE TABLE` is a powerful tool for understanding the structure of a table. However, in Snowflake the output of `DESCRIBE TABLE` is not treated like a regular table (i.e. can be manipulated using `SELECT`). To query `DESCRIBE TABLE` as a regular table we have to first run it, then run a `SELECT` query on the _last query run_ which will be `DESCRIBE TABLE`.

## Create Table Of Superheroes

{{< highlight sql >}}
-- Create a table called SUPERHEROES. If it already exists, replace it.
CREATE OR REPLACE TABLE SUPERHEROES (
  -- Column called ID allowing up to five characters
  "ID" VARCHAR(5), 
  -- Column called NAME allowing up to 100 characters
  "NAME" VARCHAR(100),
  -- Column called ALTER_EGO allowing up to 100 characters
  "ALTER_EGO" VARCHAR(100)
);
{{< /highlight >}}

## Insert Rows For Each Superhero

{{< highlight sql >}}
-- Insert rows into SUPERHEROES
INSERT INTO SUPERHEROES 
    -- With the values
    VALUES
    ('XF6K4', 'Chris Maki', 'The Bomber'),
    ('KD5SK', 'Donny Mav', 'Nuke Miner');
{{< /highlight >}}

## Describe The Table

{{< highlight sql >}}
-- Describe the table SUPERHEROES
DESCRIBE TABLE SUPERHEROES;
{{< /highlight >}}

## Run A Query On The Describe Query's Output

{{< highlight sql >}}
-- Select the "name" and "type" columns
SELECT "name", "type" 
-- Of the last query (in this case the DESCRIBE TABLE query)
FROM TABLE(RESULT_SCAN(LAST_QUERY_ID()))
;
{{< /highlight >}}
<table border=1>
    <thead>
        <tr>
            <th>name</th>
            <th>type</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ID</td>
            <td>VARCHAR(5)</td>
        </tr>
        <tr>
            <td>NAME</td>
            <td>VARCHAR(100)</td>
        </tr>
        <tr>
            <td>ALTER_EGO</td>
            <td>VARCHAR(100)</td>
        </tr>
    </tbody>
</table>




    



