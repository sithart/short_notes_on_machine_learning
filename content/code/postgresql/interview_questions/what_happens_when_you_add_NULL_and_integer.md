---
title: "What Happens When You Add NULL And Integer"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "What happens when you add a NULL value and an integer in an SQL database."
type: technical_note
draft: false
aliases: [/postgresql/interview_questions/what_happens_when_you_add_NULL_and_integer/]
---

## Question

What happens when you add a NULL value and an integer?

## Answer

You get an error.

{{< highlight sql >}}
-- Drop table if exists
DROP TABLE IF EXISTS names;

-- Create table called names
CREATE TABLE names (
    -- string variable
    name varchar(255),
    -- integer variable
    score int
)
{{< /highlight >}}

{{< highlight sql >}}
-- Insert into the table
INSERT INTO names (name, score)
-- two rows
VALUES
    (NULL, 1),
    ('Tommy', 1)
{{< /highlight >}}

{{< highlight sql >}}
-- Add a column with a NULL value and a integer
SELECT
    name + score as results
FROM names
{{< /highlight >}}
```
[42883] ERROR: operator does not exist: character varying + integer Hint: No operator matches the given name and argument type(s). You might need to add explicit type casts. Position: 17
```