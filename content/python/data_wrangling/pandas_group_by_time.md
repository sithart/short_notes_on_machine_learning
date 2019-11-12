---
title: "Group A Time Series With pandas"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Group a time series with pandas."
type: technical_note
draft: false
---
### Import required modules


```python
import pandas as pd
import numpy as np
```

### Create a dataframe


```python
df = pd.DataFrame()

df['german_army'] = np.random.randint(low=20000, high=30000, size=100)
df['allied_army'] = np.random.randint(low=20000, high=40000, size=100)
df.index = pd.date_range('1/1/2014', periods=100, freq='H')

df.head()
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
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-01-01 00:00:00</th>
      <td>21413</td>
      <td>37604</td>
    </tr>
    <tr>
      <th>2014-01-01 01:00:00</th>
      <td>25913</td>
      <td>21144</td>
    </tr>
    <tr>
      <th>2014-01-01 02:00:00</th>
      <td>22418</td>
      <td>34201</td>
    </tr>
    <tr>
      <th>2014-01-01 03:00:00</th>
      <td>20704</td>
      <td>37313</td>
    </tr>
    <tr>
      <th>2014-01-01 04:00:00</th>
      <td>27859</td>
      <td>24467</td>
    </tr>
  </tbody>
</table>
</div>



### Truncate the dataframe


```python
df.truncate(before='1/2/2014', after='1/3/2014')
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
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-01-02 00:00:00</th>
      <td>28783</td>
      <td>22407</td>
    </tr>
    <tr>
      <th>2014-01-02 01:00:00</th>
      <td>27530</td>
      <td>23106</td>
    </tr>
    <tr>
      <th>2014-01-02 02:00:00</th>
      <td>27351</td>
      <td>36703</td>
    </tr>
    <tr>
      <th>2014-01-02 03:00:00</th>
      <td>28062</td>
      <td>39590</td>
    </tr>
    <tr>
      <th>2014-01-02 04:00:00</th>
      <td>27691</td>
      <td>35282</td>
    </tr>
    <tr>
      <th>2014-01-02 05:00:00</th>
      <td>22498</td>
      <td>22229</td>
    </tr>
    <tr>
      <th>2014-01-02 06:00:00</th>
      <td>26470</td>
      <td>34484</td>
    </tr>
    <tr>
      <th>2014-01-02 07:00:00</th>
      <td>22123</td>
      <td>38835</td>
    </tr>
    <tr>
      <th>2014-01-02 08:00:00</th>
      <td>20056</td>
      <td>30520</td>
    </tr>
    <tr>
      <th>2014-01-02 09:00:00</th>
      <td>22560</td>
      <td>28191</td>
    </tr>
    <tr>
      <th>2014-01-02 10:00:00</th>
      <td>20335</td>
      <td>26722</td>
    </tr>
    <tr>
      <th>2014-01-02 11:00:00</th>
      <td>28207</td>
      <td>28571</td>
    </tr>
    <tr>
      <th>2014-01-02 12:00:00</th>
      <td>21135</td>
      <td>31793</td>
    </tr>
    <tr>
      <th>2014-01-02 13:00:00</th>
      <td>25570</td>
      <td>36780</td>
    </tr>
    <tr>
      <th>2014-01-02 14:00:00</th>
      <td>26743</td>
      <td>39214</td>
    </tr>
    <tr>
      <th>2014-01-02 15:00:00</th>
      <td>28496</td>
      <td>35278</td>
    </tr>
    <tr>
      <th>2014-01-02 16:00:00</th>
      <td>26156</td>
      <td>23902</td>
    </tr>
    <tr>
      <th>2014-01-02 17:00:00</th>
      <td>21795</td>
      <td>39038</td>
    </tr>
    <tr>
      <th>2014-01-02 18:00:00</th>
      <td>25840</td>
      <td>34204</td>
    </tr>
    <tr>
      <th>2014-01-02 19:00:00</th>
      <td>22582</td>
      <td>26021</td>
    </tr>
    <tr>
      <th>2014-01-02 20:00:00</th>
      <td>26145</td>
      <td>21035</td>
    </tr>
    <tr>
      <th>2014-01-02 21:00:00</th>
      <td>25084</td>
      <td>21895</td>
    </tr>
    <tr>
      <th>2014-01-02 22:00:00</th>
      <td>29835</td>
      <td>27199</td>
    </tr>
    <tr>
      <th>2014-01-02 23:00:00</th>
      <td>29916</td>
      <td>26703</td>
    </tr>
    <tr>
      <th>2014-01-03 00:00:00</th>
      <td>23252</td>
      <td>23883</td>
    </tr>
  </tbody>
