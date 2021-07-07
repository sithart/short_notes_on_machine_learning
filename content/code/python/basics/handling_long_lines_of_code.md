---
title: "Handling Long Lines Of Code"
author: "Chris Albon"
date: 2020-07-07T11:53:49-07:00
description: "How to handle long lines of code in Python."
type: technical_note
draft: false
aliases: [/python/basics/handling_long_lines_of_code/]
---
Often engineers and data scientists run into a situation where they have a very long line of code. This is both ugly and break's Pythonic best practices.

## Preliminaries


```python
import statistics
```

## Create Data


```python
ages_of_community_members = [39, 23, 55, 23, 53, 27, 34, 67, 32, 34, 56]
number_of_ages = [4, 4, 5, 6, 7, 8, 5, 7, 3, 2, 4]
```

## Create Long Line Of Code


```python
member_years_by_age = [first_list_element * second_list_element for first_list_element, second_list_element in zip(ages_of_community_members, number_of_ages)]
```

## Shorten Long Line

While you can use `\` to break up lines of code. A more simple and readable option is to take advantage of the fact that line breaks are ignored inside `[]`, `{}`, and `[]`. Then use comments to help the reader understand the line.


```python
# Create a variable with the count of members per age
member_years_by_age = [# multiply the first list's element by the second list's element
                           first_list_element * second_list_element 
                           # for the first list's elements and second list's element 
                           for first_list_element, second_list_element 
                           # for each element in a zip between the age of community members
                           in zip(ages_of_community_members, 
                                  # and the number of members by age
                                  number_of_ages)
                          ]
```
