---
title: "Create Symbolic Links"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to create symbolic links using the Linux command line."
type: technical_note
draft: false
---

In Linux, we can use `ln` to create a link between files. A common use case is shown below, where we have a symbolic link from the current configuration file `config_settings_v293.txt` and a link `config_setting.txt`. In our code, we can refer `config_settings.txt` as if we were refering to `config_settings_v293.txt`. However, when a new version of the configuration settings is released, `config_settings_v294.txt`, we can swap the symbolic link from `config_settings_v293.txt` to `config_settings_v294.txt` without changing all the code that references `config_settings.txt`.

Note that `-nsf` is a common set of options for `ln`: 

- `-s` make symbolic links instead of hard links
- `-f` if target file delete it so we can replace it with our new link
- `-n` if the target file or directory is a link, don't follow the link

## Create File

{{< highlight markdown >}}
echo 'Configuration settings version 293' > config_settings_v293.txt
{{< /highlight >}}

## Create Symbolic Link To File

{{< highlight markdown >}}
ln -nsf config_settings_v293.txt config_settings.txt
{{< /highlight >}}

## View Symbolic Link

{{< highlight markdown >}}
cat config_settings.txt
{{< /highlight >}}
```
Configuration settings version 293
```

## Create New File

{{< highlight markdown >}}
echo 'Configuration settings version 294' > config_settings_v294.txt
{{< /highlight >}}

## Create Symbolic Link To New File

{{< highlight markdown >}}
ln -nsf config_settings_v294.txt config_settings.txt
{{< /highlight >}}

## View Symbolic Link

{{< highlight markdown >}}
cat config_settings.txt
{{< /highlight >}}
```
Configuration settings version 294
```