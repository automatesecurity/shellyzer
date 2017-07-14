# Shellyzer v 1.0
A python script to conduct static analysis of shell scripts that can be used as a standalone script or integrated into a build pipeline.



## Assumptions

Shellyzer assumes you're running python at `#!/bin/env python` if you env is different, you will have to customize this prior to usage.



## Usage

To use Shellyzer, simply call it from the command-line.

`./shellyzer.py`

It will prompt you for the full path to your shell script(s) you would like analyzed.  

To access the docstrings, run an interactive session like the example below:
```python
Python 2.7.13 (default, Dec 18 2016, 07:03:39) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import shellyzer
>>> help(shellyzer)
Help on module shellyzer:

NAME
    shellyzer

FILE
    /Users/dwood/projects/shellyzer/shellyzer.py

CLASSES
    __builtin__.object
        Logger
    
    class Logger(__builtin__.object)
     |  Ensure the logger is setup properly
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |  
     |  flush(self)
     |  
     |  write(self, message)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    checkStrings(filepath)
        Compare lint signatures against lines of code
        within each line of a file retrieved from the 
        given filepath.
        
        The following method will loop through each file
        matching the .sh extension and compare it to the
        lintList to determine if a signature exists in a
        source file.  If a signature is found in source 
        then the line number and line of code will be 
        sent to stdout and result in a response code (0).
        
        For issues found, a counter will increment to track
        for reporting purposes per source file and for the
        overall run of the script across multiple files.
    
    main()


>>> 
```

## Pipeline Integration

In addition to calling it directly for ad-hoc usage, you can also integrate the script into a build pipeline to automate static analysis using something like Jenkins with git hooks upon commit to scan your code base.

To facilitate this the script will generate response codes for pass (0) and fail (1).  You can choose to break your build upon detecting a fail (1) if you so choose.
