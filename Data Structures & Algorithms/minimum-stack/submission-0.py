class MinStack:

    def __init__(self):
        self.st=[]
        self.minimum=[]

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.minimum or val<=self.minimum[-1]:
            self.minimum.append(val)
        
    def pop(self) -> None:
        if self.st[-1]==self.minimum[-1]:
            self.minimum.pop()
        self.st.pop()
        
    def top(self) -> int:
        return self.st[-1]
        
    def getMin(self) -> int:
        return self.minimum[-1]
        
