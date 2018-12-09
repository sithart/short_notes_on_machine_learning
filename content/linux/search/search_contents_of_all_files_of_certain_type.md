---
title: "Search Contents Of All Files Of Certain Type"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to search the contents of all files of a certain type using the Linux command line."
type: technical_note
draft: false
---

Note: In this tutorial we do not generate the files we will search but rather search the contents of this site's directory structure.

## Recursively Search All Markdown For The Word "berry"

- `grep` search command
- `-n` to display line number of matched pattern
- `-i` to make search case insensitive
- `-r` to search recursively
- `--color` to color the matches so they stand out
- `--include='*.md'` to search only in files ending in `.md`
- `'berry'` to search for the pattern "berry"
- `./` search in the current directory (and all child directories because we set command to search recursively)

{{< highlight markdown >}}
grep -n -i -r --color --include='*.md' 'berry' ./
{{< /highlight >}}
```
./content/linux/text/join_and_sort_text.md:15:echo "Strawberry" >> fruit_3.txt; echo "Blueberry" >> fruit_3.txt; echo "Mango" >> fruit_3.txt
./content/linux/text/join_and_sort_text.md:32:Blueberry
./content/linux/text/join_and_sort_text.md:37:Strawberry
./content/articles/puzzle_of_rebel_mobilization.md:22:Capacity plays a central role in political behavior (Katzenstein 1978; Migdal 1988; Ikenberry 1988). Weber’s classic definition of the state as a “human community that (successfully) claims the monopoly of the legitimate use of force within a given territory,” includes a government’s capacity to defeat or deter challengers as the principle prerequisite of statehood. Recently there has been renewed interest in the role of state capacity in civil wars, with a special
issue of the Journal of Peace Research dedicated to the topic (Sobek 2010). More broadly however, the capacity of all political actors, not just states, plays a central role in explaining civil war processes.
./content/articles/puzzle_of_rebel_mobilization.md:85:- Ikenberry, G. John. 1988. Reasons of State: Oil Politics and the Capacities of American Government. Cornell Univ Pr.
```