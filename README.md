# dependencyfixer
[![Build Status](https://travis-ci.com/avinashkarhana/dependency-fixer.svg?branch=master)](https://travis-ci.com/avinashkarhana/dependency-fixer)

A python dependency fixer and importable script function

This python script can work as a standalone python module installer and can be used to install modules in program runtime by importing the **fix** function from dependencyfixer into program.

>uses `pip._internal.cli.main.main()` function to install

## #why use dependencyfixer?
* Very useful in a case where you need to execute your own python script in a foreign environment(or maybe some other machine that doesn't have the pacakges that your script needs) without bothring to install each dependecy package one by one or creating a seprate requirements file for your script.

* Very useful in case of making your script platform independent, as if a functionality is provided by one package in one operating system and by another in other platform, so in this case you can import the desired pacakge to host machine by giving option of package installation and usage  as per host platform. (for an example if a functionality is needed by your script that is in windows specific package, now your script has to be run on macOS, so it needs a package that provides same functionality as of windows but on macOS, so in such case dependecyfixer can be used for setting option for pacakge to be installed)

So just install one package 'dependency-fixer' and the rest of the work is taken care by dependency handler that your script imported at the start

## #pros of using this package
* Standalone installing script
* Can install many modules at once
* gives report of how many script left to be installed(unsuccessful attempts)

### #install

`pip install dependency-fixer`

### #usage

> **❖Direct:** *(If are using source clone)
>> 	 run **dependencyfixer.py** and follow instruction

> **❖Importing to other python scripts**
>> * ***Import it like*** :
>> `from dependencyfixer import fix`
>>>* Function and Arguements:
>>> >* Function: `fix(dep,auto=True,instantkill=False)`
>>> >* Arguements: 
>>>> >* Mandatory: `dep` ( List of all packages to be installed or checked )
>>>> >* Optional: 
>>>>> >* ➤`instantkill` ( If set `True` then stops any futher execution of script in which function is used ) ***( False by default )***
>>>>> >* ➤`auto` ( If set `False` then asks for user's consent to install packages, if user refuses, then return result=0 )  ***( True by default )***
>>>>> >* ➤`verbose` ( If set `True` then prints details in console during installation and after installation ) ***( False by default )***
>>* ***Basic Example***:
```
from dependencyfixer import fix
## All importable package list that this script needs
dep=['pillow','jupyter']
result,leftdep=fix(dep)
if result==1:
    #Actual imports after all installation and package verification
    for lib in dep:
        globals()[lib] = importlib.import_module(lib)
elseif result==-1:
    .... handle left dependencies some other way as per list 'leftdep' or exit.....
else:
    .... No module installed Exit or Handle 'leftdep' as you like ..... 
 
#... anything in your script goes here and below
..
..
..
```
>>>>* This function returns 2 values :
>>>> > * leftdependencies : (list of packages that couldn't be installed)
>>>> > * result {1,0,-1} 
>>>>> | 1   | :   All modules installed
>>>>> | 0   | :   No module could be installed
>>>>> | -1 | :   Some modules could not be installed
