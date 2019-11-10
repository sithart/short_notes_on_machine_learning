---
title: "View A Table's Comments"
author: "Chris Albon"
date: 2019-01-28T00:00:00-07:00
description: "How to view a table's comments in SQL using Snowflake.."
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
  "ALTER_EGO" VARCHAR(100) COMMENT 'The superheroe\'s pseudonym.'
) 
-- A comment for the entire table.
COMMENT='A table for superheroes.'
;
{{< /highlight >}}

## View Table Metadata

{{< highlight sql >}}
-- Show the metadata on all tables called SUPERHEROES
SHOW TABLES LIKE 'SUPERHEROES';
{{< /highlight >}}

## View Table's Comments

{{< highlight sql >}}
-- Select the "name" and "comment" columns
SELECT "name", "comment" 
-- Of the last query (in this case the SHOW TABLES LIKE 'SUPERHEROES query)
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
            <td>SUPERHEROES</td>
            <td>A table to superheroes.</td>
        </tr>
    </tbody>
</table>