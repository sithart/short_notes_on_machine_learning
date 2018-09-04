---
title: "List The Contents Of A Directory"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to list the contents of a directory in a system using the Linux command line."
type: technical_note
draft: false
---

`ls` is one of the most useful commands when using the Linux command line. `ls` lists the contents of the directory.

## List Contents Of Directory

{{< highlight markdown >}}
ls
{{< /highlight >}}
```
bin  compiler_compat  conda-meta  doc  etc  include  lib  libexec  LICENSE.txt  mkspecs  phrasebooks  pkgs  plugins  qml  share  ssl  translations  var  x86_64-conda_cos6-linux-gnu
```

## List Contents Of Directory In Detail

Note that the first column contains the file's permission setting, which are structured as:

- Character 1: Type Of File (`d` means directory)
- Characters 2-4: Access Rights For File's Owner
- Characters 5-7: Access Rights For File's Group
- Characters 7-9: Access Rights For Everyone

{{< highlight markdown >}}
ls -l
{{< /highlight >}}
```
total 188
drwxrwxr-x   2 chris chris 12288 Oct 11  2017 bin
drwxrwxr-x   2 chris chris  4096 Oct 11  2017 compiler_compat
drwxrwxr-x   2 chris chris 20480 Oct 11  2017 conda-meta
drwxrwxr-x   3 chris chris  4096 Oct 11  2017 doc
drwxrwxr-x   7 chris chris  4096 Oct 11  2017 etc
drwxrwxr-x  31 chris chris 12288 Oct 11  2017 include
drwxrwxr-x  22 chris chris 36864 Oct 11  2017 lib
drwxrwxr-x   4 chris chris  4096 Oct 11  2017 libexec
-rw-r--r--   1 chris chris  5350 Sep 24  2017 LICENSE.txt
drwxrwxr-x  97 chris chris  4096 Oct 11  2017 mkspecs
drwxrwxr-x   2 chris chris  4096 Oct 11  2017 phrasebooks
drwxrwxr-x 244 chris chris 36864 Oct 11  2017 pkgs
drwxrwxr-x  16 chris chris  4096 Oct 11  2017 plugins
drwxrwxr-x  14 chris chris  4096 Oct 11  2017 qml
drwxrwxr-x  29 chris chris  4096 Oct 11  2017 share
drwxrwxr-x   4 chris chris  4096 Oct 11  2017 ssl
drwxrwxr-x   2 chris chris 12288 Oct 11  2017 translations
drwxrwxr-x   3 chris chris  4096 Oct 11  2017 var
drwxrwxr-x   3 chris chris  4096 Oct 11  2017 x86_64-conda_cos6-linux-gnu
```

## List All Contents Of Directory (Including Hidden Files) 

{{< highlight markdown >}}
ls -a
{{< /highlight >}}
```
.   bin              conda-meta  etc      lib      LICENSE.txt  phrasebooks  plugins  share  translations  x86_64-conda_cos6-linux-gnu
..  compiler_compat  doc         include  libexec  mkspecs      pkgs         qml      ssl    var
```

## View Contents Of Directory With Human Readable File/Folder Sizes

{{< highlight markdown >}}
ls -lh
{{< /highlight >}}
```
total 188K
drwxrwxr-x   2 chris chris  12K Oct 11  2017 bin
drwxrwxr-x   2 chris chris 4.0K Oct 11  2017 compiler_compat
drwxrwxr-x   2 chris chris  20K Oct 11  2017 conda-meta
drwxrwxr-x   3 chris chris 4.0K Oct 11  2017 doc
drwxrwxr-x   7 chris chris 4.0K Oct 11  2017 etc
drwxrwxr-x  31 chris chris  12K Oct 11  2017 include
drwxrwxr-x  22 chris chris  36K Oct 11  2017 lib
drwxrwxr-x   4 chris chris 4.0K Oct 11  2017 libexec
-rw-r--r--   1 chris chris 5.3K Sep 24  2017 LICENSE.txt
drwxrwxr-x  97 chris chris 4.0K Oct 11  2017 mkspecs
drwxrwxr-x   2 chris chris 4.0K Oct 11  2017 phrasebooks
drwxrwxr-x 244 chris chris  36K Oct 11  2017 pkgs
drwxrwxr-x  16 chris chris 4.0K Oct 11  2017 plugins
drwxrwxr-x  14 chris chris 4.0K Oct 11  2017 qml
drwxrwxr-x  29 chris chris 4.0K Oct 11  2017 share
drwxrwxr-x   4 chris chris 4.0K Oct 11  2017 ssl
drwxrwxr-x   2 chris chris  12K Oct 11  2017 translations
drwxrwxr-x   3 chris chris 4.0K Oct 11  2017 var
drwxrwxr-x   3 chris chris 4.0K Oct 11  2017 x86_64-conda_cos6-linux-gnu
```

## View Contents Of Directory Sorted By File Size

