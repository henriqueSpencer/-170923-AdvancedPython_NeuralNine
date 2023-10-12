
#---- [00] Decorater de funcoes sem parametros ----
def mydecorator(function):
    def wrapper():
        function()
        print("Ola")

    return wrapper

def hello_world():
    print("Hello World")

@mydecorator
def hello_world2():
    print("Hello World")
#---------------------------------------------

#---- [01] Decorater de funcoes Com parametros ----
def mydecorator2(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        print("Ola")

    return wrapper
@mydecorator2
def hello_pessoa(nome):
    print(f"Hello {nome}")

#---------------------------------------------

#---- [02] Decorater exemplo Logg ----
def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            print(f"{fname}: return value {value}")
            f.write(f"{fname}: return value {value}")
        return value

    return wrapper

@logged
def add(x, y):
    return x + y

#---------------------------------------------

#---- [02] Decorater exemplo Logg ----
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} levou o tempo de execução de: {after-before}")
        return value

    return wrapper

@timed
def myfunction(x):
    result =1
    for i in range(x):
        result *= i
    return result


if __name__ == "__main__":
    #mydecorator(hello_world)() # [00]

    # hello_pessoa("Joao") # [01]

    # add(1,2)# [02]

    myfunction(11) # [03]