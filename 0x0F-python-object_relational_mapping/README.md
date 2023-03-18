
<img src="https://pbs.twimg.com/media/EXBAXKbXYAQ7TX2.jpg">

## Python - Object-relational mapping (ORM)
Object-relational mapping (ORM) is a programming technique that maps data from an object-oriented language to a relational database. ORM is commonly used in Python applications to abstract database access, allowing developers to use object-oriented programming (OOP) principles to interact with databases.

Python provides several ORM libraries, including SQLAlchemy, Django ORM, and Peewee. SQLAlchemy is one of the most widely used ORM libraries in Python, providing a comprehensive set of tools for working with relational databases.

### Python - Object-relational mapping with SQLAlchemy
SQLAlchemy is a Python SQL toolkit and Object-Relational Mapping (ORM) library. It provides a set of high-level API for connecting to relational databases, performing SQL operations, and mapping relational database tables to Python objects. SQLAlchemy allows developers to work with Python objects, while providing powerful and flexible mechanisms for database querying and manipulation.
You can install SQLAlchemy using pip:
```sql
pip install SQLAlchemy
```
#### Connecting to a database
To connect to a database, you first need to create an instance of the create_engine class, which represents the database connection. The following example connects to a MySQL database:
```python
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://user:password@host:port/database')
```

######  lists all states from the database hbtn_0e_0_usa
```python
#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
```
import the mysql database and sys which we use to write the script
then use python idiom that checks whether the script is being run as the main program or not (if __name__ = "__main__")
the next line this line connects to a MySQL database with the specified parameters. host specifies the server name or IP address of the MySQL server, which is set to localhost in this case. user, passwd, and db are specified using command line arguments, which are passed in through the sys.argv list. port specifies the port number for the MySQL server, which is set to 3306
after this we use the db.cursor() function to create a cursor object, which is used to execute sql queries and fetch results.
next step is the sql query so we use the cursor object to execute this 
cur.execute("select * from states")
Next line uses The fetchall() method is a method of the cursor object cur. It is used to retrieve all rows of a query result set and return them as a list of tuples, where each tuple represents a single row.
After executing a SELECT statement with cur.execute(), the fetchall() method can be called to retrieve all of the results at once. The rows are returned as a list, where each element of the list is a tuple representing a row of data.
Calling fetchall() would return a list of tuples 
Once the results have been fetched with fetchall(), the list of tuples can be iterated over to process each row of data.
next line for loop to iterate over each row in the rows object. Each row is stored as a tuple, where each element of the tuple corresponds to a column in the result set.
The print() function is then called with the row object as an argument, which prints the entire row as a tuple to the console
the last lines close the cursor and database connection objects, respectively, to release any resources that they are holding.(i like writing note)
