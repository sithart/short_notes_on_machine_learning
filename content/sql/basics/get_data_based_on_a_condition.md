---
title: "Get Data Based On A Condition"
author: "Chris Albon"
date: 2018-06-18T11:53:49-07:00
description: "Retrieve certain records based on a conditional into an SQL database."
type: technical_note
draft: false
---
Note: This tutorial was created in a [Jupyter Notebook](http://jupyter.org/). `%%read_sql` is a [Jupyter magic command](http://engineering.pivotal.io/post/introducing-sql-magic/) and can be ignored when not using Jupyter Notebooks.

## Preliminaries


```python
# Load libraries
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists, drop_database

# Create PostgreSQL connection
engine = create_engine("postgres://localhost/notes_db")

# Load sql_magic so we can write SQL in Jupyter Notebooks
%load_ext sql_magic

# Setup SQL connection to the postgreSQL engine we created
%config SQL.conn_name = 'engine'
```



## Create Database


```python
# If a PostgreSQL database with this name exists
if database_exists(engine.url):
    # Delete PostgreSQL database 
    drop_database(engine.url)
    # Create empty PostgreSQL database
    create_database(engine.url)
# Otherwise
else:
    # Create empty PostgreSQL database
    create_database(engine.url)
```

## Create Table


```python
%%read_sql -d

CREATE TABLE staff ( 
    first_name varchar(255), 
    city_name varchar(255),
    age int
);
```

    Query started at 11:49:43 AM MST; Query executed in 0.00 m

## Populate Table With Data


```python
%%read_sql -d 

INSERT INTO staff (first_name, city_name, age) 
VALUES ('Jill', 'Miller', 30),
       ('Steve', 'Miller', 24),
       ('Sarah', 'Jackson', 25);
```

    Query started at 11:49:43 AM MST; Query executed in 0.00 m

## Retrieve Records Based On A Condition


```python
%%read_sql

-- Select all rows
SELECT * FROM staff
-- Where age is greater than 25
WHERE age > 25
```

    Query started at 11:49:43 AM MST; Query executed in 0.00 m




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>city_name</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jill</td>
      <td>Miller</td>
      <td>30</td>
    </tr>
  </tbody>
</table>
</div>




```python
%%read_sql

-- Select all rows
SELECT * FROM staff
-- Where age is greater than or equal to 25
WHERE age >= 25
```

    Query started at 11:49:43 AM MST; Query executed in 0.00 m




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>city_name</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jill</td>
      <td>Miller</td>
      <td>30</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Sarah</td>
      <td>Jackson</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>




```python
%%read_sql

-- Select all rows */
SELECT * FROM staff
-- Where city_name is "Miller" */
WHERE city_name = 'Miller'
```

    Query started at 11:49:43 AM MST; Query executed in 0.00 m




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>city_name</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jill</td>
      <td>Miller</td>
      <td>30</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Steve</td>
      <td>Miller</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>




```python
%%read_sql

-- Select all rows
SELECT * FROM staff
-- Where city_name is not "Miller"
WHERE city_name != 'Miller'
```

    Query started at 11:49:43 AM MST; Query executed in 0.00 m




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>city_name</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarah</td>
      <td>Jackson</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>


