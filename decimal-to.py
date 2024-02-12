#!/usr/bin/python3.11 env
# Usage: python3 decimal-to.py value [-b] [-o] [-H] [-v]
# Versão 1.0
# Autor: ooclaar 

import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int)
    parser.add_argument('-v', '--verbose', action='store_true')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-b', '--binary', action='store_true')
    group.add_argument('-o', '--octal', action='store_true')
    group.add_argument('-H', '--hexa', action='store_true')
    
    args = parser.parse_args()

    if args.binary == None and args.octal == None and args.hexa == None:
        print("The attribute is not defined, choose the --binary, --octal, or --hexa parameter.")
    else:
        if args.binary: 
            divisor=2
        elif args.octal:
            divisor=8
        else:
            divisor=16

        # Definindo variáveis do sistema para que se possa
        # possa realizar os calculos do sistema. 

        resto=0
        dividendo=args.number
        debug=args.verbose
        resultado=""

        while(True):
            temp = int(dividendo) // int(divisor)
            resto = int(dividendo) % int(divisor)
            quociente = int(dividendo) - int(resto)
            dividendo = temp

            # Realizando modificações de alguns números, caso a opção 
            # hexa tenha sido solicitada. 

            if args.hexa:
                if resto == 10:
                    resto="A"
                elif resto == 11:
                    resto="B"
                elif resto == 12:
                    resto="C"
                elif resto == 13:
                    resto="D"
                elif resto == 14:
                    resto="E"
                elif resto == 15:
                    resto="F"

            # Caso habilitado, mostra todas as operações até chegar
            # no valor do resultado. 

            if(debug):
                
                print("Valor do dividendo: " + str(dividendo))
                print("Valor do divisor: " + str(divisor))
                print("Valor do resto: " + str(resto))
                print("Valor do quociente: " + str(quociente))
                print("-------------------------------------")

            resultado = str(resultado) + str(resto)

            if (dividendo==0):
                print("O valor de " + str(args.number) + " ficou: " + str(resultado)[::-1])
                break

if __name__ == "__main__":
    main()