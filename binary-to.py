#!/usr/bin/python3.11 env
# Usage: python3 binary-to.py value [-b] [-o] [-H] [-v]
# Versão 1.0
# Autor: ooclaar 

import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int)
    parser.add_argument('-v', '--verbose', action='store_true')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--decimal', action='store_true')
    group.add_argument('-o', '--octal', action='store_true')
    group.add_argument('-H', '--hexa', action='store_true')

    args = parser.parse_args()
    number = str(args.number)
    result = 0
    vposicao = 1

    if args.decimal:
        for bit in number[::-1]:
            if bit=='1':
                result=result+vposicao
            elif bit=='0':
                vposicao=vposicao*2
            else:
                result=0
                break
        if result!=0:
            print("The value decimal is: " + str(result))
        else:
            print("The number is not binary.")

if __name__ == "__main__":
    main()