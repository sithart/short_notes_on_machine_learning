---
title: "Use Command Line Arguments In A Function"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "How to use command line arguments in a function in Python."
type: technical_note
draft: false
---
## Preliminary


```python
# Load library
import argparse
```

## Create Python Code


```python
#!/usr/bin/env python3

# Create a function with two inputs
def sum_two_values(value_one, value_two):
    
    # Add together two values
    _sum = value_one + value_two
    
    # Return sum
    return _sum


# If the script is run
if __name__ == '__main__':
    
    # Create argument parser
    parser = argparse.ArgumentParser()
    
    # Create an argument called v1 or value_1 that is an integer
    parser.add_argument('-v1', '--value_1', type=int, help='The first value.')
    
    # Create a required argument called v2 or value_2 that is an integer
    parser.add_argument('-v2', '--value_2', type=int, help='The second value.', required=True)
    
    # Parse arguments
    args = parser.parse_args()

    # Assign arguments to variables
    value_one = args.v1
    value_two = args.v2
    
    # Run function with argument variables as inputs
    sum_two_values(value_one, value_two)
```

## Run In Command Line

./python_code.py -v1 2 -v2 8
