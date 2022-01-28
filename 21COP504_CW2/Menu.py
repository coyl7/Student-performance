# Menu
# Date:17/01/2022
# By F121182

import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt

import DAFunction as daf
import TestResult as tr
import StudentPerformance as sp
import UnderperformingStudent as us
import HardworkingStudent as hs

def stop():
    print ("program stopped running")

def display_menu():
    """
    Building Menu Options
    
    """
    print ("\n")
    print ("**********************")
    print ("*------Menu----------*")
    print ("**********************")
    print ("Please select an option below")
    print ("\t(d) list student performance")
    print ("\t(p) visualise student performance")
    print ("\t(a) list absolute performance")
    print ("\t(va) visualise absolute performance")
    print ("\t(r) list relative performance")
    print ("\t(vr) visualise relative performance")
    print ("\t(i) list individual performance compare to average")
    print ("\t(u) show underperformed students")
    print ("\t(h) show hard working students")
    print ("\t(s) program stop running")
 
#################################################
#------------------Main-------------------------#
#################################################

while True:
    display_menu()
    menuoption=input("\t\n:>") 
    if menuoption=="d":
        tr.test_result()
    elif menuoption=="p":
        tr.plot_test_result()
    elif menuoption=="a":
        sp.df_absolute_performance()
    elif menuoption=="va":
        sp.plot_absolute_performance()
    elif menuoption=="r":
        sp.df_relative_performance()
    elif menuoption=="vr":
        sp.plot_relative_performance()
    elif menuoption=="i":
        sp.get_student_performance()    
    elif menuoption=="u":
        us.under_performing_student()
    elif menuoption=="h":
        hs.hardworking_student()    
    elif menuoption=="s":
        stop()
        break    
    else:
        print ("sorry we don't have that option") 



