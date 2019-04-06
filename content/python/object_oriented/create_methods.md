---
title: "Create Methods"
author: "Chris Albon"
date: 2018-12-16T11:53:49-07:00
description: "How to create methods for a class in object oriented programming in Python."
type: technical_note
draft: false
---
## Create Simple Class


```python
# Create a class called Soldier
class Soldier:
    """Creates a class representing a soldier."""
    
    # Whenever an object is created from this class,
    # assign the name and initial rank.
    def __init__(self, name, rank):
        self.name = name
        self.rank = 1
        
    # Promote soldier to a higher rank
    def promote(self):
        # Set rank to current rank plus one
        self.rank = self.rank + 1
```

## Create Soldier Named Jason


```python
# Create an instance of Soldier class called 'jason'
jason = Soldier('Jason Miller', 1)
```

## View Jason's Attributes


```python
# Display a dictionary of attributes
jason.__dict__
```




    {'name': 'Jason Miller', 'rank': 1}



## View Jason's Rank


```python
jason.rank
```




    1



## Promote Jason


```python
jason.promote()
```

## View Jason's Rank


```python
jason.rank
```




    2


