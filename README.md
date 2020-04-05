# Card employee manager


## Usage


Program is divided into two parts: manager client and terminal
client. 

### Manager

Manager client 'manages' whole system, modifies 
various entries in database and allows to add new employees,
terminals, cards.

#### manager.py usage

Open terminal in main directory of project and invoke command:

`python3 manage.py -h`

This will return you basic info how to use this program

For example to add new employee with
name Grzegorz Kowalski write:

`python3 manage.py add -e Grzegorz Kowalski`

Commands to invoke:

`add [-h] [-e Name Surname] [-t terminalID] [-c cardID]`

`delete [-h] [-e employeeID] [-t terminalID] [-c cardID]`

`list [-h] {employees,incidents,days,terminals,cards}`

`raport [-h] employeeID`

`assign [-h] cardID employeeID`

`unassign [-h] cardID`


### Terminal

Used to emulate physical terminal and read card from employees, and log info to system

#### terminal.py usage

Open terminal in main directory of project and invoke command:

`python3 terminal.py -h`

This will return you basic info how to use this function

There are two terminals available out of the box: __1__ and __2__

You can add other terminals via command 
`python3 manage.py add -t <terminalID to be added>`


## File system structure


![Image](images/Tree.png)

### __Auto generated files and folders(.vscode, pycache, .git, init.py)__

Auto generated by IDE and python

### __backend__

Contains functions directly used in CLI. 

#### manageBack.py

Functions for manage.py file

#### terminalBack.py

Functions for terminal.py file


### __database__

Contains direct database files 

#### employee.db

Sqlite3 database with data used in program

![Image](images/db.png)

#### Init.sql

Used to initialise database with sample data for testing

### __images__

Images used in documentation

### __managers__

Scripts which directly communicates with sql database. They are used by __backend__ scripts

### __tests__

Tests from development era. Not intended to run due to various changes of project structure


## Database


Description of tables in sqlite3 database

### __card__

Keeps info about:
1. all cards in system
2. cards employees assigment
3. wheter card was used in given day

### __day__

Keeps info about given day of certain employee

### __employee__

Keeps all employee data

### __incident__

Keeps data about all past incidents(wrong card usages)

### __terminal__

Keeps all terminal data


### __terminalCard__

Keeps data about when terminal was used and by what cardID


## Usage screenshots

![Image](images/s1.png)
![Image](images/s2.png)
![Image](images/s3.png)
![Image](images/s4.png)
