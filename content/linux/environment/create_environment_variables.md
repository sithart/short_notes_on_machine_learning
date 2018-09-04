---
title: "Create Environment Variable"
author: "Chris Albon"
date: 2018-06-17T00:00:00-07:00
description: "How to make environment variables in the Linux command line."
type: technical_note
draft: false
---

The best way to store login credentials and API tokens/secrets is by creating environment variables for them. This means they are variables in the Linux system and thus not present in any code that is shared on GitHub.

There are many ways to create environment variables, but my personal preference is to add them to the `.bashrc` file in our `home` directory. `.bashrc` does a lot of things, but it is a standard place to put customizations to our system -- for example, custom variables.

## View The End Of `.bashrc` File

{{< highlight markdown >}}
tail ~/.bashrc
{{< /highlight >}}
```
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# added by Anaconda3 installer
export PATH="/home/chris/anaconda3/bin:$PATH"

alias lcl='ls -l'
```

## Append Environment Variable To End Of `.bashrc`
{{< highlight markdown >}}
echo 'APIKEY="cH4ris_1s_c000l"' >> ~/.bashrc
{{< /highlight >}}

## View The End Of `.bashrc` File

{{< highlight markdown >}}
tail ~/.bashrc
{{< /highlight >}}
```
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# added by Anaconda3 installer
export PATH="/home/chris/anaconda3/bin:$PATH"

alias lcl='ls -l'
APIKEY="cH4ris_1s_c000l"
```

## Reload `.bashrc`

{{< highlight markdown >}}
source ~/.bashrc
{{< /highlight >}}

## View New Environment Variable

{{< highlight markdown >}}
echo $APIKEY
{{< /highlight >}}
```
cH4ris_1s_c000l
```