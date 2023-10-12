# ex seq 1 to 90000
# é utilizado para executar sequencias
# lase execution


"""
são uma forma especial de criar iteráveis
Eles são utilizados para criar sequências de valores sob demanda, em vez de gerar todos os valores de uma vez e armazená-los na memória.

Funções Geradoras: Um generator é criado utilizando funções geradoras. Uma função geradora é definida usando a palavra-chave yield em vez de return. Quando uma função geradora é chamada, ela não executa imediatamente, em vez disso, retorna um objeto generator.
Exemplo de função geradora:
python
Copy code
def gerador_simples():
    yield 1
    yield 2
    yield 3

meu_generator = gerador_simples()
Iteração Preguiçosa: Os generators geram valores sob demanda, à medida que você itera sobre eles. Isso significa que eles são especialmente úteis quando você precisa lidar com sequências de valores potencialmente grandes, economizando memória.
python
Copy code
for valor in meu_generator:
    print(valor)
O código acima imprimirá os valores 1, 2 e 3 à medida que forem solicitados, sem armazená-los todos na memória de uma só vez.

étodo next(): Você pode obter o próximo valor de um generator usando a função next(). Quando todos os valores já foram gerados, ele levanta uma exceção StopIteration.
python
Copy code
print(next(meu_generator))

"""

# Exemplo
# Leitura de Arquivos Grandes:
# Ao ler arquivos grandes linha por linha, você pode usar um generator para evitar carregar o arquivo inteiro na memória. Isso é especialmente útil para logs, arquivos de registro ou qualquer arquivo grande.
# python
# Copy code
def ler_arquivo_arquivo_grande(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            yield linha

# Exemplo interacao com libs
import requests

def solicitar_paginas_api(url):
    while url:
        response = requests.get(url)
        data = response.json()
        yield data
        url = data.get('next_page')