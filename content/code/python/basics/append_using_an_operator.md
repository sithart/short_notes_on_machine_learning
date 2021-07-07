---
title: "Append Using The Operator"
author: "Chris Albon"
date: 2018-12-16T11:53:49-07:00
description: "How to append a value using the operator in Python."
type: technical_note
draft: false
aliases: [/python/basics/append_using_an_operator/]
---
## Create A List


```python
# Create a list of three names
names = ['chris', 'nguyen', 'jack']
```

## Create A Value To Append To The List


```python
# Create a string list variable containing a name
to_append = ['sarah']
```

## Append Value To List


```python
# Create a new list with all the original names plus the appended name
names += to_append
```

## View New List


```python
# View the new list
names
```




    ['chris', 'nguyen', 'jack', 'sarah']


