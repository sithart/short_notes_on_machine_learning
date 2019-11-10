---
title: "Create Table With Column And Table Comments"
author: "Chris Albon"
date: 2019-01-28T00:00:00-07:00
description: "How to create a table with column and table comments in Snowflake using SQL."
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
COMMENT='A table for superheroes.'
;
{{< /highlight >}}