class Fifo(list):
    def __init__(self, maxlen: int = 1):
        super().__init__()
        self.maxlen: int = maxlen

    def is_full(self) -> bool:
        return len(self) == self.maxlen

    def append(self, x):
        one = None
        if self.is_full():
            one = self.pop(0)
        super().append(x)
        return one