</table>
</div>



### Set the dataframe's index


```python
df.index = df.index + pd.DateOffset(months=4, days=5)
```

### View the dataframe


```python
df.head()
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
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-06 00:00:00</th>
      <td>21413</td>
      <td>37604</td>
    </tr>
    <tr>
      <th>2014-05-06 01:00:00</th>
      <td>25913</td>
      <td>21144</td>
    </tr>
    <tr>
      <th>2014-05-06 02:00:00</th>
      <td>22418</td>
      <td>34201</td>
    </tr>
    <tr>
      <th>2014-05-06 03:00:00</th>
      <td>20704</td>
      <td>37313</td>
    </tr>
    <tr>
      <th>2014-05-06 04:00:00</th>
      <td>27859</td>
      <td>24467</td>
    </tr>
  </tbody>
</table>
</div>



### Lead a variable 1 hour


```python
df.shift(1).head()
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
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-06 00:00:00</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2014-05-06 01:00:00</th>
      <td>21413.0</td>
      <td>37604.0</td>
    </tr>
    <tr>
      <th>2014-05-06 02:00:00</th>
      <td>25913.0</td>
      <td>21144.0</td>
    </tr>
    <tr>
      <th>2014-05-06 03:00:00</th>
      <td>22418.0</td>
      <td>34201.0</td>
    </tr>
    <tr>
      <th>2014-05-06 04:00:00</th>
      <td>20704.0</td>
      <td>37313.0</td>
    </tr>
  </tbody>
</table>
</div>



### Lag a variable 1 hour


```python
df.shift(-1).tail()
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
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-09 23:00:00</th>
      <td>26615.0</td>
      <td>35368.0</td>
    </tr>
    <tr>
      <th>2014-05-10 00:00:00</th>
      <td>20410.0</td>
      <td>21218.0</td>
    </tr>
    <tr>
      <th>2014-05-10 01:00:00</th>
      <td>24404.0</td>
      <td>29038.0</td>
    </tr>
    <tr>
      <th>2014-05-10 02:00:00</th>
      <td>21190.0</td>
      <td>31730.0</td>
    </tr>
    <tr>
      <th>2014-05-10 03:00:00</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### Aggregate into days by summing up the value of each hourly observation


```python
df.resample('D').sum()
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
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-06</th>
      <td>596133</td>
      <td>715399</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>610963</td>
      <td>729702</td>
    </tr>
    <tr>
      <th>2014-05-08</th>
      <td>604796</td>
      <td>717520</td>
    </tr>
    <tr>
      <th>2014-05-09</th>
      <td>618359</td>
      <td>701690</td>
    </tr>
    <tr>
      <th>2014-05-10</th>
      <td>92619</td>
      <td>117354</td>
    </tr>
  </tbody>
</table>
</div>



### Aggregate into days by averaging up the value of each hourly observation


