---
title: "Convert Columns Into Rows"
author: "Chris Albon"
date: 2019-01-28T00:00:00-07:00
description: "How to convert columns into rows (i.e. unpivoting) in Snowflake using SQL."
type: technical_note
draft: false
---

`UNPIVOT` converts a table's columns into rows.

## Create Table Of Superheroes

{{< highlight sql >}}
-- Create a table called SUPERHEROES.
CREATE OR REPLACE TABLE SUPERHEROES (
  -- Column called ALTER_EGO allowing up to 100 characters
  "ALTER_EGO" VARCHAR(100),
  -- Column called BANK_BALANCE of integers
  "AGE" INT,
  -- Column called 2015 of integers
  "2015" INT,
  -- Column called 2016 of integers
  "2016" INT,
  -- Column called 2017 of integers
  "2017" INT,
  -- Column called 2018 of integers
  "2018" INT,
  -- Column called 2019 of integers
  "2019" INT
);
{{< /highlight >}}

## Insert Rows For Each Superhero

{{< highlight sql >}}
-- Insert rows into SUPERHEROES
INSERT INTO SUPERHEROES 
    -- With the values
    VALUES
    ('The Bomber', 45, 1, 5, 7, 8, 0),
    ('Mr. Money', 12, 1, 5, 7, 8, 2),
    ('Nuke Miner', 5, 3, 5, 5, 6, 2),
    ('The Knife', 43, 1, 2, 9, 8, 0),
    ('Ninka Baker', 32, 1, 5, 3, 8, 1),
    ('Banana Bomber', 34, 1, 3, 2, 8, 2),
    ('Augustine', 12, 1, 5, 7, 8, 0),
    ('The Kid', 21, 1, 5, 7, 3, 3),
    ('The Viking', 291, 2, 3, 7, 8, 0);
{{< /highlight >}}

## Convert Years Columns Into Rows

