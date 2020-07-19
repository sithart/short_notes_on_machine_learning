---
title: "Linear Interpolation"
author: "Chris Albon"
date: 2019-12-20T11:53:49-07:00
description: "Linear Interpolation Using Python."
type: technical_note
draft: false
---
Linear interpolation is used when we want to calculate a value between two points.

Imagine we want to calculate some point, $(x, y)$ that is between two other points $(x_1, y_1)$ and $(x_2, y_2)$. To do this, we first select some value $x$ value (often halfway between $x_2$ and $x_1$ on the x-axis) and then calculate $x$'s corresponding $y$ value using the following formula:

$$y = y_1 + \frac{y_2 - y_1}{x_2 - x_1} * (x-x_1)$$


## Create Two Coordinates


```python
# Coordinates for x_1 and y_1
x1 = 0
y1 = 0

# Coordinates for x_2 and y_2
x2 = 10
y2 = 100
```

## Select x Value


```python
# Select an x value half way between x2 and x1 on the x-axis
x = ((x2 - x1)/2) + x1

# View x
x
```




    5.0



## Create Function For Linear Interpolation


```python
# Create a function
def interpolate_y(x, x1, y1, x2, y2):
    
    # Linear interpolation formula
    y = y1 + ((y2 - y1)/(x2 - x1)) * (x - x1)
    
    # Return y
    return y
```

## Calculate y


```python
# Interpolate y
y = interpolate_y(x, x1, y1, x2, y2)
```

## Print x 


```python
x
```




    5.0



## Print y


```python
y
```




    50.0


