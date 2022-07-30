#=========================================================================================================================
#                                                        importing modules
#=========================================================================================================================
print("IMPORTING MODULES")

                              
from mysql.connector import Error                    # FOR FOR ERROR
from mysql.connector import errorcode
from termcolor import colored, cprint         # for colour in print statement     you need to install the module
from colorama import init
from pyfiglet import Figlet
from easygui import *

import pyttsx3                                  # for audio
import mysql.connector                             #FOR SQL CONNECTION
import play_video
import string1                                    # FOR LEARNING ABOUT STRINGS
import io2                                         # FOR INPUT OUTPUT STATMENT
import loop
import os                                        #USED FOR CLEARING THE SCREEN
import project                                      #USED FOR ADVANCED PYTHON
import LLM
import exam
import sys
import matplotlib.pyplot as plt


init()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
### print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#======================================================================================================
#                                 some function of colour module
#======================================================================================================
print_red_on_cyan = lambda x: cprint(x, 'red')
print_blue_on_red = lambda x: cprint(x, 'blue')
print_black_on_white = lambda x: cprint(x, 'black', 'on_white')
print_blue_on_green = lambda x: cprint(x, 'blue')
#======================================================================================================
custom_fig = Figlet(font='5lineoblique')
cprint(custom_fig.renderText(' WELCOME TO THE WORLD OF  PYTHON '),"cyan")
cprint('''\t\t\t\t\t\t\t\t\t\t\t\t\t\t CREATED BY :- TANMAY SARKAR ''',
            'red', attrs=['blink'])
speak(' WELCOME TO THE WORLD OF  PYTHON ')
#====================================================================================================
#                                            SQL connection
#====================================================================================================
count=100
#====================================================================================================
#                                      taking my sql possword from user
#====================================================================================================
speak("Enter your sql password")
P = passwordbox("What is your ""MY SQL "" password ?")
error=""
#====================================================================================================

while True:
    try:
        con = mysql.connector.connect(host="localhost", user="root", passwd=P)
        mycursor = con.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS student")
        mycursor.execute("use student")
        create="""CREATE TABLE IF NOT EXISTS studentinfo(
        name varchar(20),
        age int(5),
        gender char(5),
        marks  int(5) DEFAULT 0,
        id int(5));"""
        
        mycursor.execute(create)
            
        sql = "SELECT * FROM studentinfo"
        mycursor.execute(sql)
        my=mycursor.fetchall()
        for i in my:
            count+=1
    #======================================================================================================
    #                   Taking the requried data for sql
    #======================================================================================================
        speak("Enter your personal information") 
        msg = "Enter your personal information"
        title = "Enter your details"
        fieldNames = ["Name", "Gender ( F|M or f|m)", "age", ]
        Values = multenterbox(msg, title, fieldNames)
        if Values is None:
            sys.exit(0)
        #==================================================================
        # make sure that none of the fields were left blank
        #==================================================================
        while 1:
            errmsg = ""
            for i, name in enumerate(fieldNames):
                if Values[i].strip() == "":
                  errmsg += "{} is a required field.\n\n".format(name)
            if errmsg == "":
                break # no problems found
            Values = multenterbox(errmsg, title, fieldNames, Values)
            if Values is None:
                break
        x=Values
        name=x[0]
        gender=x[1]
        age=x[2]
        
        msg = "HELLO {} Remeber your id is {} ".format(name,count)
        speak(msg)
        msgbox(msg)
    #=====================================================================================================
    #                                   inserting values in table
    #=====================================================================================================
        sql = "insert into studentinfo(name, age, gender,id) values(%s,%s,%s,%s)"
        row=[(name,age,gender,count)]
        mycursor.executemany(sql,row)
        print(mycursor.rowcount, "Record inserted successfully into studentinfo table",)
        con.commit()
    #====================================================================================================
    #                                           CLOSING THE CONNECTION
    #====================================================================================================
        if (con.is_connected()):
            con.close()
            cprint("MySQL connection is closed","cyan")
        print_blue_on_green("You have submitted your details succecfully:")
        break
    #====================================================================================================
    #                                       ERROR HANDLING DURING THE CONNECTION
    #====================================================================================================
    except mysql.connector.Error as error:
        print_red_on_cyan("Failed to insert record into studentinfo table {}".format(error))
        speak("an error occured")
        speak("Enter your sql password again")
        P = passwordbox("What is your ""MY SQL "" password ?")
        error=" "
        
        continue