```python
df.resample('D').mean()
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
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-06</th>
      <td>24838.875000</td>
      <td>29808.291667</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>25456.791667</td>
      <td>30404.250000</td>
    </tr>
    <tr>
      <th>2014-05-08</th>
      <td>25199.833333</td>
      <td>29896.666667</td>
    </tr>
    <tr>
      <th>2014-05-09</th>
      <td>25764.958333</td>
      <td>29237.083333</td>
    </tr>
    <tr>
      <th>2014-05-10</th>
      <td>23154.750000</td>
      <td>29338.500000</td>
    </tr>
  </tbody>
</table>
</div>



### Aggregate into days by taking the min value up the value of each hourly observation


```python
df.resample('D').min()
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
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-06</th>
      <td>20331</td>
      <td>21144</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>20056</td>
      <td>21035</td>
    </tr>
    <tr>
      <th>2014-05-08</th>
      <td>20475</td>
      <td>21209</td>
    </tr>
    <tr>
      <th>2014-05-09</th>
      <td>21071</td>
      <td>20475</td>
    </tr>
    <tr>
      <th>2014-05-10</th>
      <td>20410</td>
      <td>21218</td>
    </tr>
  </tbody>
</table>
</div>



### Aggregate into days by taking the median value of each day's worth of hourly observation


```python
df.resample('D').median()
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
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-06</th>
      <td>24747.5</td>
      <td>28327.5</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>26150.5</td>
      <td>29545.5</td>
    </tr>
    <tr>
      <th>2014-05-08</th>
      <td>25035.5</td>
      <td>29677.0</td>
    </tr>
    <tr>
      <th>2014-05-09</th>
      <td>25694.5</td>
      <td>28969.0</td>
    </tr>
    <tr>
      <th>2014-05-10</th>
      <td>22797.0</td>
      <td>30384.0</td>
    </tr>
  </tbody>
</table>
</div>



### Aggregate into days by taking the first value of each day's worth of hourly observation


```python
df.resample('D').first()
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
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-06</th>
      <td>21413</td>
      <td>37604</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>28783</td>
      <td>22407</td>
    </tr>
    <tr>
      <th>2014-05-08</th>
      <td>23252</td>
      <td>23883</td>
    </tr>
    <tr>
      <th>2014-05-09</th>
      <td>25644</td>
      <td>24035</td>
    </tr>
    <tr>
      <th>2014-05-10</th>
      <td>26615</td>
      <td>35368</td>
    </tr>
  </tbody>
</table>
</div>



### Aggregate into days by taking the last value of each day's worth of hourly observation


```python
df.resample('D').last()
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
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-06</th>
      <td>22406</td>
      <td>38633</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>29916</td>
      <td>26703</td>
    </tr>
    <tr>
      <th>2014-05-08</th>
      <td>24882</td>
      <td>29425</td>
    </tr>
    <tr>
      <th>2014-05-09</th>
      <td>28307</td>
      <td>36548</td>
    </tr>
    <tr>
      <th>2014-05-10</th>
      <td>21190</td>
      <td>31730</td>
    </tr>
  </tbody>
</table>
</div>



### Aggregate into days by taking the first, last, highest, and lowest value of each day's worth of hourly observation


```python
df.resample('D').ohlc()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="4" halign="left">german_army</th>
      <th colspan="4" halign="left">allied_army</th>
    </tr>
    <tr>
      <th></th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-06</th>
      <td>21413</td>
      <td>29377</td>
      <td>20331</td>
      <td>22406</td>
      <td>37604</td>
      <td>39906</td>
      <td>21144</td>
      <td>38633</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>28783</td>
      <td>29916</td>
      <td>20056</td>
      <td>29916</td>
      <td>22407</td>
      <td>39590</td>
      <td>21035</td>
      <td>26703</td>
    </tr>
    <tr>
      <th>2014-05-08</th>
      <td>23252</td>
      <td>29591</td>
      <td>20475</td>
      <td>24882</td>
      <td>23883</td>
      <td>37465</td>
      <td>21209</td>
      <td>29425</td>
    </tr>
    <tr>
      <th>2014-05-09</th>
      <td>25644</td>
      <td>29924</td>
      <td>21071</td>
      <td>28307</td>
      <td>24035</td>
      <td>39892</td>
      <td>20475</td>
      <td>36548</td>
    </tr>
    <tr>
      <th>2014-05-10</th>
      <td>26615</td>
      <td>26615</td>
      <td>20410</td>
      <td>21190</td>
      <td>35368</td>
      <td>35368</td>
      <td>21218</td>
      <td>31730</td>
    </tr>
  </tbody>
</table>
</div>


