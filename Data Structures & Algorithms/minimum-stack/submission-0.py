class MinStack:

    def __init__(self):
        self.val = []
        self.miN = []

    def push(self, val: int) -> None:
        self.val.append(val)
        if not self.miN:
            self.miN.append(val)
        else:
            curr_min = self.miN[-1]
            self.miN.append(min(val, curr_min))            

    def pop(self) -> None:
        self.val.pop()
        self.miN.pop()

    def top(self) -> int:
        return self.val[-1]

    def getMin(self) -> int:
        return self.miN[-1]