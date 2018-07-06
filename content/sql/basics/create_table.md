---
title: "Create Table"
author: "Chris Albon"
date: 2018-06-18T11:53:49-07:00
description: "Create a table in an SQL database."
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

    The sql_magic extension is already loaded. To reload it, use:
      %reload_ext sql_magic


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

    Query started at 06:42:10 AM MST; Query executed in 0.00 m

## View Table


```python
%%read_sql

-- Select all records from the staff table
SELECT * FROM staff;
```

    Query started at 06:42:10 AM MST; Query executed in 0.00 m




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
  </tbody>
</table>
</div>


