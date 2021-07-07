---
title: "Override Parent Class"
author: "Chris Albon"
date: 2020-12-16T11:53:49-07:00
description: "How to override a parent class in obhject oriented Python."
type: technical_note
draft: false
aliases: [/python/object_oriented/override_parent_class/]
---
## Create Parent Class


```python
# Create a class called `parent`
class Parent:
    
    # Create an init method with fruit and protein
    def __init__(self, fruit, meat):
        
        # Assign fruit and meat values
        self.fruit = fruit
        self.meat = meat
```

## Create Child Class Override Parent Class


```python
# Create a class called `parent`
class Child(Parent):
    
    # Create an init method with fruit and protein
    def __init__(self, fruit, veggie):
        
        # Override Parent class and replace meat attribute with veggie attribute
        super().__init__(fruit, veggie)
        
        # Assign fruit, vegtable, and grain values
        self.fruit = fruit
        self.veggie = veggie
        self.meat = False
```

## Create Instance Of Parent Class


```python
meal_1 = Parent(fruit='apple', meat='fish')
```

## Create Instance Of Child Class


```python
meal_2 = Child(fruit='apple', veggie='onion')
```

## View Parent Class


```python
meal_1.__dict__
```




    {'fruit': 'apple', 'meat': 'fish'}



## View Child Class


```python
meal_2.__dict__
```




    {'fruit': 'apple', 'meat': False, 'veggie': 'onion'}


