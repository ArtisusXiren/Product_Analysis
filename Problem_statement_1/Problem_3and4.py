#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
def generate(Id,user_id,status,amount,gateway,timestamp):
    conn=sqlite3.connect(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_1\Database_1.db")
    cursor=conn.cursor()
    table_command="""
    Create Table IF NOT EXISTS Payments(Id INTEGER PRIMARY KEY,
    user_id INTEGER,
    status INTEGER,
    amount INTEGER,
    gateway text,
    timestamp DOUBLE);
    """
    cursor.execute(table_command)
    try: 
        insert_command= """
        Insert INTO  Payments(Id,user_id,status,amount,gateway,timestamp)
        values(?,?,?,?,?,?)
        """
        with conn:                        
            cursor.execute( insert_command,(Id,user_id,status,amount,gateway,timestamp))
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
    {"Id":1,"user_id":17,"status":2,"amount":50,"gateway":"paytm","timestamp":1383678600},
    {"Id":2,"user_id":64,"status":2,"amount":100,"gateway":"google","timestamp":1383709905},
    {"Id":3,"user_id":33,"status":2,"amount":250,"gateway":"apple","timestamp":1583071000},
    {"Id":4,"user_id":628,"status":0,"amount":49,"gateway":"upi","timestamp":1520820200},
    {"Id":5,"user_id":533,"status":1,"amount":99,"gateway":"google","timestamp":1540820200},
    {"Id":6,"user_id":464,"status":2,"amount":150,"gateway":"apple","timestamp":1549082020},
    {"Id":7,"user_id":39,"status":2,"amount":7900,"gateway":"upi","timestamp":1569082020},
    {"Id":8,"user_id":103,"status":2,"amount":4900,"gateway":"tapjoy","timestamp":1582082020},
    {"Id":9,"user_id":293,"status":3,"amount":1500,"gateway":"upi","timestamp":1585082020}
    
]
def gen_product(): 
    for entry in Entries:
        yield entry["Id"],entry["user_id"],entry["status"],entry["amount"],entry["gateway"],entry["timestamp"]
    
for Id,user_id,status,amount,gateway,timestamp in gen_product():
    generate(Id,user_id,status,amount,gateway,timestamp)
print("Success")

conn =sqlite3.connect(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_1\Database_1.db")
statement= """
Select * from matches
"""
data=pd.read_sql(statement,conn)
conn.close
data.to_csv(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_1\Payments.csv")
# In[3]:


def operations():
    conn=sqlite3.connect(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_1\Database_1.db")
    cursor=conn.cursor()
    try:
        command=("""
        SELECT user_id FROM Payments
        WHERE status=2 
        AND gateway!= "tapjoy"
        AND timestamp>=1583001000  
        AND timestamp <=1583778600
        """);
        cursor.execute(command)
        results=cursor.fetchall()
        if results:
            for row in results:
                row=row[0]
                print(f"user_id:{row}")
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


# In[4]:


def generate_2(Id,user_id,createtime,last_active_at):
    conn=sqlite3.connect(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_1\Database_1.db")
    cursor=conn.cursor()
    table_command="""
    Create Table IF NOT EXISTS Users(Id INTEGER PRIMARY KEY,
    user_id INTEGER,
    createtime DOUBLE,
    last_active_at DOUBLE);
    """
    cursor.execute(table_command)
    try: 
        insert_command= """
        Insert INTO  Users(Id,user_id,createtime,last_active_at)
        values(?,?,?,?)
        """
        with conn:                        
            cursor.execute( insert_command,(Id,user_id,createtime,last_active_at))
            conn.commit()      
    except sqlite3.Error as e:
        print("Error executing SQL:", e)
    finally:                                   
        if cursor:                             
            cursor.close()
        if conn:
            conn.close()


# In[5]:


Entries = [
    {"Id":1,"user_id":33,"createtime":1283678600,"last_active_at":1383678600},
    {"Id":2,"user_id":222,"createtime":1383709905,"last_active_at":1483709905},
    {"Id":3,"user_id":354,"createtime":1520420200,"last_active_at":1620420200},
    {"Id":4,"user_id":97886,"createtime":1520820200,"last_active_at":1620820200},
    {"Id":5,"user_id":3532,"createtime":1540820200,"last_active_at":1640820200},
    {"Id":6,"user_id":858,"createtime":1549082020,"last_active_at":1649082020},
    {"Id":7,"user_id":34322,"createtime":1569082020,"last_active_at":1669082020},
    {"Id":8,"user_id":7687,"createtime":1582082020,"last_active_at":1682082020},
    
]
def gen_product(): 
    for entry in Entries:
        yield entry["Id"],entry["user_id"],entry["createtime"],entry["last_active_at"],
    
for Id,user_id,createtime,last_active_at in gen_product():
    generate_2(Id,user_id,createtime,last_active_at)
print("Success")
conn =sqlite3.connect(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_1\Database_1.db")
statement= """
Select * from matches
"""
data=pd.read_sql(statement,conn)
conn.close
data.to_csv(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_1\Users.csv")

# In[6]:


def user():
    conn=sqlite3.connect(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_1\Database_1.db")
    cursor=conn.cursor()
    try:
        command="""
        Select Users.user_id From Payments
        JOIN Users ON Payments.user_id= Users.user_id
        where Payments.timestamp>=1366137000
        AND Payments.timestamp<=1397673000 
        AND Users.last_active_at>=1483209000
        """
        cursor.execute(command)
        results=cursor.fetchall()
        if results:
            for row in results:
                row=row[0]
                print(f"user_id:{row}")
        else:
            print("No columns matched")
    except sqlite3.Error as e:
        print("Error executing SQL:", e)
    finally:                                   
        if cursor:                             
            cursor.close()
        if conn:
            conn.close()
user()


# In[ ]:




