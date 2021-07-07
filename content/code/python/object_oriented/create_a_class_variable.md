---
title: "Create A Class Variable"
author: "Chris Albon"
date: 2018-12-16T11:53:49-07:00
description: "How to create a variable for a class in object oriented programming in Python."
type: technical_note
draft: false
aliases: [/python/object_oriented/create_a_class_variable/]
---
Class variables are shared by all instances of that class. For example, if a class variable is a list, all instances of that class can modify that single list.

## Create Class Containing Class Variable


```python
# Create a class called persons
class person:
    
    # Create list variable that is shared amongst all classes
    # i.e. a class variable
    all_persons = []

    # Create an init method requiring a name argument
    def __init__(self, name):
        
        # Set the name variable
        self.name = name
        
        # Add the name variable to the class variable
        person.all_persons.append(self.name)
```

## Create three instances of the `person` class

Notice that in the code above when we initiative a class we append a name of the `all_persons` class variable.


```python
bob = person('Bob')
jack = person('Jack')
jill = person('Jill')
```

## View class variable


```python
person.all_persons
```




    ['Bob', 'Jack', 'Jill']



## Create two more instances of the `person` class


```python
sarah = person('Sarah')
bill = person('Bill')
```

## View class variable


```python
person.all_persons
```




    ['Bob', 'Jack', 'Jill', 'Sarah', 'Bill']


