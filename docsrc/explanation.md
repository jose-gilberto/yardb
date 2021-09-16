
## Architecture

The project will be builded on top of the following architecture of a dbms:

![arch](https://raw.githubusercontent.com/jose-gilberto/yardb/main/architecture.svg)

Explaining each part separately.

### Query (Query Manager)

Manages queries based on a subset of SQL. Some new commands implemented while others were removed to make building the base easier. All grammar can be found in this [link]().

#### Query Parser

Do the compiler functions on top of each statement. Following this sequence:  
- Tokenize (Lexer)  
- Parser (Parser)  
- Sematic analyzer  
- AST build  

#### Query Optimizer

Run an optimization on top of an AST, making the changes based on relational algebra functions like projection and others functions.

#### Query Planner

Do the execution plan based on the AST generated before, using a set of algorithms builded internally on the yardb.

---

### Metadata

Contains information relating to tables, columns, schemas, and other types of data relating to the stores used internally by yardb.

### Indexes

---

### Storage Manager

#### File Manager
#### Memory Manager
#### Buffer
#### Data

---

### Transaction Manager

#### Concurrency Control

#### Recovery Manager

#### .logs

---

### Executor