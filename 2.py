#리스트는 파이썬이 이미 만든 클래스
a = [2, 3, 4]
a = list() 

#person은 사용자가 만든 클래스
class Person:
    cnt = 0 #1번으로 실행
    def __init__(self, name): 
        name1 = 'aaa'   
        self.name = name

P = Person("길동") 
print(P.name)
# print(name1) #실행안됨



class Person:
    cnt = 0 
    @classmethod
    def class_method(cls):

    def __init__(self, name): 
        name1 = 'aaa'   
        self.name = name

    def instance_method(self):

P = Person("길동") 
print(P.name)
P.instance_method() #P가 자동으로 넘어감
Person.class_method() #Person이 자동으로 넘어감
# P.class_method()
# Person.instance_method()  #인스턴스메소드에 뭘 넣어줘야 할지 모름,사용하지 말자


#왜 오류가 날까?
class Person:
    def i_func(d):
        return d+5

p = Person()
print(p.i_func(3))
#def i_func(d): 를 def i_func(self,d):로 고쳐준다.


p = Person()
print('p',id(p))
print(p.i_func(3))
#두개의 아이디 값이 같다. 