def loop():
                con5=True
                while con5:
                    print( "Python offers  2  type of loop statement")
                    print ("1. The for loop")
                    print ("2. The while loop")
                    print ("3. Get back to previous menu"  )
                    i4=eval(input("Enter your choice(1-3):"))
                    if i4==1:
                        print( "The general form of 'for loop' is as given below:")
                        print (" for <variable> in <sequence> :")
                        print ("     statements_to_repeat")
                        print ("eg.")
                        print ("    for element in [10,15,20,25]:")
                        print ("        print (element +2),")
                        print ("Or for loop can be also used wiht range()function")
                        print ("eg.")
                        print ("   for val in range(3,10):")
                        print ("      print val")
                        raw_input=input("press enter to continue")
                    elif i4==2:
                        print( "The general form of while loop is given below")
                        print (" while <logicalExpression>:",0)
                        print ("    loop-body")
                        raw_input=input("press enter to continue")
                    elif i4==3:
                        con5=False
                    else:
                        print( "Invalid Input")
                        raw_input=input("press enter to continue")
