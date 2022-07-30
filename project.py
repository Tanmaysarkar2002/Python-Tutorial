#==========================================================================
#                                 importing modules
#==========================================================================
def high():
        import fun
        import stack
        import Queue
        import LLM
        import os
        import image
        import linear
        import queuevideo
        import  stackvideo
        import datafilevideo
        import advanced
        from termcolor import colored, cprint
        from colorama import init
        init()
        con2=True
        while con2:
                cprint(" Lets start with advanced python","blue")
                cprint( "Choose anyone of the module to start","blue")
                cprint(" 1. Python Functions and Modules","blue")
                cprint(" 2. list's and linner  search & binnary search","blue")
                cprint(" 3. Stacks and Queues","blue")
                cprint(" 4. Data File Handiling","blue")
                cprint(" 5.Get back to main menu","blue")
                cprint(" 6. watch a video on advanced python press 't' to end the video","blue")
                LLM.s()
                try:
                    i2=int(input(":-"))
                except:
                    print("No input given")
                    i2=int(input("Enter again:-"))
                    
                if i2==1:
#============================================================================
                                     # lists
#============================================================================
                         fun.fun()
                         LLM.s()
                         os.system('cls')
                elif i2==2:
                        cprint("""list is a standard data type of python that can store a sequence of values
            belonging to any type . The list are depected through square bracket
            EXAMPLES
            1. Empty list--> []
            2. list of integer --> [1,2,3,4,5,6,7]
            3. list of floatijng no--> [1.2,2.1,3.5]
            4.list of characters -->["a","s',"d"]
            5. list of string -->["one","two","three"]
            6. list of mixed valuse -->[1,2"d","f",1.2,"zero"]""","green")
                        LLM.s()
                        cprint("If you want to search an element in list then their are two method","blue")
                        cprint("1.Bineary search ","blue")
                        cprint("2.Linner search","blue")
                        LLM.s()
                        cprint("If you want to short a list then there are two method","blue")
                        cprint("3.bubble short","blue")
                        cprint("4.Insertion sort","blue")
                        LLM.s()
                        try:
                            i3=int(input("Enter your choice (1-4)"))
                        except:
                            cprint("No input given ","red")
                            print("program will ask for input again","blue")
                            i3=int(input("Enter your choice (1-4)"))
                        os.system('cls')
                        if i3==1:
                            cprint("ALGORITHM for binary search","blue")
                            #=============================================================
                            #              display image
                            #=============================================================
                            image.img()
                            
                            raw_input=input("Press enter ro continue:-")
                            
                            n= int(input("Enter desired linear list size(max . 50.....):--"))
                            print("\nEnter elements for linear list\n")
                            ar=[0]*n
                            for i in range(n):
                                ar[i]=int(input("Element"+str(i)+":"))
                            item = int(input("\nEnter Element to be searched for.......:--"))
                            d1=LLM.b_s(ar,item)
                            if d1==False:
                                print("Element not found")
                            else:
                                cprint("##########Element found at ",d1,"############","green")
                        elif i3==2:
                            n= int(input("Enter desired linear list size(max . 50.....):--"))
                            print("\nEnter elements for linear list\n")
                            ar=[0]*n
                            for i in range(n):
                                ar[i]=int(input("Element"+str(i)+":"))
                            item = int(input("\nEnter Element to be searched for.......:--"))
                            d1=LLM.l_s(ar,item)
                            if d1==False:
                                print("Element not found")
                            else:
                                print("##########Element found at ",d1,"############")
                        if i3==3:
                            do=input("Do you want to watch a video on linear search (Y|N)")
                            if do.lower() == "y":
                                linear.video()
                            else:
                                cprint("Then lets see the code","green")
                            n= int(input("Enter desired linear list size(max . 50.....):--"))
                            print("\nEnter elements for linear list\n")
                            ar=[0]*n
                            for i in range(n):
                                ar[i]=int(input("Element"+str(i)+":"))
                            LLM.b_sort(ar)
                        if i3==4:
                            n= int(input("Enter desired linear list size(max . 50.....):--"))
                            print("\nEnter elements for linear list\n")
                            ar=[0]*n
                            for i in range(n):
                                ar[i]=int(input("Element"+str(i)+":"))
                            LLM.i_sort(ar)
                            raw_input=input("press enter to continue")
                        LLM.s()
#=============================================================================================
                        #                          SATCK AND QUEUE
#=============================================================================================
                if i2==3:
                        q=True
                        while q:
                            print("""1.Stack
            2.Queue
            3.Previous menu""")
                            i3=int(input(":--"))
                            if i3==1:
                                kuchbhi=input("Do you want watch a video onn stack [y|n]")
                                if kuchbhi.lower()=="y":
                                    stackvideo.video()
                                else:
                                    cprint("Then lets try the code")
                                stack.stack()
                                raw_input=input("press enter to continue")
                            elif i3==2:
                                Queue.queue()
                                kuchbhi1=input("Do you want watch a video onn stack [y|n]")
                                if kuchbhi1.lower()=="y":
                                    queuevideo.video()
                                LLM.s()
                                raw_input=input("press enter to continue")
                            else:
                                q=False
#================================================================================================
                #                                  DATA FILE HANDLING
#================================================================================================
                elif i2==4:
                        kuchbhi1=input("Do you want watch a video onn datafile handling(Y|N)")
                        if kuchbhi1.lower()=="y":
                                    datafilevideo.video()
                        
                        f=open("data file handling.txt","r")
                        p=f.read()
                        cprint(p,"blue")
                        LLM.s()
                        raw_input=input("press enter to continue")
                elif i2==5:
                        con2=False
                        LLM.s()
                elif i2 == 6:
                    advanced.video()
                else:
                    print("Invalid input")
                        
                    
