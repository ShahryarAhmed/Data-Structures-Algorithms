#A stack is a very useful data structure that is implemeneted with the computer architecture
#It follows the Last In First Out (LIFO) principle
#It is appropriate to use this type for reversing string
class Stack:
    #initialises the stack empty
    def __init__(self):
        self.items = []
    
    #is used for base cases
    def is_empty(self):
        return len(self.items) == 0
        #return not self.items   <- alternate method
    
    #pushes a new item on to the stack using append
    def push(self, item):
        self.items.append(item)
    
    #pops the newest item off the stack using pop    
    def pop(self):
        return self.items.pop()
    
    #looks at the last item without removing it
    def peak(self):
        return self.items[-1]
    
    #returns the number of items
    def size(self):
        return len(self.items)
    
    #for printing purposes
    def __str__(self):
        return str(self.items)
    
    
#only run the following code below if this is the main file, 
#if file being imported to another file where there is a main then do not run this
# can be thought of like a testing function that doesnt need to be removed
if __name__ == "__main__":
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(3)
    print(s)
    print(s.peak())
    
    
#Reverse a string
if __name__ == "__main__":
    s= Stack()
    string = "learn a lot with linkedin learning"
    
    reversed_string = ""
    
    for i in range(len(string)):
        s.push(string[i])
    
    for i in range(len(string)):
        reversed_string += s.pop()
        
    print(reversed_string)