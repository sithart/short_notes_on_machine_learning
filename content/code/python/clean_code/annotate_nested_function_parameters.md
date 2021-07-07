---
title: "Annotate Nested Function Parameters"
author: "Chris Albon"
date: 2021-02-19T00:00:00-07:00
description: "How to annotate a function with nested parameters in Python."
type: technical_note
draft: false
aliases: [/python/clean_code/annotate_nested_function_parameters/]
---
_This tutorial is inspired by [Clean Code in Python](https://amzn.to/3ue4Ywv) by Mariano Anaya._

Python annotations allow us to softly define the data types of function inputs. However, commonly the parameter is a data type that contains other data types, for example a list containing integers.

## Preliminaries


```python
# Import typing library
import typing
```

## Create Variables


```python
# Create two variables to use as inputs to the function
fruit = 'Apple'
pieces = 12
basket = (fruit, pieces)
```

## Create Function


```python
# Create a function called describe_fruit that has one parameter,
# called "container" that is expected to be a tuple containing a string and an integer.
# The output of the function should be a string.
def describe_fruit(container: typing.Tuple[str, int]) -> str:
    
    # Create output from the inputs
    description = "We have " + str(container[1]) + " pieces of " + container[0]
    
    # Return the output
    return description
```

## Execute Function


```python
# Run function with inputs
describe_fruit(basket)
```




    'We have 12 pieces of Apple'



## View Function's Annotations


```python
# List the annotations of the function
describe_fruit.__annotations__
```




    {'container': typing.Tuple[str, int], 'return': str}


