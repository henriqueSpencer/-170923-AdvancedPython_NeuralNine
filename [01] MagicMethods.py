

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        """
        O python automaticamente deleta cada objeto, aqui vai so add uma print para vermos isso
        """
        print("objeto deletado")

    def __add__(self, outra):
        """
        diz como tratar uma adicao dos objetos
        :param outra:
        :return:
        """
        return Person(self.name+outra.name, 1)

    def __repr__(self):
        """
        Representacao dos objetos
        :return:
        """
        return f"nome:{self.name} idade:{self.age}"

if __name__ == '__main__':
    """
    Magic methods 
    sao os metodos com __
    """

    p1 = Person("mike", 23)
    p2 = Person("juliana", 23)
    p3 = p1+p2
    print('fim')