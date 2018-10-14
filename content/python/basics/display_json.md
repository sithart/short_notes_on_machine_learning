---
title: "Display JSON"
author: "Chris Albon"
date: 2017-12-20T11:53:49-07:00
description: "Display JSON using Python."
type: technical_note
draft: false
---
## Preliminary


```python
# Import library
import json
```

## Create String With JSON Data


```python
_string = '{"data": {"title": "Machine Learning With Python Cookbook","author": {"name": "Chris Albon","biography": {"eduation": {"phd": "UC Davis","masters": "UC Davis","undergraduate": "Univ. Of Miami","acronym": "CRA","full name": "Christopher Albon","favorites": {"food": "Steak","sport": ["baseball", "basketball"]},"dissertation": "Health Systems During And After Civil WarS"}}}}}'
```

## Convert String To JSON


```python
json_data = json.loads(_string)
```

## Display JSON


```python
print(json.dumps(json_data, indent=2))
```

    {
      "data": {
        "title": "Machine Learning With Python Cookbook",
        "author": {
          "name": "Chris Albon",
          "biography": {
            "eduation": {
              "phd": "UC Davis",
              "masters": "UC Davis",
              "undergraduate": "Univ. Of Miami",
              "acronym": "CRA",
              "full name": "Christopher Albon",
              "favorites": {
                "food": "Steak",
                "sport": [
                  "baseball",
                  "basketball"
                ]
              },
              "dissertation": "Health Systems During And After Civil WarS"
            }
          }
        }
      }
    }

