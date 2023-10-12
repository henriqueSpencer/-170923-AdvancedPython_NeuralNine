#  myscripty

def myfuntion(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs['keyone'])

#myfuntion(1,2,3,3, keyone="ola")

# -----------------------------
import sys

if __name__ == '__main__':

    print(sys.argv[0])
    #print(sys.argv[1])

    # python3 [04] ArgumentParsing.py test