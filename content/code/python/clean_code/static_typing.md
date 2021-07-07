---
title: "Static Typing Checking"
author: "Chris Albon"
date: 2021-02-19T00:00:00-07:00
description: "How to static type check in Python using Mypy"
type: technical_note
draft: false
aliases: [/python/clean_code/static_typing/]
---

## Create Variables
{{< highlight python >}}
# Create two variables to use as inputs to the function
fruit = 'Apple'
pieces = 'twelve'
{{< /highlight >}}

## Create Function
{{< highlight python >}}
# Create a function called describe_fruit that has two parameters,
# fruit_type that should be a string and fruit_number which should be an integer.
# The output of the function should be a string.
def describe_fruit(fruit_type: str, fruit_number: int) -> str:
    
    # Create output from the inputs
    description = "We have " + str(fruit_number) + " pieces of " + fruit_type 
    
    # Return the output
    return description
{{< /highlight >}}

## Run Function
{{< highlight python >}}
# Run function with inputs
describe_fruit(fruit, pieces)
{{< /highlight >}}
'We have twelve pieces of Apple'

## Run `mypy` In Command Line

**Notice** that `describe_fruit`'s annotations hint that `fruit_number` is an integer (`fruit_number: int`). However, `fruit_number` is a string (`pieces = 'twelve'`). Using mypy we can catch that mistake.

{{< highlight bash >}}
mypy static_typing.py
{{< /highlight >}}
static_typing.py:17: error: Argument 2 to "describe_fruit" has incompatible type "str"; expected "int"
Found 1 error in 1 file (checked 1 source file)
