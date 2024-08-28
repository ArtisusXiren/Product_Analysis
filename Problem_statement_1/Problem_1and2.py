#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
def generate(Id,home_team_id,away_team_id,Type,timestamp):
    conn=sqlite3.connect(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_1\Database_1.db")
    cursor=conn.cursor()
    table_command="""
    Create Table IF NOT EXISTS matches(Id INTEGER PRIMARY KEY,
    home_team_id INTEGER,
    away_team_id INTEGER,
    Type text,
    timestamp DOUBLE);
    """
    cursor.execute(table_command)
    try: 
        insert_command= """
        Insert INTO  matches(Id,home_team_id,away_team_id,Type,timestamp)
        values(?,?,?,?,?)
        """
        with conn:                        
            cursor.execute( insert_command,(Id,home_team_id,away_team_id,Type,timestamp))
            conn.commit()      
    except sqlite3.Error as e:
        print("Error executing SQL:", e)
    finally:                                   
        if cursor:                             
            cursor.close()
        if conn:
            conn.close()


# In[2]:


Entries = [
    {"Id":1,"home_team_id":17,"away_team_id":629,"Type":"F5","timestamp":1383678600},
    {"Id":2,"home_team_id":64,"away_team_id":211,"Type":"League","timestamp":1383709905},
    {"Id":3,"home_team_id":34,"away_team_id":209,"Type":"League","timestamp":1520420200},
    {"Id":4,"home_team_id":628,"away_team_id":229,"Type":"F5","timestamp":1520820200},
    {"Id":5,"home_team_id":533,"away_team_id":142,"Type":"F5","timestamp":1540820200},
    {"Id":6,"home_team_id":464,"away_team_id":66,"Type":"F5","timestamp":1549082020},
    {"Id":7,"home_team_id":39,"away_team_id":203,"Type":"F5","timestamp":1569082020},
    {"Id":8,"home_team_id":103,"away_team_id":58,"Type":"Alliance","timestamp":1582082020},
    {"Id":9,"home_team_id":293,"away_team_id":86,"Type":"League","timestamp":1585082020}
    
]
def gen_product(): 
    for entry in Entries:
        yield entry["Id"],entry["home_team_id"],entry["away_team_id"],entry["Type"],entry["timestamp"]
    
for Id,home_team_id,away_team_id,Type,timestamp in gen_product():
    generate(Id,home_team_id,away_team_id,Type,timestamp)
print("Success")

conn =sqlite3.connect(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_1\Database_1.db")
statement= """
Select * from matches
"""
data=pd.read_sql(statement,conn)
conn.close
data.to_csv(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_1\matches.csv")
# In[3]:


def operations():
    conn=sqlite3.connect(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_1\Database_1.db")
    cursor=conn.cursor()
    try:
        command=("""
        SELECT home_team_id ,Count(*) AS match_count FROM matches
        WHERE Type='F5'
        AND timestamp>=1583001000  
        AND timestamp <=1583778600
        GROUP BY home_team_id
        HAVING COUNT(*)>=3
        """);
        cursor.execute(command)
        results=cursor.fetchall()
        if results:
            for row in results:
                home_team_id=row[1]
                matches_played=row[0]
                print(f"home_team_id:{home_team_id}, matches_played:{matches_played}")
        else:
            print("No matching columns")
    except sqlite3.Error as e:
        print("Error executing SQL:", e)
    finally:                                   
        if cursor:                             
            cursor.close()
        if conn:
            conn.close()
operations()


# In[ ]:




