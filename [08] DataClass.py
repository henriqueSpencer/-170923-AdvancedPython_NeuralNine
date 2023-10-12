from dataclasses import dataclass, field

'''
Não preciso prover um construtur, 
não preciso prover um metodo de representação
não preciso prover um metodo de comparação
Ele ja vai prover tudo isso para mim !
'''

@dataclass
class Pessoa:
    nome: str
    idade: int
    dinheiro: float = field(default=0.0)

    def __post_init__(self):
        self.nome = self.nome.upper()


if __name__ == '__main__':
    p1 = Pessoa("mike", 23)
    p2 = Pessoa("miked", 22)
    print(p1)