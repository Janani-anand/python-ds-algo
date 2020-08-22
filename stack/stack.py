class stack:

    def __init__(self):
        self.stack=[]

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def ispresent(self,item):
        if self.stack:
            return item in self.stack

    def display(self):
        return self.stack

if __name__=='__main__':
    st=stack()
    st.push(1)
    st.push(2)
    st.push(3)
    print(st.display())
    st.pop()
    print(st.peek())
    print(st.size())
    st.push(5)
    print(st.ispresent(2))
    print(st.ispresent(3))
    print(st.display())
