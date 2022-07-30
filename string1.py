def string():
                con3=True
                while con3:
                    print ("Strings :-A data type are any number of valid characters into a set of quotion marks.")
                    print ("Operations that can be performed with string are::")
                    print ("1.Traversing of string")
                    print ("2.String opeartors  on string")
                    print ("3.String Functions")
                    print ("4.Slicing a string")
                    print ("5.Get Back to previous menu")
                    i3=eval(input("Enter your choice(1-5):"))
                    if i3=="":
                        print("no input given")
                    if i3==1:
                        print ("Traversing can be performed in a following way")
                        a="Python"
                        print (">>>a='Python'")
                        print (">>>for i in a:")
                        print ("      print i,'-'" )
                        print ("_______ OUTPUT OF ABOVE PROGRAM ________")
                        for i in a :
                            print( i,"-",)
                        print()
                        print (" *** ")
                        raw_input=input("Press Enter to Continue")
                    elif i3==2:
                        print( "String operators are")
                        print("1.String Concatenation operator (+):")
                        print("  eg.")
                        print("     'ram' + 'shayam'")
                        print("  will result into")
                        print("     'ramshayam' ")
                        print("2. String replication operator  (*):")
                        print("  eg.")
                        print("     'DSS'*3")
                        print("  will result into ")
                        print("     'DSSDSSDSS'")
                        print("3. Mermbership operator:")
                        print("in : Returns True if sub string  exist in given string, otherwise False")
                        print("not in: Returns True if sub string   not exist in given string, oterwise False")
                        print(" eg.")
                        print("   >>> 'a' in 'ram'")
                        print("       True")
                        print("   >>> 'a' not in 'ram'")
                        print("4.Comparison operator(<,>,>=,<=,==,!=):")
                        print(" eg.")
                        print("   'a'=='a' will give True")
                        print(" 'a==b' will give false")
                        raw_input=input("Press Enter to Continue")
                    elif i3==3:
                        q=open("S_FUN.txt")
                        w=q.read()
                        print (w)
                        del q,w
                        raw_input=input("Press Enter to Continue")
                    elif i3==4:
                        print ("Slicing a string can be performed  as follow,")
                        print()
                        print (">>a=ramayan")
                        a='ramayan'
                        print (">>>print a[0:3]")
                        print ("output>>>",a[0:3])
                        raw_input=input("Press Enter to Continue")
                    elif i3==5:
                        con3=False
                    else:
                        print( "INvalid input !!!!!!!!!!!")
            
