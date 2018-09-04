---
title: "Mathematical Operations On Columns"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to conduct mathematical operations on columns in an SQL database."
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
    race varchar(255)
)
{{< /highlight >}}

## Insert Rows

{{< highlight sql >}}
-- Insert into the table adventurers
INSERT INTO adventurers (name, age, race)
VALUES ('Fjoak Doom-Wife', 28, 'Human'),
       ('Alooneric Cortte', 29, 'Elf'),
       ('Piperel Ramsay', 35, 'Elf'),
       ('Casimir Yardley', 14, 'Elf')
{{< /highlight >}}

## Apply Addition To Column

{{< highlight sql >}}
-- Apply operation
UPDATE adventurers SET age = age + 10
{{< /highlight >}}

## View Table

{{< highlight sql >}}
-- Retrieve data
SELECT * FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>38</td><td>Human</td></tr>
<tr><td>Alooneric Cortte</td><td>39</td><td>Elf</td></tr>
<tr><td>Piperel Ramsay</td><td>45</td><td>Elf</td></tr>
<tr><td>Casimir Yardley</td><td>24</td><td>Elf</td></tr></table>

## Apply Substraction To Column

{{< highlight sql >}}
-- Apply operation
UPDATE adventurers SET age = age - 10
{{< /highlight >}}

## View Table

{{< highlight sql >}}
-- Retrieve data
SELECT * FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>28</td><td>Human</td></tr>
<tr><td>Alooneric Cortte</td><td>29</td><td>Elf</td></tr>
<tr><td>Piperel Ramsay</td><td>35</td><td>Elf</td></tr>
<tr><td>Casimir Yardley</td><td>14</td><td>Elf</td></tr></table>

## Apply Multiplication To Column

{{< highlight sql >}}
-- Apply operation
UPDATE adventurers SET age = age * 10
{{< /highlight >}}

## View Table

{{< highlight sql >}}
-- Retrieve data
SELECT * FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>280</td><td>Human</td></tr>
<tr><td>Alooneric Cortte</td><td>290</td><td>Elf</td></tr>
<tr><td>Piperel Ramsay</td><td>350</td><td>Elf</td></tr>
<tr><td>Casimir Yardley</td><td>140</td><td>Elf</td></tr></table>

## Apply Division To Column

{{< highlight sql >}}
-- Apply operation
UPDATE adventurers SET age = age / 10
{{< /highlight >}}

## View Table

{{< highlight sql >}}
-- Retrieve data
SELECT * FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>28</td><td>Human</td></tr>
<tr><td>Alooneric Cortte</td><td>29</td><td>Elf</td></tr>
<tr><td>Piperel Ramsay</td><td>35</td><td>Elf</td></tr>
<tr><td>Casimir Yardley</td><td>14</td><td>Elf</td></tr></table>

## Apply Modulo To Column

{{< highlight sql >}}
-- Apply operation
UPDATE adventurers SET age = age % 10
{{< /highlight >}}

## View Table

{{< highlight sql >}}
-- Retrieve data
SELECT * FROM adventurers
{{< /highlight >}}
<table border="1" style="border-collapse:collapse">
<tr><th>name</th><th>age</th><th>race</th></tr>
<tr><td>Fjoak Doom-Wife</td><td>8</td><td>Human</td></tr>
<tr><td>Alooneric Cortte</td><td>9</td><td>Elf</td></tr>
<tr><td>Piperel Ramsay</td><td>5</td><td>Elf</td></tr>
<tr><td>Casimir Yardley</td><td>4</td><td>Elf</td></tr></table>
