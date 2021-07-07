---
title: "Annotate Functions"
author: "Chris Albon"
date: 2021-02-19T00:00:00-07:00
description: "How to annotate a function in Python."
type: technical_note
draft: false
aliases: [/python/clean_code/annotate_functions/]
---
_This tutorial is inspired by [Clean Code in Python](https://amzn.to/3ue4Ywv) by Mariano Anaya._

Functions can include annotations providing additional information about the data type of a function's inputs and outputs. This information is not used by Python by default, but can be used by other libraries like [Mypy](https://mypy.readthedocs.io/en/stable/) to create [static-typing](https://en.wikipedia.org/wiki/Type_system#Static_and_dynamic_type_checking_in_practice).

## Create Variables


```python
# Create two variables to use as inputs to the function
fruit = 'Apple'
pieces = 12
```

## Create Function


```python
# Create a function called describe_fruit that has two parameters,
# fruit_type that should be a string and fruit_number which should be an integer.
# The output of the function should be a string.
def describe_fruit(fruit_type: str, fruit_number: int) -> str:
    
    # Create output from the inputs
    description = "We have " + str(fruit_number) + " pieces of " + fruit_type 
    
    # Return the output
    return description
```

## Execute Function


```python
# Run function with inputs
describe_fruit(fruit, pieces)
```




    'We have 12 pieces of Apple'



## View Function's Annotations


```python
# List the annotations of the function
describe_fruit.__annotations__
```




    {'fruit_type': str, 'fruit_number': int, 'return': str}