#==========================================================================================================
#                                            connection closed
#==========================================================================================================
con = True
while con:
    LLM.s()
    #=================================================================================================
    #                                           ENTER CHOICE
    #=================================================================================================
    speak("you have three choices")
    cprint ("1. GET STARTED with PYTHON","cyan")
    cprint ("2. ABOUT PYTHON AND PROJECT","cyan")
    cprint ("3. EXIT","red")
    LLM.s()
    try:
        i1=eval(input("Enter your choice(1-3)"))
    except :
        print_red_on_cyan("no input given")
        print()
        print("program will ask for input again")
        LLM.s()
        i1=eval(input("Enter your choice(1-3):-"))
    os.system('cls')
    
    if i1==1:
        while True:
            speak("you have 6 choice")
            cprint("Enter your choice","blue")
            cprint("1.Basic python","blue")
            cprint("2.Advanced python","blue")
            cprint("3.Exit","red")
            cprint("4.Give a test on python","blue")
            cprint("5.Statistical representation of marks of student","blue")
            cprint("6.previous menue","blue")
        
        
            while True:
                try:
                    i0=int(input(" :-"))
                    break
                except:
                    print_red_on_cyan("NO input given or invalid input")
                    continue
                
            if i0==1:
                os.system('cls')
                con2=True
                while con2:
                    
                        speak("welcome to basic python")
                        speak("you have 7 choice")
                        print_blue_on_green(" Lets start with basic python")
                        print_blue_on_green( "Choose anyone of the module to start")
                        print_blue_on_green( "1. Working with Srings")
                        print_blue_on_green( "2. Simple Input and Output Statements")
                        print_blue_on_green(" 3. Loops in Python")
                        print_blue_on_green(" 4. statement in python")
                        print_blue_on_green(" 5. Data Types and Usage")
                        print_blue_on_green(" 6. previous menu")
                        print_blue_on_green(" 7. video on python")
                        while True:
                            try:
                                i2=int(input("Enter your choice(1-7)"))
                                LLM.s()
                                break
                            except :
                                print_red_on_cyan("no input given")
                                print("program will ask for input again or invalid input")
                                
                                continue
                        
                        if i2==1:
        #===============================================================================================
        #                                       string operation
        #===============================================================================================
                            string1.string()
                            LLM.s()
                            os.system('cls')
                        elif i2==2:
        #================================================================================================
        #                                   Simple I/O Statementelif
        #================================================================================================
                            io2.IO()
                            LLM.s()
                            os.system('cls')
        #=================================================================================================
        #                                            LOOPS
        #=================================================================================================
                        elif i2==3:
                            loop.loop()
                            LLM.s()
                            os.system('cls')
        #=================================================================================================
                            #                   DATA TYPES AND USAGE
        #=================================================================================================
                        elif i2 == 5:
                            z=open("d_data.txt","r")
                            x=z.read()
                            print(x)
                            raw_input=input("Press enter to continue")
                            LLM.s()
                            os.system('cls')
        #===================================================================================================
                            #                  RETURN TO PREVIOUS MENUE
        #===================================================================================================
                        elif i2==6:
                            con2=False
                            
                        elif i2==7:
                            play_video.video()
                        elif i2 not in [1,2,3,4,5,6,7]:
                            speak("invalid input")
                            print("invalid input")
                            continue
    #============================================================================================================
                        #                 LEARNING ABOUT ADVANCED PYTHON
    #============================================================================================================                
        
            if i0 == 2:
                speak("welcome to advanced python")
                project.high()
    #===========================================================================================================
    #                                                          Exiting the program
    #===========================================================================================================
            if i0==3:
                exit()
    #===========================================================================================================
    #                               if user want to give a test on python
    #===========================================================================================================
            if i0==4:
                cprint("DO YOU WANT TO GIVE EXAM ON PYTHON [y|n orY|N]","blue")
                while True:
                    while True:
                    
                        try:
                            i9=input(":-")
                            break
                        except:
                            print_red_on_cyan("No Input given or invalid input")
                            continue
                        
                    if i9.lower()=="y":
                        print(count)
                        a=exam.basic()
                        msg1="YOU GOT {}".format(a)
                        msgbox(msg1)
                    
                        
                        try:
                            con = mysql.connector.connect(host="localhost", user="root", passwd=P,database="student")
                            mycursor = con.cursor()
                            sql = "update studentinfo set marks='%d' where id='%d'"%(a,count)
                            mycursor.execute(sql)
                            print_blue_on_green("your marks updated successfully into studentinfo table")
                            con.commit()
                        
                        #=============================================================================================
                        #                            ERROR HANDLING DURING THE CONNECTION
                        #=============================================================================================
                        except mysql.connector.Error as error:
                            print_red_on_cyan("Failed to insert record into studentinfo table {}".format(error))
                        #=============================================================================================
                        #                                   CLOSING THE CONNECTION
                        #=============================================================================================
                        finally:
                            if (con.is_connected()):
                                con.close()
                                print("MySQL connection is closed")
                        print_blue_on_green("You have submitted your details succecfully:")
                        break
                    elif i9.lower() not in ["y","n"]:
                        speak("invalid input")
                        print("invalid input")
                        continue
                    else:
                        break

                            
            elif i0==5:
                con = mysql.connector.connect(host="localhost", user="root", passwd=P,database="student")
                mycursor = con.cursor()
                l=[]
                q=[]
                kuch_bhi="SELECT NAME FROM STUDENTINFO"
                mycursor.execute(kuch_bhi)
                m=mycursor.fetchall()
                for i in m:
                    for j in i:
                        l.append(j)
                kuch_bhi1="SELECT marks FROM STUDENTINFO"
                mycursor.execute(kuch_bhi1)
                k=mycursor.fetchall()
                for i in k:
                    for j in i:
                        q.append(j)
                plt.bar(l,q)
                plt.show()
            elif i0 not in [1,2,3,4,5,6]:
                speak("invalid input")
                print("invalid input")
                continue
            elif i0==6:
                break
                