{{< highlight markdown >}}
ls -lS
{{< /highlight >}}
```
total 188
drwxrwxr-x  22 chris chris 36864 Oct 11  2017 lib
drwxrwxr-x 244 chris chris 36864 Oct 11  2017 pkgs
drwxrwxr-x   2 chris chris 20480 Oct 11  2017 conda-meta
drwxrwxr-x   2 chris chris 12288 Oct 11  2017 bin
drwxrwxr-x  31 chris chris 12288 Oct 11  2017 include
drwxrwxr-x   2 chris chris 12288 Oct 11  2017 translations
-rw-r--r--   1 chris chris  5350 Sep 24  2017 LICENSE.txt
drwxrwxr-x   2 chris chris  4096 Oct 11  2017 compiler_compat
drwxrwxr-x   3 chris chris  4096 Oct 11  2017 doc
drwxrwxr-x   7 chris chris  4096 Oct 11  2017 etc
drwxrwxr-x   4 chris chris  4096 Oct 11  2017 libexec
drwxrwxr-x  97 chris chris  4096 Oct 11  2017 mkspecs
drwxrwxr-x   2 chris chris  4096 Oct 11  2017 phrasebooks
drwxrwxr-x  16 chris chris  4096 Oct 11  2017 plugins
drwxrwxr-x  14 chris chris  4096 Oct 11  2017 qml
drwxrwxr-x  29 chris chris  4096 Oct 11  2017 share
drwxrwxr-x   4 chris chris  4096 Oct 11  2017 ssl
drwxrwxr-x   3 chris chris  4096 Oct 11  2017 var
drwxrwxr-x   3 chris chris  4096 Oct 11  2017 x86_64-conda_cos6-linux-gnu
```

## View Contents Of Directory Sorted By Last Modified

{{< highlight markdown >}}
ls -lt
{{< /highlight >}}
```
total 188
drwxrwxr-x   2 chris chris 20480 Oct 11  2017 conda-meta
drwxrwxr-x  22 chris chris 36864 Oct 11  2017 lib
drwxrwxr-x 244 chris chris 36864 Oct 11  2017 pkgs
drwxrwxr-x   2 chris chris 12288 Oct 11  2017 bin
drwxrwxr-x   7 chris chris  4096 Oct 11  2017 etc
drwxrwxr-x  29 chris chris  4096 Oct 11  2017 share
drwxrwxr-x  31 chris chris 12288 Oct 11  2017 include
drwxrwxr-x  16 chris chris  4096 Oct 11  2017 plugins
drwxrwxr-x  97 chris chris  4096 Oct 11  2017 mkspecs
drwxrwxr-x  14 chris chris  4096 Oct 11  2017 qml
drwxrwxr-x   2 chris chris 12288 Oct 11  2017 translations
drwxrwxr-x   2 chris chris  4096 Oct 11  2017 phrasebooks
drwxrwxr-x   4 chris chris  4096 Oct 11  2017 libexec
drwxrwxr-x   3 chris chris  4096 Oct 11  2017 doc
drwxrwxr-x   3 chris chris  4096 Oct 11  2017 var
drwxrwxr-x   4 chris chris  4096 Oct 11  2017 ssl
drwxrwxr-x   3 chris chris  4096 Oct 11  2017 x86_64-conda_cos6-linux-gnu
drwxrwxr-x   2 chris chris  4096 Oct 11  2017 compiler_compat
-rw-r--r--   1 chris chris  5350 Sep 24  2017 LICENSE.txt
```

## View Contents In Reverse Order

{{< highlight markdown >}}
ls -ltr
{{< /highlight >}}
```
total 188
-rw-r--r--   1 chris chris  5350 Sep 24  2017 LICENSE.txt
drwxrwxr-x   2 chris chris  4096 Oct 11  2017 compiler_compat
drwxrwxr-x   3 chris chris  4096 Oct 11  2017 x86_64-conda_cos6-linux-gnu
drwxrwxr-x   4 chris chris  4096 Oct 11  2017 ssl
drwxrwxr-x   3 chris chris  4096 Oct 11  2017 var
drwxrwxr-x   3 chris chris  4096 Oct 11  2017 doc
drwxrwxr-x   4 chris chris  4096 Oct 11  2017 libexec
drwxrwxr-x   2 chris chris  4096 Oct 11  2017 phrasebooks
drwxrwxr-x   2 chris chris 12288 Oct 11  2017 translations
drwxrwxr-x  14 chris chris  4096 Oct 11  2017 qml
drwxrwxr-x  97 chris chris  4096 Oct 11  2017 mkspecs
drwxrwxr-x  16 chris chris  4096 Oct 11  2017 plugins
drwxrwxr-x  31 chris chris 12288 Oct 11  2017 include
drwxrwxr-x  29 chris chris  4096 Oct 11  2017 share
drwxrwxr-x   7 chris chris  4096 Oct 11  2017 etc
drwxrwxr-x   2 chris chris 12288 Oct 11  2017 bin
drwxrwxr-x 244 chris chris 36864 Oct 11  2017 pkgs
drwxrwxr-x  22 chris chris 36864 Oct 11  2017 lib
drwxrwxr-x   2 chris chris 20480 Oct 11  2017 conda-meta
```