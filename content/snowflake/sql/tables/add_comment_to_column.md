---
title: "Add Comment To Column"
author: "Chris Albon"
date: 2019-01-28T00:00:00-07:00
description: "Add comments to a column using SQL in Snowflake."
type: technical_note
draft: false
---

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

## Describe Table (To See Comments)

{{< highlight sql >}}
-- Describe table
DESCRIBE TABLE SUPERHEROES;
{{< /highlight >}}
<table border=1>
    <thead>
        <tr>
            <th>name</th>
            <th>type</th>
            <th>kind</th>
            <th>null?</th>
            <th>default</th>
            <th>primary key</th>
            <th>unique key</th>
            <th>check</th>
            <th>expression</th>
            <th>comment</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ID</td>
            <td>VARCHAR(5)</td>
            <td>COLUMN</td>
            <td>Y</td>
            <td></td>
            <td>N</td>
            <td>N</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>NAME</td>
            <td>VARCHAR(100)</td>
            <td>COLUMN</td>
            <td>Y</td>
            <td></td>
            <td>N</td>
            <td>N</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>ALTER_EGO</td>
            <td>VARCHAR(100)</td>
            <td>COLUMN</td>
            <td>Y</td>
            <td></td>
            <td>N</td>
            <td>N</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>

## Add Comment To Column

Note: If a comment already exists, this will override it.

{{< highlight sql >}}
-- If it exists, comment...
COMMENT IF EXISTS 
-- The "ALTER_EGO" column in the table "SUPERHEROES"
ON COLUMN SUPERHEROES.ALTER_EGO
-- With this string
IS 'This is a column of the superhero aliases';
{{< /highlight >}}

## Describe Table (To See Comments)

{{< highlight sql >}}
-- Describe table
DESCRIBE TABLE SUPERHEROES;
{{< /highlight >}}
<table border=1>
    <thead>
        <tr>
            <th>name</th>
            <th>type</th>
            <th>kind</th>
            <th>null?</th>
            <th>default</th>
            <th>primary key</th>
            <th>unique key</th>
            <th>check</th>
            <th>expression</th>
            <th>comment</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ID</td>
            <td>VARCHAR(5)</td>
            <td>COLUMN</td>
            <td>Y</td>
            <td></td>
            <td>N</td>
            <td>N</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>NAME</td>
            <td>VARCHAR(100)</td>
            <td>COLUMN</td>
            <td>Y</td>
            <td></td>
            <td>N</td>
            <td>N</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>ALTER_EGO</td>
            <td>VARCHAR(100)</td>
            <td>COLUMN</td>
            <td>Y</td>
            <td></td>
            <td>N</td>
            <td>N</td>
            <td></td>
            <td></td>
            <td>This is a column of the superhero aliases</td>
        </tr>
    </tbody>
</table>