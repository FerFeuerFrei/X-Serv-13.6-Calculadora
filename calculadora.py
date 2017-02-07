#import sys

#exit(0)

#if sys.argv[2] == "+":
#    print(sys.argv[1] + sys.argv[3])

# FORMA 1

import sys

# _: lo tiro a la basura.

if len(sys.argv) != 4:
    sys.exit("Usage: python3 calculadora.py operacion operando1 operando2")
    
print(sys.argv)
    
_, operacion, operando1, operando2 = sys.argv


try:
    operando1 = float(operando1)
    operando2 = float(operando2)
except ValueError:
    sys.exit("Los operandos han de ser floats. Gracias")

if operacion == "suma":
    print(operando1 + operando2)
elif operacion == "div":
    try:
        print(operando1 / operando2)
    except ZeroDivisionError:
        sys.exit
        


