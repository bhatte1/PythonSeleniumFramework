from demo import Calculator


class childImpl(Calculator):
    num2 = 200

    def __init__(self,a,b):
        super().__init__(a, b)
        self.a = a
        self.b = b

    def get_complete_Data(self):
        return self.num + self.sum() + self.num2

obj = childImpl(25,50)
print(obj.get_complete_Data())

