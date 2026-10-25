class MinStack:
    # 1, 2, 0, 3
    # 1, 2, 0, 3
    # 1, 0

    # 1, 2, 0
    # 1, 0
    # 1, 2
    # 1, 
    # 1
    # 1

    #
    # 


    def __init__(self):

    # 2 stacks
    # 1 is a normal stack
    # 1 is a monotonic min stack - bottom elements, large, top elements small
    # push: push to the top of the normal stack, while 
    # the 
        self.st = []
        self.min_st = []
        

    def push(self, val: int) -> None:
        self.st.append(val)
        # dont want to have only one instance of min eleemnt in min stack
        # but multiple in the main stack
        if not self.min_st or self.min_st[-1] >= val:
            self.min_st.append(val)
        

    def pop(self) -> None:
        popped = self.st.pop()
        if self.min_st[-1] == popped:
            self.min_st.pop()


    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.min_st[-1]
