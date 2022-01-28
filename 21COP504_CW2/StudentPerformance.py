# StudentPerformance
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

#function to get dataframe of absolute performance
def df_absolute_performance():
    choice = input("Please enter - test1, test2, test3, test4, sumtest or mocktest:")
    
    if choice == "test1":
        df = Test1
        print(df)
        return(df)
    
    elif choice == "test2":
        df = Test2
        print(df)
        return(df)
    
    elif choice == "test3":
        df = Test3
        print(df)
        return(df)
    
    elif choice == "test4":
        df = Test4
        print(df)
        return(df)
    
    elif choice == "mocktest":
        df = MockTest
        print(df)
        return(df)
    
    elif choice == "sumtest":
        df = SumTest
        print(df)
        return(df)
    
    else:
        print("Invalid choice, please try again")
        return(df_absolute_performance())


#function to plot absolute performance of each test
def plot_absolute_performance():
    choice = input("Please enter which test to plot, \ntest1, test2, test3, test4, sumtest or mocktest?:")
    
    if choice == "test1":
        df = Test1.iloc[:,2:]
        
    elif choice == "test2":
        df = Test2.iloc[:,2:]
        
    elif choice == "test3":
        df = Test3.iloc[:,2:]
        
    elif choice == "test4":
        df = Test4.iloc[:,2:]
        
    elif choice == "mocktest":
        df = MockTest.iloc[:,2:]
        
    elif choice == "sumtest":
        df = SumTest.iloc[:,2:]
        
    else:
        print("Invalid choice, please try again")
        return(plot_absolute_performance())
    
    df.plot(kind="box")
    plt.title("Absolute performance of %s" % choice)
    plt.xlabel("Questions", size=15)
    plt.ylabel("Marks", size=15)
    plt.figure(figsize=(6,8))
    plt.show()

#================================================================

#funtion to get average marks and relative mark
def get_relative(df, last_cols_index):
    mean_df = df.iloc[:,1:8].mean().round(2)
    mean_df = pd.DataFrame(mean_df, columns=["mean"])
    mean_df = mean_df.reset_index(level=0)
    mean_list = mean_df["mean"].tolist()
    df_relative = df.iloc[:,1:].sub(mean_list, axis="columns")
    return(df_relative)


#function to get relative performance dataframe
def df_relative_performance():
    choice = input("Please enter - test1, test2, test3, test4, sumtest or mocktest:")
    
    if choice == "test1":
        df = get_relative(Test1, 8)
        print(df)
        return(df)
    
    elif choice == "test2":
        df = get_relative(Test2, 8)
        print(df)
        return(df)
    
    elif choice == "test3":
        df = get_relative(Test3, 8)
        print(df)
        return(df)
    
    elif choice == "test4":
        df = get_relative(Test4, 4)
        print(df)
        return(df)
    
    elif choice == "mocktest":
        df = get_relative(MockTest, 12)
        print(df)
        return(df)
    
    elif choice == "sumtest":
        df = get_relative(SumTest, 12)
        print(df)
        return(df)
    
    else:
        print("Invalid choice, please try again")
        return(df_relative_performance())
    
    
#function to plot relative performance of each test
def plot_relative_performance():
    choice = input("Please enter which test to plot, \ntest1, test2, test3, test4, sumtest or mocktest?:")
    
    if choice == "test1":
        df = get_relative(Test1, 8)
        df = df.iloc[:,1:]
        
    elif choice == "test2":
        df = get_relative(Test2, 8)
        df = df.iloc[:,1:]
        
    elif choice == "test3":
        df = get_relative(Test3, 8)
        df = df.iloc[:,1:]
        
    elif choice == "test4":
        df = get_relative(Test4, 4)
        df = df.iloc[:,1:]
        
    elif choice == "mocktest":
        df = get_relative(MockTest, 12)
        df = df.iloc[:,1:]
        
    elif choice == "sumtest":
        df = get_relative(SumTest, 12)
        df = df.iloc[:,1:]
        
    else:
        print("Invalid choice, please try again")
        return(plot_absolute_performance())
    
    df.plot(kind="box")
    plt.title("Relative performance of %s" % choice)
    plt.xlabel("Questions", size=15)
    plt.ylabel("Relative marks of average", size=15)
    plt.figure(figsize=(6,8))
    plt.show()


    
######################################################################################

#caculate the average of data
def get_mean(df, last_cols_index):
    mean_df = df.iloc[:,1:last_cols_index].mean().round(2)
    mean_df = pd.DataFrame(mean_df, columns=["average_mark"])
    mean_df = mean_df.reset_index(level=0)
    mean_df = mean_df.rename(columns={"index":"questions"})
    return(mean_df)

dfmean_test1 = get_mean(Test1, 8)
dfmean_test2 = get_mean(Test2, 8)
dfmean_test3 = get_mean(Test3, 8)
dfmean_test4 = get_mean(Test4, 4)
dfmean_mocktest = get_mean(MockTest, 12)
dfmean_sumtest = get_mean(SumTest, 12)

#this function gives individual student performance compare to average
def get_student_performance():
    choice = input("Please enter - test1, test2, test3, test4, sumtest or mocktest:")
    
    if choice == "test1":
        s_id = int(input("Please enter studentID(1-156):"))
        
        s_list = Test1.loc[Test1["research id"] == s_id]
        s_list = s_list.iloc[:,1:].values.squeeze(axis=0)
        column_values = s_list
        student_p = dfmean_test1.assign(student_mark = column_values)
        print(student_p)
        return(student_p)
    
    elif choice == "test2":
        s_id = int(input("Please enter studentID(1-156):"))
        
        s_list = Test2.loc[Test2["research id"] == s_id]
        s_list = s_list.iloc[:,1:].values.squeeze(axis=0)
        column_values = s_list
        student_p = dfmean_test2.assign(student_mark = column_values)
        print(student_p)
        return(student_p)
    
    elif choice == "test3":
        s_id = int(input("Please enter studentID(1-156):"))
        
        s_list = Test3.loc[Test3["research id"] == s_id]
        s_list = s_list.iloc[:,1:].values.squeeze(axis=0)
        column_values = s_list
        student_p = dfmean_test3.assign(student_mark = column_values)
        print(student_p)
        return(student_p)
    
    elif choice == "test4":
        s_id = int(input("Please enter studentID(1-156):"))
        
        s_list = Test4.loc[Test4["research id"] == s_id]
        s_list = s_list.iloc[:,1:].values.squeeze(axis=0)
        column_values = s_list
        student_p = dfmean_test4.assign(student_mark = column_values)
        print(student_p)
        return(student_p)
    
    elif choice == "mocktest":
        s_id = int(input("Please enter studentID(1-156):"))
        
        s_list = MockTest.loc[MockTest["research id"] == s_id]
        s_list = s_list.iloc[:,1:].values.squeeze(axis=0)
        column_values = s_list
        student_p = dfmean_mocktest.assign(student_mark = column_values)
        print(student_p)
        return(student_p)
    
    elif choice == "sumtest":
        s_id = int(input("Please enter studentID(1-156):"))
        
        s_list = SumTest.loc[SumTest["research id"] == s_id]
        s_list = s_list.iloc[:,1:].values.squeeze(axis=0)
        column_values = s_list
        student_p = dfmean_sumtest.assign(student_mark = column_values)
        print(student_p)
        return(student_p)
    
    else:
        print("Invalid choice, please try again")
        return(get_student_performance())
    





