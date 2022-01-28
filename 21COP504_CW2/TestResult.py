# TestResults
# Date:17/01/2022
# By F121182

import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt

import DAFunction as daf


#retrieve test result data 
dfTest1_Results = daf.Test1_Results()
dfTest2_Results = daf.Test2_Results()
dfTest3_Results = daf.Test3_Results()
dfTest4_Results = daf.Test4_Results()
dfMockTest_Results = daf.MockTest_Results()
dfSumTest_Results = daf.SumTest_Results()



def stop():
    print ("program stopped running")


#function to create test result dataframe
def test_result():
    global s_id
    s_id = int(input("Plese enter student ID(1-156):"))
    allgrades = []
    alltest = [dfTest1_Results, dfTest2_Results, dfTest3_Results, dfTest4_Results, dfMockTest_Results, dfSumTest_Results]

    for i in alltest:
        grade = i.loc[i["research id"] == s_id, "Grade"].to_list()
        allgrades = allgrades + grade
    
    global df_allgrades
    data = {"Test":["Test1", "Test2", "Test3", "Test4", "MockTest", "SumTest"], "Grade":allgrades}     
    df_allgrades = pd.DataFrame(data)
    print(df_allgrades)
    return(df_allgrades)


#============================================================================================================================

#visualise test result
def plot_test_result():
    plot = df_allgrades.plot(kind="bar", x="Test", 
                              legend=None,
                              color='skyblue')
    #annotation 
    for bar in plot.patches:
        plot.annotate(format(bar.get_height(), '.2f'),
                      (bar.get_x() + bar.get_width() / 2,
                      bar.get_height()), ha='center', va='center',
                      size=8.5, xytext=(0, 5),
                      textcoords='offset points')

    #remove top and right frame
    plot.spines["top"].set_visible(False)
    plot.spines["right"].set_visible(False)
    #set title and labels
    plt.title("Test result of student id %i" % s_id, size=15)
    plt.xlabel("Tests", size=15)
    plt.ylabel("Marks", size=15)
    plt.figure(figsize=(6,8))
    plt.show()



