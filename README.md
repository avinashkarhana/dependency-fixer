# dependencyhandler

A python dependency Handler and importable script function

  

This python script can work as a standalone python module installer and can be used to install modules in program runtime by importing the **dependencyhandler** function into program.

>uses `pip._internal.cli.main.main()` function to install

  

## #pros of using this package

  

* Standalone installing script

* Can install many modules at once

* gives report of how many script left to be installed(unsuccessful attempts)

  

### #install

`pip install dependency-handler`

  

### #usage

> **Direct:**
>> 	 run **dependencyhandler.py** and follow instruction

>**Importing to other python scripts**
>>  Use below command to import
>>* `from dependency-handler import dependencyhandler`
>>>* Function (dependencyhandler) takes a list consisting of all module names that are to be installed, as a arguement
>>>* ***Example***:
`dep=['pillow','jupyter']
result,leftdep=dependencyhandler(dep)`
>>>* This function returns 2 values :
>>> > * leftdependencies : (list of unsuccessfull modules)
>>> > * result {1,0,-1} 
>>>> | 1   | :   All modules installed
>>>> | 0   | :   No modules installed
>>>> | -1 | :   Some modules can not be installed

**If not installed by pip or using repo clone, to import in other python scripts be sure 'dependencyhandler.py' script is in same folder as calling script or specify appropriate path while importing