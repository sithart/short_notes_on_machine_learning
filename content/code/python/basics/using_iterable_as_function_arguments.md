---
title: "Using Iterable As Function Arguments"
author: "Chris Albon"
date: 2020-07-12T11:00:00-00:00
description: "How to use an interable as the arguments to a function."
type: technical_note
draft: false
aliases: [/python/basics/using_iterable_as_function_arguments/]
---
## Create Arguments


```python
# Create a list with three values
scores = [1,2,3]
```


```python
# Create a dictionary with a single key-value pair
scores_with_names = {'amy_score': "200"}
```

## Create Function With Positional Arguments


```python
# Create a function with three positional arguments
def show_team_scores(jack_score, amy_score, sarah_score):
    # Print each of the positional arguments
    print(jack_score, amy_score, sarah_score)
```


```python
# Run the function with * and an iterable object (in this case a list)
show_team_scores(*scores)
```

    1 2 3


## Create Function Using Keyword Arguments


```python
# Create a function with three keyword arguments with default values
def show_team_scores(jack_score=0, amy_score=0, sarah_score=0):
    # Print each of the keyword arguments
    print(jack_score, amy_score, sarah_score)
```


```python
# Run the function with ** and a dictionary
show_team_scores(**scores_with_names)
```

    0 200 0


Notice how `jack_score` and `sarah_score` used the default values, while `amy_score` used the argument value we defined in `scores_with_names`.
