---
title: "Calculate Requests Sent"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to calculate requests sent in an SQL database."
type: technical_note
draft: false
aliases: [/postgresql/interview_questions/calculate_requests_sent/]
---

## Question

You are given a table containing a country code, the number of requests attempted, and the percentage of those requests that failed to sent. Calculate:

1. The total number of requests attempted by country.
2. The total number of failed requests attempted by country.

## Answer

## Create Table

{{< highlight sql >}}
-- Drop table if exists
DROP TABLE IF EXISTS global_usage

-- Create table called documents
CREATE TABLE global_usage (
    -- string variable
    country varchar(255),
    -- integer variable
    requests_attempted int,
    -- float variable
    percent_requests_failed float
);
{{< /highlight >}}

## Insert Data Into Table

{{< highlight sql >}}
-- Insert data into the table
INSERT INTO global_usage (country, requests_attempted, percent_requests_failed)
VALUES
    ('US', 100, .2),
    ('US', 100, .1),
    ('US', 100, .5),
    ('NZ', 100, .1),
    ('NZ', 100, .2),
    ('NZ', 100, .3),
    ('NZ', 100, .5);
{{< /highlight >}}

## View Table

{{< highlight sql >}}
-- View the raw table
SELECT * FROM global_usage;
{{< /highlight >}}
<table>
<tr><th>country</th><th>requests_attempted</th><th>percent_requests_failed</th></tr>
<tr><td>US</td><td>100</td><td>0.2</td></tr>
<tr><td>US</td><td>100</td><td>0.1</td></tr>
<tr><td>US</td><td>100</td><td>0.5</td></tr>
<tr><td>NZ</td><td>100</td><td>0.1</td></tr>
<tr><td>NZ</td><td>100</td><td>0.2</td></tr>
<tr><td>NZ</td><td>100</td><td>0.3</td></tr>
<tr><td>NZ</td><td>100</td><td>0.5</td></tr></table>

## Calculate Total Requests Attempted By Country

{{< highlight sql >}}
-- Select
SELECT
   -- the country
   country,
   -- the sum of requests attempted
   sum(requests_attempted)
-- From the global usage table
FROM global_usage
-- Aggregate the rows
GROUP BY
    -- by country
    country;
{{< /highlight >}}
<table>
<tr><th>country</th><th>sum</th></tr>
<tr><td>US</td><td>300</td></tr>
<tr><td>NZ</td><td>400</td></tr></table>

## Calculate Total Failed Requests By Country

{{< highlight sql >}}
-- Select
SELECT
   -- the country
   country,
   -- the sum of the number of requests attempted and the number of requests they were failed
   sum(requests_attempted * percent_requests_failed) as total_failed
-- from the table
FROM global_usage
-- aggregated by country
GROUP BY country
{{< /highlight >}}
<table>
<tr><th>country</th><th>total_failed</th></tr>
<tr><td>US</td><td>80</td></tr>
<tr><td>NZ</td><td>110</td></tr></table>