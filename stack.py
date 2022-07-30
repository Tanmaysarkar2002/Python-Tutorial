def stack():
    def display(stack):
        top = len(stack)
        if top == 0:
            print(" ##Stack Empty## ")
        else:
            print("  The Stack is ",stack)
    def push(stack):
        a=int(input("Enter your desired no:- "))
        stack.append(a)
        return stack
    def pop(stack):
        top=len(stack)
        if top == 0:
            print("##stack empty$$")
        else:
            stack.pop()
            print("New Stack ",stack)
            return stack
    stack = []
    print("""The concept of Stack and Queue is easy to implement in Python.

Stack works on the principle of “Last-in, first-out”. Also, the inbuilt functions in Python make the code short and simple. To add an item to the top of the list, i.e., to push an item, we use append() function and to pop out an element we use pop() function. These functions work quiet efficiently and fast in end operations.

Let’s look at an example and try to understand the working of push() and pop() function:
Example:""")
    while True:
        d = input("Enter what do you want to do \n1:-pop\n2:-push\n3:-display\n:-")
        if d == "1":
            pop(stack)
        elif d == "2":
            stack=push(stack)
        elif d == "3":
            display(stack)
        else:
            print("THANK YOU")
            break