{{< highlight sql >}}
-- Select all columns from SUPERHEROES
SELECT * FROM SUPERHEROES
-- Convert the columns "2015", "2016", "2017", "2018", "2019" into
-- rows with appropriate values in a new a YEARS column 
UNPIVOT(YEAR FOR YEARS IN ("2015", "2016", "2017", "2018", "2019"));
{{< /highlight >}}
<table border=1>
    <thead>
        <tr>
            <th>ALTER_EGO</th>
            <th>AGE</th>
            <th>YEAR</th>
            <th>KILLS</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>The Bomber</td>
            <td>45</td>
            <td>2015</td>
            <td>1</td>
        </tr>
        <tr>
            <td>The Bomber</td>
            <td>45</td>
            <td>2016</td>
            <td>5</td>
        </tr>
        <tr>
            <td>The Bomber</td>
            <td>45</td>
            <td>2017</td>
            <td>7</td>
        </tr>
        <tr>
            <td>The Bomber</td>
            <td>45</td>
            <td>2018</td>
            <td>8</td>
        </tr>
        <tr>
            <td>The Bomber</td>
            <td>45</td>
            <td>2019</td>
            <td>0</td>
        </tr>
        <tr>
            <td>Mr. Money</td>
            <td>12</td>
            <td>2015</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Mr. Money</td>
            <td>12</td>
            <td>2016</td>
            <td>5</td>
        </tr>
        <tr>
            <td>Mr. Money</td>
            <td>12</td>
            <td>2017</td>
            <td>7</td>
        </tr>
        <tr>
            <td>Mr. Money</td>
            <td>12</td>
            <td>2018</td>
            <td>8</td>
        </tr>
        <tr>
            <td>Mr. Money</td>
            <td>12</td>
            <td>2019</td>
            <td>2</td>
        </tr>
        <tr>
            <td>Nuke Miner</td>
            <td>5</td>
            <td>2015</td>
            <td>3</td>
        </tr>
        <tr>
            <td>Nuke Miner</td>
            <td>5</td>
            <td>2016</td>
            <td>5</td>
        </tr>
        <tr>
            <td>Nuke Miner</td>
            <td>5</td>
            <td>2017</td>
            <td>5</td>
        </tr>
        <tr>
            <td>Nuke Miner</td>
            <td>5</td>
            <td>2018</td>
            <td>6</td>
        </tr>
        <tr>
            <td>Nuke Miner</td>
            <td>5</td>
            <td>2019</td>
            <td>2</td>
        </tr>
        <tr>
            <td>The Knife</td>
            <td>43</td>
            <td>2015</td>
            <td>1</td>
        </tr>
        <tr>
            <td>The Knife</td>
            <td>43</td>
            <td>2016</td>
            <td>2</td>
        </tr>
        <tr>
            <td>The Knife</td>
            <td>43</td>
            <td>2017</td>
            <td>9</td>
        </tr>
        <tr>
            <td>The Knife</td>
            <td>43</td>
            <td>2018</td>
            <td>8</td>
        </tr>
        <tr>
            <td>The Knife</td>
            <td>43</td>
            <td>2019</td>
            <td>0</td>
        </tr>
        <tr>
            <td>Ninka Baker</td>
            <td>32</td>
            <td>2015</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Ninka Baker</td>
            <td>32</td>
            <td>2016</td>
            <td>5</td>
        </tr>
        <tr>
            <td>Ninka Baker</td>
            <td>32</td>
            <td>2017</td>
            <td>3</td>
        </tr>
        <tr>
            <td>Ninka Baker</td>
            <td>32</td>
            <td>2018</td>
            <td>8</td>
        </tr>
        <tr>
            <td>Ninka Baker</td>
            <td>32</td>
            <td>2019</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Banana Bomber</td>
            <td>34</td>
            <td>2015</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Banana Bomber</td>
            <td>34</td>
            <td>2016</td>
            <td>3</td>
        </tr>
        <tr>
            <td>Banana Bomber</td>
            <td>34</td>
            <td>2017</td>
            <td>2</td>
        </tr>
        <tr>
            <td>Banana Bomber</td>
            <td>34</td>
            <td>2018</td>
            <td>8</td>
        </tr>
        <tr>
            <td>Banana Bomber</td>
            <td>34</td>
            <td>2019</td>
            <td>2</td>
        </tr>
        <tr>
            <td>Augustine</td>
            <td>12</td>
            <td>2015</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Augustine</td>
            <td>12</td>
            <td>2016</td>
            <td>5</td>
        </tr>
        <tr>
            <td>Augustine</td>
            <td>12</td>
            <td>2017</td>
            <td>7</td>
        </tr>
        <tr>
            <td>Augustine</td>
            <td>12</td>
            <td>2018</td>
            <td>8</td>
        </tr>
        <tr>
            <td>Augustine</td>
            <td>12</td>
            <td>2019</td>
            <td>0</td>
        </tr>
        <tr>
            <td>The Kid</td>
            <td>21</td>
            <td>2015</td>
            <td>1</td>
        </tr>
        <tr>
            <td>The Kid</td>
            <td>21</td>
            <td>2016</td>
            <td>5</td>
        </tr>
        <tr>
            <td>The Kid</td>
            <td>21</td>
            <td>2017</td>
            <td>7</td>
        </tr>
        <tr>
            <td>The Kid</td>
            <td>21</td>
            <td>2018</td>
            <td>3</td>
        </tr>
        <tr>
            <td>The Kid</td>
            <td>21</td>
            <td>2019</td>
            <td>3</td>
        </tr>
        <tr>
            <td>The Viking</td>
            <td>291</td>
            <td>2015</td>
            <td>2</td>
        </tr>
        <tr>
            <td>The Viking</td>
            <td>291</td>
            <td>2016</td>
            <td>3</td>
        </tr>
        <tr>
            <td>The Viking</td>
            <td>291</td>
            <td>2017</td>
            <td>7</td>
        </tr>
        <tr>
            <td>The Viking</td>
            <td>291</td>
            <td>2018</td>
            <td>8</td>
        </tr>
        <tr>
            <td>The Viking</td>
            <td>291</td>
            <td>2019</td>
            <td>0</td>
        </tr>
    </tbody>
</table>