# UnderperformingStudent
# Date:17/01/2022
# By F121182

import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt

import DAFunction as daf

#retrieve the data we need
Test1 = daf.Test1_Results()
Test2 = daf.Test2_Results()
Test3 = daf.Test3_Results()
Test4 = daf.Test4_Results()
MockTest = daf.MockTest_Results()
SumTest = daf.SumTest_Results()


def stop():
    print ("program stopped running")

#funtion to check under perform students in each test
def check_under_perform(test_df):
    df = test_df[(test_df["Grade"] > 1) & (test_df["Grade"] <= 50)]
    df = df.iloc[:,[0,1]]
    return(df)

#find under perform students in each test
up_t1 = check_under_perform(Test1)
up_t2 = check_under_perform(Test2)
up_t3 = check_under_perform(Test3)
up_t4 = check_under_perform(Test4)
up_mt = check_under_perform(MockTest)
up_st = check_under_perform(SumTest)


#function to look for under performing student
#criteria will be students who got lower than 51 for their summative test,
#and 2 more tests lower than 51.
def under_performing_student():
    left = up_st
    right = [up_t1, up_t2, up_t3, up_t4, up_mt]
    
    #join all the under perform in all the tests together
    for i in right:
        left = pd.merge(left, i, on="research id", how="left")
    
    #change column names
    left.columns = ["research id", "sumtest", "test1", "test2",
                "test3", "test4", "mocktest"]

    #count the number of tests under performed  
    left["total_underperform_test"] = left.iloc[:,1:].apply(lambda x: x.count(), axis=1)
    global up_students
    up_students = left.loc[left["total_underperform_test"] >= 3]
    up_students.sort_values(by="sumtest")
    print(up_students)

    ########################################################################################    
    #try to highlight lowest mark, but did not work
    # def highlight_min(s, props=''):
    #     return np.where(s == np.nanmin(s.values), props, '')
    
    # up_students.apply(highlight_min, props='color:white;background-color:red;', axis=1)
    #########################################################################################
    return(up_students)







