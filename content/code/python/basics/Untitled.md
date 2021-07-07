```python
# Load library
import pandas as pd

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'

# Load data as a dataframe
dataframe = pd.read_csv(url)

# Show first 5 rows
dataframe.head(5)
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
      <th>Name</th>
      <th>PClass</th>
      <th>Age</th>
      <th>Sex</th>
      <th>Survived</th>
      <th>SexCode</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Allen, Miss Elisabeth Walton</td>
      <td>1st</td>
      <td>29.00</td>
      <td>female</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Allison, Miss Helen Loraine</td>
      <td>1st</td>
      <td>2.00</td>
      <td>female</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Allison, Mr Hudson Joshua Creighton</td>
      <td>1st</td>
      <td>30.00</td>
      <td>male</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Allison, Mrs Hudson JC (Bessie Waldo Daniels)</td>
      <td>1st</td>
      <td>25.00</td>
      <td>female</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Allison, Master Hudson Trevor</td>
      <td>1st</td>
      <td>0.92</td>
      <td>male</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
