---
title: "Ignore Files While Building"
date: 2020-07-22T00:00:00-07:00
description: "Use .dockerignore for Dockerfiles."
type: technical_note
draft: false
aliases: [/docker/dockerfiles/ignore_files_while_building/]
---

## Create File Called .dockerignore
{{< highlight bash >}}
touch .dockerignore
{{< /highlight >}}

## Add File Contents
{{< highlight bash >}}
# Ignore any file called .git
.git

# Ignore any file with a .ipynb extension
*.ipynb

# Except don't ignore important_analysis.ipynb
!important_analysis.ipynb

# Ignore every file and folder in secret_project/ directory
secret_project/
{{< /highlight >}}

Any Docker build in the directory with the `.dockerignore` file will follow rules declared above.