#=========================================================================================================                
#                                                   ABOUT PYTHON
#=========================================================================================================
    if i1==2:
                    
            LLM.s()
            cprint("let me frist Tell something about python it advatages/disadvantages its use etc","cyan")
            y=open("python.txt","r")
            m=y.read()
            cprint(m,"cyan")
            LLM.s()
            raw_input=input("press enter to continue")
#==========================================================================================================
#                                             ABOUT THE PROJECT
#==========================================================================================================
            cprint("""___________________________ABOUT THE PROJECT__________________________________

    This project has been created to fulfill the requirment of the CBSE Senior Secondary Examination Class XII
    for Computer science.
    This project is been created by TANMAY SARKAR  and  RAHUL KUMAR of class XII under the guideance of Mr Tanmay suhane sir .
    This project is created to teach a new begineer how to code with python.""","cyan")
            speak("""ABOUT THE PROJECT

    This project has been created to fulfill the requirment of the CBSE Senior Secondary Examination Class XII
    for Computer science.
    This project is been created by TANMAY SARKAR  and  RAHUL KUMAR of class XII under the guideance of Mr Tanmay suhane sir .
    This project is created to teach a new begineer how to code with python.""")
            raw_input=input("press enter to continue")
            os.system('cls')
            
#==========================================================================================================
#                                             ABORTING THE PROGRAM
#==========================================================================================================
    elif i1==3:
        print_blue_on_green("ABORTING PROGRAM..................")
        LLM.s()
        exit()
    elif i1 not in [1,2,3]:
        print("invalid input")
        speak("invalid input")





            
            
