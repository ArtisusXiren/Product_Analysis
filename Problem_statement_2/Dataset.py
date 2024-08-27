#!/usr/bin/env python
# coding: utf-8

# In[5]:


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
def generate(Class,Gender,Values):
    conn=sqlite3.connect(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_2\Database.db")
    cursor=conn.cursor()
    table_command="""
    Create Table IF NOT EXISTS Section_2(Class INTEGER,
    Gender varchar(5),
    "Values" INTEGER);
    """
    cursor.execute(table_command)
    try: 
        insert_command= """
        Insert INTO Section_2(Class,Gender,"Values")
        values(?,?,?)
        """
        with conn:                        
            cursor.execute( insert_command,(Class,Gender,Values))
            conn.commit()      
    except sqlite3.Error as e:
        print("Error executing SQL:", e)
    finally:                                   
        if cursor:                             
            cursor.close()
        if conn:
            conn.close()


# In[6]:


Entries = [
    {"Class":4,"Gender":"Female","Values":10},
    {"Class":4,"Gender":"Male","Values":3},
    {"Class":5,"Gender":"Male","Values":1},
    {"Class":1,"Gender":"Female","Values":5},
    {"Class":1,"Gender":"Male","Values":7},
    {"Class":2,"Gender":"Female","Values":2},
    {"Class":5,"Gender":"Female","Values":5},
    {"Class":2,"Gender":"Male","Values":10}
    
]
def gen_product(): 
    for product in Entries:
        yield product["Class"],product["Gender"],product["Values"]
    
for Class, Gender, Values in gen_product():
    generate(Class,Gender,Values)
print("Success")






# In[7]:


conn=sqlite3.connect(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_2\Database.db")
select_query="""
Select* from Section_2
"""
data=pd.read_sql_query(select_query,conn)
conn.close()
data.to_csv(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_2\table.csv",index=False)
print("Saved")
    


# In[10]:

def ascending():
    data=pd.read_csv(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_2\table.csv")
    Class_df=data.sort_values(by='Class')
    #Class_df.columns=['Class','Gender','Values']
    print(Class_df)
ascending()


# In[11]:

def plot():
    data=pd.read_csv(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_2\table.csv")
    plt.figure(figsize=(10,6))
    for gender in data['Gender'].unique():
        subset=data[data['Gender']==gender]
        plt.scatter(subset['Class'],subset['Values'],label=gender)
    plt.xlabel('Class')
    plt.ylabel('Values')
    plt.legend(title='Gender')
    plt.show()
plot()


# In[12]:


def uni():
    data=pd.read_csv(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_2\table.csv")
    data_df=data.groupby(['Class','Gender'])['Values'].unique()
    print(data_df)
uni()


# In[13]:


def reshape():
    data=pd.read_csv(r"C:\Users\ArtisusXiren\Desktop\Hitwicket\Problem_statement_2\table.csv")
    reshape=data.pivot(index='Class',columns='Gender', values='Values')
    reshape.reset_index(inplace=True)
    reshape.columns.name=None
    reshape =reshape[['Class','Male','Female']]
    print(reshape)
reshape()


# In[ ]:




