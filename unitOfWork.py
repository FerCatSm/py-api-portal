#!/usr/bin/env python3

import os
import connection

class Repository:
 def __init__(self):
  self.db = init_connection_engine()

  print("Conexión establecida")

 def select_user(self, id):
  sql = 'SELECT nationalId, name, lastName, age, originPlanet, pictureUrl FROM people where nationalId =\'{}\''.format(id)
  try:
   with self.db.connect() as conn:
    userCursor = conn.execute(sql).cursor
    result = {}
    column = [str(t[0]).replace("b","").replace("'","") for t in userCursor.description]
    user = userCursor.fetchone()
    result = {column[0]: user[0], column[1]: user[1], column[2]: user[2], column[3]: user[3], column[4]: user[4], column[5]: user[5]}      
    return result
  except Exception as e:
   return None
   
 def select_all_users(self):
  sql = 'SELECT nationalId, name, lastName, age, originPlanet, pictureUrl FROM people'
  try:
   with self.db.connect() as conn:
    usersCursor = conn.execute(sql).cursor
    column = [str(t[0]).replace("b","").replace("'","") for t in usersCursor.description]
    result = []
    users = usersCursor.fetchall()
   for row in users:
    result.append({column[0]: row[0], column[1]: row[1], column[2]: row[2], column[3]: row[3], column[4]: row[4], column[5]: row[5]})
   print(result)
   return result
  except Exception as e:
   raise  
   
   
def init_connection_engine():
 db_config = {
        "pool_size": 5,
        "max_overflow": 2,
        "pool_timeout": 30,  # 30 seconds
        "pool_recycle": 1800,  # 30 minutes
    }

 if os.environ.get("DB_HOST"): 
  return connection.init_tcp_connection_engine(db_config)
 else:
  return connection.init_unix_connection_engine(db_config)

