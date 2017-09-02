# CYCFBbot
## About
CYCFBbot is a facebook bot project in python3. CYCFBbot provides the framework of
a facebook bot which examines and executes the commands. Facebook bot developers 
can add on commands programs to their designed bot under the framework.

## Installation
`pip3 install git+https://github.com/chingyuchen/CYCFBBot`

## Usage
### Run the CYCFBbot
1. download all the files (see Installation)
2. create a file "Token" in the same directory, write the token of your own bot
in the file. (If you haven't got a facebook bot, please check [here](https://developers.facebook.com/docs/messenger-platform/guides/quick-start))
3. execute        
`./cycfbbot`

### Add commands
All the command programs are subclasses of PgmAbstract in pgmabstract module 
(pgmabstract.py). One can add new command program by writing a subclass of new 
program which inherits PgmAbstact in the same directory. Then add the 
corresponding ("/new_command" : "NewProgramSubclassName") in the list of the 
commandsmap.json file.
