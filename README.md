# Shellyzer v 1.0
A python script to conduct static analysis of shell scripts that can be used as a standalone script or integrated into a build pipeline.



## Assumptions

Shellyzer assumes you're running python at `#!/bin/env python` if you env is different, you will have to customize this prior to usage.



## Usage

To use Shellyzer, simply call it from the command-line.

`./shellyzer.py`

It will prompt you for the full path to your shell script(s) you would like analyzed.  



## Pipeline Integration

In addition to calling it directly for ad-hoc usage, you can also integrate the script into a build pipeline to automate static analysis using something like Jenkins with git hooks upon commit to scan your code base.

To facilitate this the script will generate response codes for pass (0) and fail (1).  You can choose to break your build upon detecting a fail (1) if you so choose.