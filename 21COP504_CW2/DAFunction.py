# DAFunction
# Date:17/01/2022
# By F121182


import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt

#retrieve Test1 result of all students of each question 
def Test1_Results():
    try:
        conn = sqlite3.connect("ResultDatabase.db")
        cursor = conn.cursor()
        print("Connected to SQLite")
        
        sql_query = """ SELECT "research id", Grade, Q1, Q2, Q3, Q4, Q5, Q6
                        FROM dfFormattedCleanTest_1"""
        
        dfTest1_Results = pd.read_sql(sql_query, conn)

        conn.close()
    except sqlite3.Error as error:
        print("Fail to retrieve results", error)
    finally:
        if conn:
            conn.close()
            print("SQLite connection is close")
    return dfTest1_Results                 
    

#retrieve Test2 result of all students of each question
def Test2_Results():
    try:
        conn = sqlite3.connect("ResultDatabase.db")
        cursor = conn.cursor()
        print("Connected to SQLite")
         
        sql_query = """ SELECT "research id", Grade, Q1, Q2, Q3, Q4, Q5, Q6
                         FROM dfFormattedCleanTest_2"""
         
        dfTest2_Results = pd.read_sql(sql_query, conn)
 
        conn.close()
    except sqlite3.Error as error:
        print("Fail to retrieve results", error)
    finally:
        if conn:
            conn.close()
            print("SQLite connection is close")
    return dfTest2_Results  
 

 
#retrieve Test3 result of all students of each question 
def Test3_Results():
    try:
        conn = sqlite3.connect("ResultDatabase.db")
        cursor = conn.cursor()
        print("Connected to SQLite")
         
        sql_query = """ SELECT "research id", Grade, Q1, Q2, Q3, Q4, Q5, Q6
                         FROM dfFormattedCleanTest_3"""
         
        dfTest3_Results = pd.read_sql(sql_query, conn)
 
        conn.close()
    except sqlite3.Error as error:
        print("Fail to retrieve results", error)
    finally:
        if conn:
            conn.close()
            print("SQLite connection is close")
    return dfTest3_Results  
 
#retrieve Test4 result of all students of each question 
def Test4_Results():
    try:
        conn = sqlite3.connect("ResultDatabase.db")
        cursor = conn.cursor()
        print("Connected to SQLite")
        
        sql_query = """ SELECT "research id", Grade, Q1, Q2
                        FROM dfFormattedCleanTest_4"""
        
        dfTest4_Results = pd.read_sql(sql_query, conn)

        conn.close()
    except sqlite3.Error as error:
        print("Fail to retrieve results", error)
    finally:
        if conn:
            conn.close()
            print("SQLite connection is close")
    return dfTest4_Results  



#retrieve Mock Test result of all students of each question
def MockTest_Results():
    try:
        conn = sqlite3.connect("ResultDatabase.db")
        cursor = conn.cursor()
        print("Connected to SQLite")
        
        sql_query = """ SELECT "research id", Grade, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10
                        FROM dfFormattedCleanMockTest"""
        
        dfMockTest_Results = pd.read_sql(sql_query, conn)

        conn.close()
    except sqlite3.Error as error:
        print("Fail to retrieve results", error)
    finally:
        if conn:
            conn.close()
            print("SQLite connection is close")
    return dfMockTest_Results  



#retrieve Sum Test result of all students of each question
def SumTest_Results():
    try:
        conn = sqlite3.connect("ResultDatabase.db")
        cursor = conn.cursor()
        print("Connected to SQLite")
        
        sql_query = """ SELECT "research id", Grade, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10
                        FROM dfFormattedCleanSumTest"""
        
        dfSumTest_Results = pd.read_sql(sql_query, conn)

        conn.close()
    except sqlite3.Error as error:
        print("Fail to retrieve results", error)
    finally:
        if conn:
            conn.close()
            print("SQLite connection is close")
    return dfSumTest_Results  




