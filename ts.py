""" class Person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender """


""" class Person:
    def __init__(self,name,age):
        print("자동으로 불려옴")
        self.name = name
        self.age = age        
    def __str__(self):
        return '이클래스를 하나의 문자열로 표현하면 이거'


aiden = Person('aiden', 23)
isaac = Person('isaac', 19) """
# print(aiden > isaac) #어떤것을 기준으로 비교해야할지 모름

""" class Person:
    count = 0
    def __init__(self.name):
        self.name = name
        person.count += 1

    @classmethod
    def number_of_population(cls):
        print(f'인구수는{cls.count}')

person1 = Person('아이유')
person2 = Person('이찬혁')

Person.number_of_population()
person1.number_of_population()
person2.number_of_population() """