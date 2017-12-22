---
title: "Test article"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "spf13-vim is a cross platform distribution of vim plugins and resources for Vim."
type: article
draft: false
image: https://chrisalbon.com/about/chris_albon/chris_albon_banner.jpg
---

Bessel's correction is the reason we use $n-1$ instead of $n$ in the calculations of sample variance and sample standard deviation.

Sample variance:

$$ s^2 = \frac {1}{n-1} \sum_{i=1}^n  \left(x_i - \overline{x} \right)^ 2 $$

When we calculate sample variance, we are attempting to estimate the population variance, an unknown value. To make this estimate, we estimate this unknown population variance from the mean of the squared deviations of samples from the overall sample mean. A negative sideffect of this estimation technique is that, because we are taking a sample, we are a more likely to observe observations with a smaller deviation because they are more common (e.g. they are the center of the distribution). The means that by definiton we will underestimate the population variance.

Friedrich Bessel figured out that by multiplying a biased (uncorrected) sample variance `$ s^2 $` we will $ s^2 $ be able to reduce that bias and thus be able to make an accurate estimate of the population variance and standard deviation. The end result of that multiplication is the unbiased sample variance.

<div>$$ s^2 = \frac {1}{n-1} \sum_{i=1}^n  \left(x_i - \overline{x} \right)^ 2 $$ </div>

![png](test.png)

## Preliminaries


```python
# Load libraries
from sklearn import preprocessing
import numpy as np
```

## Create Feature Data


```python
# Create feature
features = np.array([[-100.1, 3240.1], 
                     [-200.2, -234.1], 
                     [5000.5, 150.1], 
                     [6000.6, -125.1], 
                     [9000.9, -673.1]])
```

## Standardize Feature Data


```python
# Create scaler
scaler = preprocessing.StandardScaler()

# Transform the feature
features_standardized = scaler.fit_transform(features)
```

## Show Standardized Features


```python
# Show feature
features_standardized
```




    array([[-1.12541308,  1.96429418],
           [-1.15329466, -0.50068741],
           [ 0.29529406, -0.22809346],
           [ 0.57385917, -0.42335076],
           [ 1.40955451, -0.81216255]])



## Show Standardized Features Summary Statistics


```python
# Print mean and standard deviation
print('Mean:', round(features_standardized[:,0].mean()))
print('Standard deviation:', features_standardized[:,0].std())
```

    Mean: 0.0
    Standard deviation: 1.0