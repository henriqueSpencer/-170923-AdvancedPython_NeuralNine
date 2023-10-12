
class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name = value


if __name__ == '__main__':


    p1 = Person("mike", 23, 'm')
    print(p1.Name)