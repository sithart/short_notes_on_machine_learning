---
title: "List All Files Of Certain Type In A Directory"
author: "Chris Albon"
date: 2018-11-20T11:53:49-07:00
description: "List all files of a certain type in a directory using Python"
type: technical_note
draft: false
---
## Preliminaries


```python
import os
```

## List All .ipynb Files In Directory


```python
[x for x in os.listdir() if x.endswith(".ipynb")]
```




    ['create_a_new_file_and_the_write_to_it.ipynb',
     'unpacking_a_tuple.ipynb',
     'unpacking_function_arguments.ipynb',
     'convert_html_symbols_to_strings.ipynb',
     'arithmetic_basics.ipynb',
     'cleaning_text.ipynb',
     'applying_functions_to_list_items.ipynb',
     'while_statements.ipynb',
     'continue_and_break_loops.ipynb',
     'queues_and_stacks.ipynb',
     'numpy_array_basics.ipynb',
     'schedule_run_in_the_future.ipynb',
     'Untitled.ipynb',
     'repr_vs_str.ipynb',
     'using_named_tuples_to_store_data.ipynb',
     'hard_wrapping_text.ipynb',
     'string_formatting.ipynb',
     'functions_vs_generators.ipynb',
     'nesting_lists.ipynb',
     'sort_a_list_of_strings_by_length.ipynb',
     'filter_items_in_list_with_filter.ipynb',
     'swapping_variable_values.ipynb',
     'iterating_over_dictionary_keys.ipynb',
     'iterate_ifelse_over_list.ipynb',
     'recursive_functions.ipynb',
     'for_loops.ipynb',
     'use_command_line_arguments_in_a_function.ipynb',
     'logical_operations.ipynb',
     'strings_to_datetime.ipynb',
     'flatten_list_of_lists.ipynb',
     'nested_for_loops_using_list_comprehension.ipynb',
     'Untitled1.ipynb',
     'function_basics.ipynb',
     'find_the_max_value_in_a_dictionary.ipynb',
     'any_all_max_min_sum.ipynb',
     'display_json.ipynb',
     'exiting_a_loop.ipynb',
     'date_and_time_basics.ipynb',
     'add_padding_around_string.ipynb',
     'iterate_over_multiple_lists_simultaneously.ipynb',
     'breaking_up_string_variables.ipynb',
     'mocking_functions.ipynb',
     'compare_two_dictionaries.ipynb',
     'chain_together_lists.ipynb',
     'function_annotation_examples.ipynb',
     'brute_force_d20_simulator.ipynb',
     'string_operations.ipynb',
     'data_structure_basics.ipynb',
     'string_indexing.ipynb',
     'math_operations.ipynb',
     'numpy_array_basic_operations.ipynb',
     'ifelse_on_any_or_all_elements.ipynb',
     'sort_a_list_by_last_name.ipynb',
     'apply_operations_over_items_in_lists.ipynb',
     'all_combinations_of_a_list_of_objects.ipynb',
     'try_except_finally.ipynb',
     'cartesian_product.ipynb',
     'concurrent_processing.ipynb',
     'display_scientific_notation_as_floats.ipynb',
     'lambda_functions.ipynb',
     'assignment_operators.ipynb',
     'select_random_element_from_list.ipynb',
     'generating_random_numbers_with_numpy.ipynb',
     'if_and_if_else_statements.ipynb',
     'how_to_use_default_dicts.ipynb',
     'indexing_and_slicing_numpy_arrays.ipynb',
     'formatting_numbers.ipynb',
     'priority_queues.ipynb',
     'partial_function_applications.ipynb',
     'store_api_credentials_for_open_source_projects.ipynb',
     'dictionary_basics.ipynb',
     'numpy_indexing_and_slicing.ipynb',
     'create_a_temporary_file.ipynb',
     'parallel_processing.ipynb',
     'generator_expressions.ipynb',
     'looping_over_two_lists.ipynb',
     'set_the_color_of_a_matplotlib.ipynb']


