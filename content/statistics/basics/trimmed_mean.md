---
title: "Trimmed Mean"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Trimmed Mean Using Python."
type: technical_note
draft: false
---
Trimmed means are averaging techniques that do not count (i.e. trim off) extreme values. The goal is to make mean calculations more robust to extreme values by not considering those values when calculating the mean.

[SciPy](https://docs.scipy.org/) offers a great methods of calculating trimmed means.

## Preliminaries


```python
# Import libraries
import pandas as pd
from scipy import stats
```

## Create DataFrame


```python
# Create dataframe with two extreme values
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy', 'Bob', 'Jack', 'Jill', 'Kelly', 'Mark', 'Kao', 'Dillon'], 
        'score': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 100]
       }
df = pd.DataFrame(data)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bob</td>
      <td>6</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Jack</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Jill</td>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Kelly</td>
      <td>9</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Mark</td>
      <td>10</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Kao</td>
      <td>100</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Dillon</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>



## Calculate Non-Trimmed Mean


```python
# Calculate non-trimmed mean
df['score'].mean()
```




    21.25



## Calculate Mean After Trimming Off Highest And Lowest


```python
# Trim off the 20% most extreme scores (lowest and highest)
stats.trim_mean(df['score'], proportiontocut=0.2)
```




    6.5



We can use `trimboth` to see which values are used to calculate the trimmed mean:


```python
# Trim off the 20% most extreme scores and view the non-trimmed values
stats.trimboth(df['score'], proportiontocut=0.2)
```




    array([ 3,  5,  4,  6,  7,  8,  9, 10])



## Calculate Mean After Trimming Only Highest Extremes

The `right` tail refers to the highest values in the array and `left` refers to the lowest values in the array.


```python
# Trim off the highest 20% of values and view trimmed mean
stats.trim1(df['score'], proportiontocut=0.2, tail='right').mean()
```




    5.5




```python
# Trim off the highest 20% of values and view non-trimmed values
stats.trim1(df['score'], proportiontocut=0.2, tail='right')
```




    array([ 1,  3,  2,  4,  5,  6,  7,  9,  8, 10])


