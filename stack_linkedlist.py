class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.head = None
 
    def push(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
 
    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped
    def display(self):
        if self. head is None:
            print("Stack empty")
        else:
             n = self.head
             print(n,end=' ')
             while n is not None:
                 print("-->"+str(n.data)+"("+str(n.next)+")",end=' ')
                 n = n.next
             print()
            
a_stack = Stack()
while True:
    print('1. push <value>')
    print('2. pop')
    print('3.display')
    print('4. quit')
    do = input("Enter your choice:" )
 
    operation = do
    if operation == '1':
        num=int(input("Enter the value"))
        a_stack.push(num)
    elif operation == '2':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == '3':
        print(a_stack.display())
    elif operation == '4':
        break
