#!/usr/bin/python3.11 env
# Usage: python3 decimal-to.py value [-b] [-o] [-H] [-v]
# Versão 1.0
# Autor: ooclaar 

import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int)
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-O', '--output', action='store_true')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-b', '--binary', action='store_true')
    group.add_argument('-o', '--octal', action='store_true')
    group.add_argument('-H', '--hexa', action='store_true')
    
    args = parser.parse_args()

    if args.binary: 
        divider=2
    elif args.octal:
        divider=8
    else:
        divider=16

    # Definindo variáveis do sistema para que se possa
    # possa realizar os calculos do sistema. 

    rest=0
    dividend=args.number
    debug=args.verbose
    output=args.output
    result=""

    while(True):
        temp = int(dividend) // int(divider)
        rest = int(dividend) % int(divider)
        quociente = int(dividend) - int(rest)
        dividend = temp

        # Realizando modificações de alguns números, caso a opção 
        # hexa tenha sido solicitada. 

        if args.hexa:
            if rest == 10:
                rest="A"
            elif rest == 11:
                rest="B"
            elif rest == 12:
                rest="C"
            elif rest == 13:
                rest="D"
            elif rest == 14:
                rest="E"
            elif rest == 15:
                rest="F"

        # Caso habilitado, mostra todas as operações até chegar
        # no valor do result. 

        if(debug):
            
            print("Dividend value: " + str(dividend))
            print("Divider value: " + str(divider))
            print("Rest value: " + str(rest))
            print("Quotient value: " + str(quociente))
            print("-------------------------------------")

        result = str(result) + str(rest)

        if (dividend==0):
            if(output):
                print(str(result))
            else:
                print("The value " + str(args.number) + " was: " + str(result)[::-1])
            break

if __name__ == "__main__":
    main()