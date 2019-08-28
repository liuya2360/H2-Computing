#Database 

**Defination:** An organised collection of data in persistent storage. 

##### Flat File

* Anomalies during insert, delete, update adn query

##### Relational Data Model 

* ERD -> entities, relationships, cardinality 
* Normalisatuons -> Relations(Tables), Attributes, Primary/Foreign keys 
* Goals of Normalisation 
	* Avoid redundancy 
	* Maintain consistency 
	* Avoid anomalies

#### Terms
* Table, entity, relation 
* rows, record, tuple 
* attributes, column, fields 
* relationships 
* integrity rules, constraints 

### Database Applicaiton 
**Defination:** A program for entering and 

### Database Management Systems(DBMS) 
**Defination:** Software for the implementation and management of databases. 

### Features of a Database Management System
* _Persistent data_
* Data Dictionary 
* Security 
* Concurretn Access 
* Integrity 
* _Data Manipulation Language (DML)_ 
* _Data Defination Language (DDL)_ 

#### Data Ditionary 
* Meta data 
* the description of tabels, relationships and all design information such as indexing. 
	* indexes are data structures created for fast retrieval 
* the rules about data integrity including validation rules for all attributes. 

#### Data Integrity 
* Enforces rules known as database constraints to ensure the accuracy and consistency of the data 
* Example: NOT NULL, UNIQUE, CHECK 

##### Type of keys in a database 
* Primary 
	* Unique 
	* can be a few attributes 
* Foreign 
	* reference to the primary key of another table 
	* creates a rule (relationship) 
* _Secondary_ 
	* potential keys 
* _Composite_ 

##### Referential Integrity 
* Referencdial integrity using foreign key and primary key constaints 
* Cannot insert a record in Student table until the referenced RTacher record is created 
* Cannot delete/update a Teacher record until all the records in Student table that references it are deleted. 

###### By Aug 8 
-- 

### Concurrent Access 
* Two users can access the database at the same time. 
* When two users send request to edit the database, one of the user's request will be paused and will only be excecuted once the other user commit the change (finish editing) 

### Data Security
* Access Control 
	* WHO can access WHAT 
* Backup 
	* Full (weekly) 
	* Differential, backup only changes since last full (daily) 
	* Purpose: for recovery when data is lost or corrupted 
* Archive 
	* Purpose: for space management and long term retention. Original may be deleted. 
	* Not necessarily deleted 

### SQL (Structured Query Language) 
* A computer language that aim to store, manipulate and retrive data in database. 
* 
* Types: 
	* Data Definatio Langueage (DDL) 
		* Create, altering and deleting tabels
	* Data Manipulation Language (DML) 
		* Inserting, updating and deleting rows 
		* Query tables 
	* Dtabase Control Language (DCL) 
		* Controlling access to the database 
	* Transaction Control Language (TCL) 
		* Dealing with transactions within a database  
* Type Affinities in SQLite 
	* SQLite supports the concept of **type affinity** on columns 
	* Type affinity refers to the **preferred type** for data stored in a column 
	* SQLite Type Affinities: **integer**, **text**, **real**, numberic, blob  

### Create Table 

### Multi-table SELECT Statements 
* SELECT loan.name FORM book, loan WHERE book.isbn13 = loan.isbn13 AND book.title = 'Introduction to Algorithms'
* SELECT loan.name FROM book INNER JOIN `