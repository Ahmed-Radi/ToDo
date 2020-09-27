# ToDo

## DataBase project

Change this line of code with your right information
``` app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://username:password@localhost:5432/todoapp' ```

**todoapp** name of the database you should create it manually before running the code

to create database **todoapp**
open CMD(command Prompt) then write:

- ```psql``` OR ```psql.exe -U username -d dbname```
*note:* ``` -d dbname ``` *is optional*

- Password: your password
- CREATE DATABASE todoapp;
- Then run the project you will found the ```todos``` Table is built automatically
- Now open **psql** again then INSERT some columns to retrieve from the database
example for INSERT statements
```
INSERT INTO todos (description) VALUES ('Do a thing 1');
```
## Run project 

- Open CMD(command Prompt) then write:
```
FLASK_APP=app.py
flask run
```
*optional* you can open debug mode using this code ``` FLASK_DEBUG=true```

