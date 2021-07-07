---
title: "Tuples Vs. Named Tuples"
author: "Chris Albon"
date: 2020-06-24T11:53:49-07:00
description: "What is the difference between tuples and named tuples"
type: technical_note
draft: false
aliases: [/python/basics/tuples_vs_named_tuples/]
---
## Preliminaries


```python
# Import the collections library
import collections
```

## Create A Tuple

A tuple is a simple, efficient data type widely used in Python. However, it uses numerical indexes which can be frustrating to use when tuples are large.


```python
# Create a long tuple
employee = ('Jane',
            'Miller',
            'Engineer',
            '29',
            '3023 Homespun Place',
            '#4023',
            'Jacksonville',
            'FL',
            '49342',
            'USA'
           )
```

## View Tuple


```python
# Print tuple
employee
```




    ('Jane',
     'Miller',
     'Engineer',
     '29',
     '3023 Homespun Place',
     '#4023',
     'Jacksonville',
     'FL',
     '49342',
     'USA')



## Select State Value From Tuple


```python
# The state is the 7th element in the tuple, so the index is 6
employee[6]
```




    'Jacksonville'



## Create A Named Tuple

Named tuples are special variation of tuples that are just as memory efficent but allows you to select elements in tuples by name.


```python
# Create a new named tuple class called Person
Person = collections.namedtuple('Person', 
                                # containing these fields
                                'first_name lastname job age address_1 address_2 city, state, zip, country')
```


```python
# Create a named tuple instance called customer
customer = Person(first_name = 'Jane',
                  lastname = 'Miller',
                  job = 'Engineer',
                  age = '29',
                  address_1 = '3023 Homespun Place',
                  address_2 = '#4023',
                  city = 'Jacksonville',
                  state = 'FL',
                  zip = '49342',
                  country = 'USA'
                 )
```


```python
# View the state
customer.state
```




    'FL'


