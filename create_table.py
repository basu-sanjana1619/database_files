import sqlite3
con = sqlite3.connect('IT_company.db')
cur = con.cursor()

cur.execute('''DROP TABLE IF EXISTS Employee''')
cur.execute('''CREATE TABLE Employee(
              name TEXT,
              emp_ID INTEGER)''')
              
#[IF NOT EXISTS] option will create a table if table does not exist             
cur.execute('''CREATE TABLE IF NOT EXISTS Department(
              dep_name TEXT,
              dep_ID INTEGER)''')
              
#commit and save the changes
con.commit()
#close the connection
con.close()

              