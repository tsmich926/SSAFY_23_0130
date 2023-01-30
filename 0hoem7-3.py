#계산기
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        if b == 0: 
            print('0으로 나눌수없음')
    
    def add(self,a, b):
        return a + b 
    
    def substract(self,a, b):
        return a - b

    def multuply(self, a, b):
        return a * b
    
    def divide(self,a, b):
        return a / b

c = Calculator(3,4)
print(c.add(5, 0))
