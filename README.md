# CYCFBbot
## About
CYCFBbot is a facebook bot project in python3. CYCFBbot provides the framework of
a facebook bot which examines and executes the commands. Facebook bot developers 
can add on commands programs to their designed bot under the framework.

## Installation
`pip3 install git+`

## Usage


### Add commands
All the command programs are subclasses of PgmAbstract in pgmabstract module 
(pgmabstract.py). One can add new command program by writing a subclass of new 
program which inherits PgmAbstact in the same directory. Then add the 
corresponding ("/new_command" : "NewProgramSubclassName") in the list of the 
commandsmap.json file.
