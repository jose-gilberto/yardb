
# Utils

## CLI Interface

The command line interface is responsible for starting a class that receives the sql statements to be executed by dbms. An example implementation would be as follows:

```python

class CLIInterface:

    @staticmethod
    def run():
        while True:
            # Do the processing of information
            # Calls DBMS passing the query
            ...

```

The loop runs until an exit command is entered by the user. Possible commands are:

- `.exit`
- `.tables`

All commands are started with a `.` followed by the statement.

### Overall Statements

These are commands that start with a period, these commands are executed without going through the normal processes of reading an SQL command. That is, they start and are processed by custom and static pipes. They can be used regardless of the database file structure.

| command | explanation |
| --- | --- |
| `.exit` | Calls a exit, breaking the loop and closing the connection with the yardb. |
| `.tables` | Shows all the existing tables in this database. |

In the future, new commands can be created and added to this list.

### SQL Statements

Only in v0.2+.

## SktInterface (Socket Interface)

Only in v0.5+.
