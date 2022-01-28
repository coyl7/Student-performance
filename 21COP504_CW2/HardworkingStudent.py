# HardworkingStudent
# Date:17/01/2022
# By F121182

import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt

import DAFunction as daf


def stop():
    print ("program stopped running")

def df_biginners():
    df = pd.read_csv("DataFiles/StudentRate.csv")
    #filter out the "Below beginner", "Beginner" students
    hs = ["Below beginner", "Beginner"]
    col_name = "What level programming knowledge do you have?"
    global df1
    global list1
    
    df1 = df.iloc[:, [0,3]]
    df1 = df1.loc[df1[col_name].isin(hs)]
    list1 = df1["research id"].tolist()
    return(df1, list1)


#filter out students got more than 60 in Summative test
#and rated as "below beginner" or "beginner"
def filter_hardworking_student():
    df_biginners()
    SumTest = daf.SumTest_Results()
    
    global df_hw_stu
    
    df_grade_60 = SumTest.loc[SumTest["Grade"] > 60]
    df_hw_stu = df_grade_60.loc[df_grade_60["research id"].isin(list1)]
    df_hw_stu = df_hw_stu.iloc[:,[0,1]]
    return(df_hw_stu)


def hardworking_student():
    left = filter_hardworking_student()
    right = df1
    result = pd.merge(left, right, on="research id", how="left")
    result = result.sort_values(by=["Grade"], ascending=False)
    print(result)
    return(result)


