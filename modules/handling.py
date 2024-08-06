# try:
#   import pymysql
# except ImportError:
import pymysql
import sqlite3


class MySQLExecutor:
  def __init__(self, host, user, password, db_name, port):
    self.host = host
    self.user = user
    self.password = password
    self.db_name = db_name
    self.port = port

    self.connection = None
    self.cursor = None
  
  def connect(self):
    try:
      self.connection = pymysql.connect(
        host=self.host,
        user=self.user,
        passwd=self.password,
        db=self.db_name,
        port=self.port
      )
      self.cursor = self.connection.cursor()
      print("Connection seccessful!")
    except pymysql.Error as e:
      print(f"Error connecting to MySQL: {e}")
      print(f" or MySQL not exists")

  def execute(self, sql_code: str):
    if self.connection is None:
      print("No connection to the database. Call connect() first.")
      return
    
    try:
      self.cursor.execute(sql_code)
      self.connection.commit()
      print("SQL execute successfuly!")
      return self.cursor.fetchall()
    except pymysql.Error as e:
      print(f"Error executing SQL: {e}")
      # self.connection.rollback()
      return None

  def fetch_query(self, query, params=None):
    """Fetch results from a query"""
    with self.connection.cursor() as cursor:
      try:
        if params:
          cursor.execute(query, params)
        else:
          cursor.execute(query)
        result = cursor.fetchall()
        return result
      except pymysql.MySQLError as e:
        print(f"Error: '{e}'")
  
  def fetchone(self, query, params=None):
    """Fetchone results from a query"""
    with self.connection.cursor() as cursor:
      try:
        if params:
          cursor.execute(query, params)
        else:
          cursor.execute(query)
        result = cursor.fetchone()
        return result
      except pymysql.MySQLError as e:
        print(f"Error: '{e}'")
    
  def close(self):
    if self.cursor:
      self.cursor.close()
    if self.connection:
      self.connection.close()
      print("Connection closed.")

class SQLite3Executor:
  def __init__(self, db_name) -> None:
    self.db_name = db_name

    self.connection = None
    self.cursor = None
  
  def connect(self):
    try:
      self.connection = sqlite3.connect(self.db_name)
      self.cursor = self.connection.cursor()
      print("Connection seccessful!")
    except sqlite3.Error as e:
      print(f"Error connecting to MySQL: {e}")
  
  def execute(self, sql_code: str):
    if self.connection is None:
      print("No connection to the database. Call connect() first.")
      return
    
    try:
      self.cursor.execute(sql_code)
      self.connection.commit()
      print("SQL execute successfuly!")
      return self.cursor.fetchall()
    except sqlite3.Error as e:
      print(f"Error executing SQL: {e}")
      self.connection.rollback()
      return None
  
  def close(self):
    if self.cursor:
      self.cursor.close()
    if self.connection:
      self.connection.close()
      print("Connection closed.")

class MariaDBExecutor:
  def __init__(self, host, user, password, db_name) -> None:
    self.host = host
    self.user = user
    self.password = password
    self.db_name = db_name
    self.connection = None
  
  def connect(self):
    """Establish a connection to the database."""
    try:
      self.connection = pymysql.connect(
        host=self.host,
        user=self.user,
        password=self.password,
        database=self.db_name
      )
      print("Connected to MariaDB database")
    except pymysql.MySQLError as e:
      print(f"Error connection to MariaDB Platform: {e}")
  
  def close(self):
    """Close the database connection"""
    if self.connection:
      self.connection.close()
      print("MairaDB connection is closed")
  
  def execute(self, query, params=None): 
    """Execute a single query"""
    with self.connection.cursor() as cursor:
      try:
        if params:
          cursor.execute(query, params)
        else:
          cursor.execute(query)
        self.connection.commit()
        print("Query executed successfully")
      except pymysql.MySQLError as e:
        print(f"Error: '{e}'")
  
  def fetch_query(self, query, params=None):
    """Fetch results from a query"""
    with self.connection.cursor() as cursor:
      try:
        if params:
          cursor.execute(query, params)
        else:
          cursor.execute(query)
        result = cursor.fetchall()
        return result
      except pymysql.MySQLError as e:
        print(f"Error: '{e}'")
  
  def fetchone(self, query, params=None):
    """Fetchone results from a query"""
    with self.connection.cursor() as cursor:
      try:
        if params:
          cursor.execute(query, params)
        else:
          cursor.execute(query)
        result = cursor.fetchone()
        return result
      except pymysql.MySQLError as e:
        print(f"Error: '{e}'")



# if __name__ == "__main__":

#   executor = MariaDBExecutor("localhost", 'root', '123456789mM.', 'alakhrah')
#   executor.connect()
#   create_table = """
# DROP TABLE users;
# """
#   executor.execute(create_table)
#   executor.close()


# query = open("query.sql", 'r').read()

# result = executor.execute(query)
# executor.close()

# from werkzeug.security import check_password_hash, generate_password_hash
# result = executor.execute("select * from users;")
# if result is not None:
#   for row in result: 
#     if row and check_password_hash(row[3], "01020"):
#       de = generate_password_hash(row[3]).encode()
#       print(f"ID: '{row[0]}' - Name: '{row[1]}' - Email: '{row[2]}' Password: '{row[3]}'")
# executor.close()

# from werkzeug.security import check_password_hash
# r = check_password_hash("scrypt:32768:8:1$Ulst44mttfzfMCUf$0dec92b0a25a60d1d15e5f251e4ce19127e860640e4ee47c3d0e2b545df7f5e2d1c03d3d729f91c1c455bde700389b7d9c37c702639670a92d9e422417e025dc", "01020")
# print(r)