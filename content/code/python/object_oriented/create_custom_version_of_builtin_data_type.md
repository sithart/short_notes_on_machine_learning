---
title: "Customize Built-in Data Types"
author: "Chris Albon"
date: 2018-12-16T11:53:49-07:00
description: "How to create  object oriented programming in Python."
type: technical_note
draft: false
aliases: [/python/object_oriented/create_custom_version_of_builtin_data_type/]
---
This is a toy example of how we can extending a built-in data type (i.e. a class) in Python to add additional functionality.

## Create New Class From `list`


```python
# Create a class that inherits from the built-in list class
class CapitalizedList(list):
    
    # Create a method called capitalize
    def capitalize(self):
        
        # Create a list
        capitalized_list = []
        
        # For each element in the instance
        for element in self:
            # Uppercase the string and append to the capitalized list
            capitalized_list.append(element.upper())
        
        # Return the capitalized list
        return capitalized_list
        
```

## Create Instance Of New Class


```python
capitalized_list = CapitalizedList()
```

## Add Elements To New Class


```python
capitalized_list.append('bob')
capitalized_list.append('sarah')
capitalized_list.append('miller')
```

## View Capitalized List Without Running `capitalize` Method


```python
capitalized_list
```




    ['bob', 'sarah', 'miller']



## View Capitalized List With Running `capitalize` Method


```python
capitalized_list.capitalize()
```




    ['BOB', 'SARAH', 'MILLER']


