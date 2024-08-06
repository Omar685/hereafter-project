from modules.handling import MySQLExecutor

executor = MySQLExecutor("localhost", "root", "123456789987654321mM.", "akhirah", port=9500)
executor.connect()