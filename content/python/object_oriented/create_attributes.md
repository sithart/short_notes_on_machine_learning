---
title: "Create Attributes"
author: "Chris Albon"
date: 2018-12-16T11:53:49-07:00
description: "How to create attributes for a class in object oriented programming in Python."
type: technical_note
draft: false
---
## Create Simple Class


```python
class Soldier: 
    pass
```

## Create Instance Of Class


```python
jason = Soldier()
```

## Create Attribute


```python
jason.age = 36
jason.height = 124
```

## View Attributes


```python
# Display a dictionary of attributes
jason.__dict__
```




    {'age': 36, 'height': 124}


