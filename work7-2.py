# class Doggy:
#     birth_of_dog=0
#     curren_dog=0
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#         Doggy.birth_of_dog += 1
#         Doggy.curren_dog += 1

#     def bark(self):
#         print("멍멍")
    
#     def get_status(self):
#         print(birth_of_dogs)
#         print(num_of_dog)


# class Doggy:
#     num_of_dogs = 0
#     birth_of_dogs = 0

#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#         print(f'{self.name}이 태어남')
#         Doggy.num_of_dogs += 1
#         Doggy.birth_of_dogs += 1

#     def bark(self):
#         print(f"{self.name}이 멍멍")

#     def __del__(self):
#         print(f'{self.name}이 죽음')
    

# dog1 = Doggy('해피','말티')
# dog2 = Doggy('오즈','요쿠')


class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, species):
        self.name = name
        self.species = species
        print(f'{self.name}이 태어남')
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def bark(self):
        print(f"{self.name}이 멍멍")

    def __del__(self):
        print(f'{self.name}이 죽음')
        self.num_of_dogs -= 1

    def get_status(self):
        print(self.num_of_dogs,self.birth_of_dogs)   #dog1.get_status()로 호출

    @classmethod
    def get_status(cls):
        print(cls.num_of_dogs,cls.birth_of_dogs)   #Doggy.get_status()로 호출

dog1 = Doggy('해피','말티')
dog2 = Doggy('오즈','요쿠')
Doggy.get_status()
dog2.bark()