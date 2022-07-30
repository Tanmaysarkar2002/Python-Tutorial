from termcolor import *
from colorama import init
init()
def fun():
                 
                 con4=True
                 while con4:                 
                     cprint ("Python offers 3 type of Functions","blue")
                     cprint ("1.In-built functions","blue")
                     cprint ("2.Function defined in Modules","blue")
                     cprint ("3.User  defined functions","blue")
                     cprint ("4.Get back to previous menu","blue")
                     i4=eval(input("enter your choice(1-4)"))
                     if i4==1:
                        print( "Python offers some builtin functions which are always availabel to use")
                        print (" eg. len(),type(),int()")
                        print( ">>> a=Python")
                        print (">>>len(a)")
                        print ("   6")
                        print("There are two types of IN-Built function ")
                        f=True
                        while f:

                            print("""
                                  1.Mathematical
                                  2.String
                                  3.Previous menu""")
                            a=int(input("Enter your choice:-"))
                            if a==1:
                                print("""
                            1. oct(<integer>)
                                      "return octal string for given number "
                            2. hex(<integer>)
                                      "return hex string for given number  "
                           3. int(<integer>)
                                   "Turncates the fractional part of given number nad returns
                                  only the integer or whole part."
                           4. round(<number>,[<ndigits>])
                                     "return number rounded to ndigits after the decimal points
                                    if ndigits is notgiven it returns nearest integer to its input"
                                            """)
                                raw_input=input("Press Enter to continue...")
                            elif a==2:
                                print("built in string fun are ")
                                print("""
                                    1. <str>.join()
                                          if the string based iterator is a string then the <str> is intrested after
                                          every character  of the string eg:-
                                          !!!!In[]:"*".join("Hello")
                                             Out[]:'H*e*l*l*o'
                                    2.<str>.split():
                                             In[]:"I Love python".split()
                                             out[]:['I','Love','python']
                                    3<str>.replace()
                                            In[]:"I Love python".replace("python","programing")
                                            out[]:"I Love programming""")
                            else:
                                f=False
                        raw_input=input("Press Enter to continue...")
                     elif i4==2:
                         q=open("M_FUN.txt")
                         w=q.read()
                         print (w)
                         q.close()
                         del q,w
                         raw_input=input("Press Enter to continue...")
                     elif i4==3:
                         print ("These are the functions defined by programmer.And can be defined using 'def' keyword. ")
                         print ("How to create a function is illustrated in following eample")
                         print()
                         print("def sum(x,y):")
                         print("    r= x+y")
                         print( "    return r")
                         print ("a=input('Enter number1:')")
                         print ("b=input('Enter number 2:)")
                         print ("c=sum(a,b)")
                         print ("print c")
                         raw_input=input("Press Enter to continue...")
                     elif i4==4:
                         con4=False       
                     else:
                        print ("Invalid in put")
