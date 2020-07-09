### dependencyhandler
A python dependency Handler and importable script function

This python script can work as a standalone python module installer and can be used to install modules in program runtime by importing the "dependencyhandler" function into program.
*uses pip._internal.cli.main.main() function to install

#pros of using this script

    *Standalone installing script
  
    *Can install many modules at once
  
    *gives report of how many script left to be installed(unsuccessful attempts)

###install 
      ```
      pip install dependency-handler
      ```

###usage

  ~ Direct
  
      : run and follow instruction
  
  
  ~ Importing to other python scripts
  
      : use below command to import
        ```
        from dependency-handler import dependencyhandler
        ```
      : now this function takes a list consisting of all module names that are to be installed, as a arguement  
        *example: 
        ```
                   dep=['pillow','jupyter']
                   rs,lftdep=dependencyhandler(dep)
        ```
        This function returns 2 parameters : 
                  >result(1/0/-1) 1 : All modules installed 
                                  0 : No modules installed 
                                 -1 : Some modules can not be installed
                  >leftdependencies(list of unsuccessfull modules)
                  
**If not installed by pip or using repo clone, to import in other python scripts be sure 'dependencyhandler.py' script is in same folder as calling script or specify appropriate path while importing
