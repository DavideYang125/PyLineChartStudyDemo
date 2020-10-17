import pymysql
import pandas as pd

def Read_database (sql):
    user_name='root'
    password='root'
    address='localhost'
    port='3306'
    database_name='cry'

    conn = pymysql.connect(host = address,user = user_name,passwd = password,\
                           db = database_name , port = int(port) ,charset = "utf8mb4")
    try:
        #df = pd.read_sql (sql,con = conn)
        cursor = conn.cursor()
        cursor.execute(sql)
        df = cursor.fetchall()
    except:
        print ('\n Reading Error  \n')    
    finally:
        conn.close()
    print ('\n Completion of data reading \n')    
    return (df) 