# python

## H2 Selector.py
Simple script to allow the quick navigation between directories on a unix system. The python script processes a file and gives you a set of menu options for each line. 
The example below shows quick jump to navigation, but there are other uses too.

Setup these aliases (for tcsh):

```
alias addir "echo $cwd >> ~/etc/possible_dirs; sort < ~/etc/possible_dirs > ~/etc/possible_dirs2; mv ~/etc/possible_dirs2 ~/etc/possible_dirs;"
alias wcd cd `selector.py ~/etc/possible_dirs`"
```

Example of usage:

```
System User@Collie:Notepad++{60} pwd
/cygdrive/c/Program Files/Notepad++
System User@Collie:Notepad++{61} addir
mv: overwrite `/cygdrive/c/etc/possible_dirs'? y
System User@Collie:Notepad++{62} wcd

0:      /cygdrive/c/Program Files/Notepad++
1:      /cygdrive/c/akm

Entering /cygdrive/c/akm
System User@Collie:akm{63} pwd
/cygdrive/c/akm
```