# CYCFBbot
## About
CYCFBbot is a facebook bot project in python3. CYCFBbot provides the framework of
a facebook bot which examines and executes the commands. Facebook bot developers 
can add on commands programs to their designed bot under the framework.
                 
## Installation
`pip3 install git+https://github.com/chingyuchen/CYCFBBot`
                 
## Example
Here we have "/start", "/default" and "/help" commands in the CYCFBbot framwork. The
following examples are based on these three commands. Facebook bot develpers can 
add more command programs to their own CYCFBbot (see Add commands in Usage)

### "/start" command
When users start chating with CYCFBbot or send a text message "/start", CYCFBBot will
execute the "/start" command program which sends a greeting message to the user.         
        
<a href="url"><img src="https://github.com/chingyuchen/CYCFBBot/blob/master/photo_2017-09-02_14-03-17.jpg" height="304" width="213"></a>

<a href="url"><img src="https://github.com/chingyuchen/CYCFBBot/blob/master/photo_2017-09-02_14-03-35.jpg" height="208" width="213"></a>
          
Following the greeting, the CYCFBBot will operates the default program. Here the default 
program asks the user to choose a option as above figures.

### "/default" command
The default program is the standby running program. Whenever a program execution is 
finished, CYCFBBot will automatically run the standby program. For example, as the 
description for the "/start" command operation above, after CYCFBbot finishes the 
start program execution (greeting to the user), CYCFBbot runs the default program. 
Here the default program asks users to choose a option. CYCFBbot also runs default 
program when recieves "/default" command.                
<a href="url"><img src="https://github.com/chingyuchen/CYCFBBot/blob/master/photo_2017-09-03_20-06-49.jpg" height="143" width="213"></a>
                    
### "/help" command 
The help commands in CYCFBbot provides the command instructions. By sending "/help"
to CYCFBbot, CYCFBbot will execute the help program which sends an instruction
message to the user.

<a href="url"><img src="https://github.com/chingyuchen/CYCFBBot/blob/master/photo_2017-09-02_14-04-01.jpg" height="208" width="213"></a>

Again, after the help program execution ends, the CYCFBbot will automatically run
the default program (ask user to choose an option).

### Invalid commands
If a command is invalid, CYCFBbot will send a error message to the user.               
<a href="url"><img src="https://github.com/chingyuchen/CYCFBBot/blob/master/photo_2017-09-02_14-04-08.jpg" height="123" width="213"></a>


              
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
