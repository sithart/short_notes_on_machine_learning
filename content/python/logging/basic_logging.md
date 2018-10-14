---
title: "Basic Logging"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Use basic logging using Python."
type: technical_note
draft: false
---
## Preliminaries


```python
# Import standard library's logging
import logging
```

## Configure Logging


```python
# Configure logging to ignore messages below info (i.e. debug level is ignored)
logging.basicConfig(level=logging.INFO)
```

## Create Function


```python
# Create function that converts dollars to cents
def convert_dollars_to_cents(dollars):
    
    # Try...
    try:
        # Multiply dollars by 100
        cents = dollars * 100    
        
        # Convert to integer
        cents = int(cents)
        
        # Send info message that function was run successful
        logging.info("convert_dollars_to_cents run successfully")
        
        # Return cents
        return cents
    
    # If a ValueError is raised
    except ValueError:
        
        # Create data type of input
        dollars_type = type(dollars)
        
        # Create error message detailing the error
        error_message = f"Function input is {dollars_type}, should be <class \'int\'>"
        
        # Send error message
        logging.error(error_message)
```

## Run Function With Argument That Works


```python
# Run function with a float value
convert_dollars_to_cents(12.45)
```

    INFO:root:convert_dollars_to_cents run successfully





    1245



## Run Function With Argument That Produces Error


```python
# Run function with a string value
convert_dollars_to_cents("dsfsd")
```

    ERROR:root:Function input is <class 'str'>, should be <class 'int'>

