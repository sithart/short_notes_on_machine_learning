---
title: "Create PostgreSQL Database With Python"
author: "Chris Albon"
date: 2018-06-18T11:53:49-07:00
description: "How to create a PostgreSQL database using Python."
type: technical_note
draft: false
---
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

    Query started at 12:44:03 PM MST; Query executed in 0.00 m

## Populate Table With Data


```python
%%read_sql -d 

INSERT INTO staff (first_name, city_name, age) 
VALUES ('Jill', 'Miller', 30),
       ('Steve', 'Miller', 24),
       ('Sarah', 'Jackson', 25);
```

    Query started at 12:44:03 PM MST; Query executed in 0.00 m

## Retrieve All Records


```python
%%read_sql

-- Select all records from the staff table
SELECT * FROM staff;
```

    Query started at 12:44:03 PM MST; Query executed in 0.00 m




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
    <tr>
      <th>2</th>
      <td>Sarah</td>
      <td>Jackson</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>


