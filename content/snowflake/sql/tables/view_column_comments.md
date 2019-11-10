---
title: "View A Column's Comments"
author: "Chris Albon"
date: 2019-01-28T00:00:00-07:00
description: "How to view a column's comments in SQL using Snowflake.."
type: technical_note
draft: false
---

## Create Table Of Superheroes With Comments

Column comments concern a particular column, while table comments are about the entire table.

{{< highlight sql >}}
-- Create a table called SUPERHEROES. If it already exists, replace it.
CREATE OR REPLACE TABLE SUPERHEROES (
  -- Column called ID allowing up to five characters with a comment.
  "ID" VARCHAR (5) COMMENT 'A unique ID for each superhero.', 
  -- Column called ALTER_EGO allowing up to 100 characters with a comment.
  "ALTER_EGO" VARCHAR(100) COMMENT 'The superhero\'s pseudonym.'
) 
-- A comment for the entire table.
COMMENT='A table to superheroes.'
;
{{< /highlight >}}

## Describe The Table

{{< highlight sql >}}
-- Describe the table SUPERHEROES
DESCRIBE TABLE SUPERHEROES;
{{< /highlight >}}

## View Table Comments

{{< highlight sql >}}
-- Select the "name" and "comment" columns
SELECT "name", "comment" 
-- Of the last query (in this case the DESCRIBE TABLE query)
FROM TABLE(RESULT_SCAN(LAST_QUERY_ID()))
;
{{< /highlight >}}
<table border=1>
    <thead>
        <tr>
            <th>name</th>
            <th>comment</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ID</td>
            <td>A unique ID for each superhero.</td>
        </tr>
        <tr>
            <td>ALTER_EGO</td>
            <td>The superhero's pseudonym.</td>
        </tr>
    </tbody>
</table>