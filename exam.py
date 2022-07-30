count=0
def basic():
        global count
        print("""Q1->What will be the output of the following code :
        print type(type(int))""")
        print("your options are \n A->type 'int'\n B->type'type'\n C->error\n D->0\n ")
        answer=input("Apka answer:")
        if answer.lower() =='a':
               count+=1
               import os
               os.system('cls')
        print("""Q2->What will be the output of the following code :
        print 9//2""")
        print("your options are \n A->4.5\n B->4.0\n C->error\n D->4\n ")
        answer=input("Apka answer:")
        if answer.lower() =='b':
               count+=1
               import os
               os.system('cls')
        print("""Q4->Given a string s = “Welcome”, which of the following code
        is incorrect? :""")
        print("your options are \n A->print(s[0])\n B->print(s.lower())\n C-> no error\n D->print(s.strip())\n ")
        answer=input("Apka answer:")
        if answer.lower() =='c':
               count+=1
               import os
               os.system('cls')
        
        print("""Q5->What will be the output of the following code :
        print (0.1 + 0.2 == 0.3)""")
        print("your options are \n A->true\n B->False\n C->error\n D->0\n ")
        answer=input("Apka answer:")
        if answer.lower() =='b':
               count+=1
               import os
               os.system('cls')

        print("""Q6->In Python 3,
        the maximum value for an integer is 263 - 1:""")
        print("your options are \n A->true\n B->False\n C->error\n ")
        answer=input("Apka answer:")
        if answer.lower() =="b":
               count+=1
               import os
               os.system('cls')
        print("""Q7->Which of the following are valid ways
        to specify the string literal foo'bar in Python:""")
        print("""your options are \n A->'''foo'bar'''\n
              B->'foo''bar'\n C->'foo"bar'\n""")
        answer=input("Apka answer:")
        if answer.lower() =="a":
               count+=1
               import os
               os.system('cls')
        return count
        
        
        
