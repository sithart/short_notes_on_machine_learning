---
title: "Function Example"
author: "Chris Albon"
date: 2018-12-16T11:53:49-07:00
description: "How to create a best practice function in Python."
type: technical_note
draft: false
aliases: [/python/basics/function_example/]
---
There are many features to use with functions in Python from docstrings to type annotation to naming conventions. This is my version of a best practice function in Python.

This function uses [numpydoc docstring format](https://numpydoc.readthedocs.io/en/latest/format.html) and [typing hinting](https://docs.python.org/3/library/typing.html).

## Create Function


```python
# Define a function called word_count that takes in a argument 
# called document is a string and outputs an integer.
def word_count(document: str) -> int:
    """Counts the number of words in a string.
    
    The purpose of this function is to count the number of words 
    (as defined by separation by spaces) in any string.
    
    Parameters
    ----------
    document : str
        A string representing a single document.
    
    Returns
    -------
    words : int
        The number of words in `document`
        
    Raises
    ------
    ValueError
        If `words` contains zero words, an error is raised to help the user.
        
    """
    
    # Split document by spaces and count the number of elements
    # in that list
    words = len(document.split()) 
    
    # If there are zero words,
    if words == 0:
        # raise an error
        raise ValueError('`words` must contain at least one word')
    
    # Return word count
    return words
```

## Run Function


```python
# Create a string
hemingway_quote = "But man is not made for defeat. A man can be destroyed but not defeated."

# Run word_count function
word_count(hemingway_quote)
```




    15


