---
title: "Sort By Natural Ordering"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to sort by natural ordering in an SQL database."
type: technical_note
draft: false
aliases: [/postgresql/interview_questions/sort_column_natural_ordering/]
---

## Question

You are given a column of strings, sort them in natural order.

## Answer

Natural ordering is simply the ordering that a human would expect.

### Create Table

{{< highlight sql >}}
CREATE TABLE documents (
    -- string variable
    name varchar(255)
)
{{< /highlight >}}

### Insert Values Into Table

{{< highlight sql >}}
-- Insert into the table documents
INSERT INTO documents (name)
-- a list of files (notice the numbering)
VALUES
    ('file1.txt'),
    ('file2.txt'),
    ('file3.txt'),
    ('file4.txt'),
    ('file5.txt'),
    ('file6.txt'),
    ('file7.txt'),
    ('file8.txt'),
    ('file9.txt'),
    ('file10.txt'),
    ('file11.txt'),
    ('file12.txt'),
    ('file13.txt'),
    ('file14.txt'),
    ('file15.txt')
{{< /highlight >}}

### View Table

{{< highlight sql >}}
-- View all the rows
SELECT * FROM documents
{{< /highlight >}}
<table>
<tr><th>name</th></tr>
<tr><td>file1.txt</td></tr>
<tr><td>file2.txt</td></tr>
<tr><td>file3.txt</td></tr>
<tr><td>file4.txt</td></tr>
<tr><td>file5.txt</td></tr>
<tr><td>file6.txt</td></tr>
<tr><td>file7.txt</td></tr>
<tr><td>file8.txt</td></tr>
<tr><td>file9.txt</td></tr>
<tr><td>file10.txt</td></tr>
<tr><td>file11.txt</td></tr>
<tr><td>file12.txt</td></tr>
<tr><td>file13.txt</td></tr>
<tr><td>file14.txt</td></tr>
<tr><td>file15.txt</td></tr></table>

### View Table Sorted In Non-Natural Order

Notice that simply using `ORDER BY` creates a non-natural ordering.

{{< highlight sql >}}
-- View all the rows
SELECT * FROM documents
-- Order them alphanumerically
ORDER BY name
{{< /highlight >}}
<table>
<tr><th>name</th></tr>
<tr><td>file10.txt</td></tr>
<tr><td>file11.txt</td></tr>
<tr><td>file12.txt</td></tr>
<tr><td>file13.txt</td></tr>
<tr><td>file14.txt</td></tr>
<tr><td>file15.txt</td></tr>
<tr><td>file1.txt</td></tr>
<tr><td>file2.txt</td></tr>
<tr><td>file3.txt</td></tr>
<tr><td>file4.txt</td></tr>
<tr><td>file5.txt</td></tr>
<tr><td>file6.txt</td></tr>
<tr><td>file7.txt</td></tr>
<tr><td>file8.txt</td></tr>
<tr><td>file9.txt</td></tr></table>

### View Table Sorted In Natural Order

The solution is to sort by length and then alphanumerically.

{{< highlight sql >}}
-- View all the rows
SELECT * FROM documents
-- Order them by length and then alphanumerically
ORDER BY LENGTH(name), name
{{< /highlight >}}
<table>
<tr><th>name</th></tr>
<tr><td>file1.txt</td></tr>
<tr><td>file2.txt</td></tr>
<tr><td>file3.txt</td></tr>
<tr><td>file4.txt</td></tr>
<tr><td>file5.txt</td></tr>
<tr><td>file6.txt</td></tr>
<tr><td>file7.txt</td></tr>
<tr><td>file8.txt</td></tr>
<tr><td>file9.txt</td></tr>
<tr><td>file10.txt</td></tr>
<tr><td>file11.txt</td></tr>
<tr><td>file12.txt</td></tr>
<tr><td>file13.txt</td></tr>
<tr><td>file14.txt</td></tr>
<tr><td>file15.txt</td></tr></table>