def queue():
    print("""Implementing queue is a bit different. Queue works on the principle of “First-in, first-out”.
Time plays an important factor here. We saw that during the implementation of stack we used append() and pop() function
which was efficient and fast because we inserted and popped elements from the end of the list, but in queue when insertion
and pops are made from the beginning of the list, it is slow. This occurs due to the properties of list,
which is fast at the end operations but slow at the beginning operations, as all other elements have to
be shifted one by one. So, we prefer the use of collections.deque over list, which was specially designed
to have fast appends and pops from both the front and back end.

Let’s look at an example and try to understand queue:""")
    raw_input=input("press enter to continue")
    def display(Q):
        if len(Q)==0:
            print('Queue is empty')
        else:
            print(Q)
    def push(Q,items):   
        Q.append(items)
    def pop():
        if Q==[]:
            print('No elements are present in the Queue') 
        else:
            Q.pop(0)
    Q=[]
    while True:
        print('\t','\t','\t','\t',"**MENU**")
        print()
        print('\t','\t','\t',"Given Choicices are :")
        print('\t','\t','\t','\t',"1.DISPLAY")
        print('\t','\t','\t','\t',"2.PUSH")
        print('\t','\t','\t','\t',"3.POP")
        print('\t','\t','\t','\t',"4.EXIT")
        print()
        print('\t','\t','\t','Enter your choice:-')
        c=eval(input())
        if c==2:
            items=eval(input('enter element:-'))
            push(Q,items)
        elif c==3:
            pop()
        elif c==1:    
            display(Q)
        elif c==4:
            print("Aborting program.......")
            break
        
