---
title: "Get Help With A Command"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to get help with a command using the Linux command line."
type: technical_note
draft: false
---

The `--help` argument is a common choice for quickly learning about a command. Particularly useful, `--help` shows the arguments for that particular command so we don't have to look them up online.

Another option is the `whatis` command, which prints a one-line description of the command.

## Quickly Describe A Command
{{< highlight markdown >}}
whatis mkdir
{{< /highlight >}}
```
mkdir (1)            - make directories
mkdir (2)            - create a directory
```

Note that in this case there are two mkdir commands with slightly different descriptions, but you can ignore that.

## Get Help With A Command

In this example, we get help for the command `mkdir` (make directory).

{{< highlight markdown >}}
mkdir --help
{{< /highlight >}}
```
Usage: mkdir [OPTION]... DIRECTORY...
Create the DIRECTORY(ies), if they do not already exist.

Mandatory arguments to long options are mandatory for short options too.
  -m, --mode=MODE   set file mode (as in chmod), not a=rwx - umask
  -p, --parents     no error if existing, make parent directories as needed
  -v, --verbose     print a message for each created directory
  -Z                   set SELinux security context of each created directory
                         to the default type
      --context[=CTX]  like -Z, or if CTX is specified then set the SELinux
                         or SMACK security context to CTX
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/mkdir>
or available locally via: info '(coreutils) mkdir invocation'
```