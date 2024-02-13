#!/usr/bin/python3.11 env
# Usage: python3 hexa-to.py value [-b] [-o] [-H] [-v]
# Versão 1.0
# Autor: ooclaar

import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('number')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-O', '--output', action='store_true')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-b', '--binary', action='store_true')
    group.add_argument('-o', '--octal', action='store_true')
    group.add_argument('-d', '--decimal', action='store_true')
    
    args = parser.parse_args()
    debug = args.verbose

    # Definição de Dados Estáticos

    hex_to_bin = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

    if args.binary:

        binario = ""

        number = str(args.number)
        for bit in number:
            binario = binario + hex_to_bin[bit]

        print(f"O valor em binário é: {binario}")
    
    if args.octal:

        bin_to_octal = {
            '000': '0',
            '001': '1',
            '010': '2',
            '011': '3',
            '100': '4',
            '101': '5',
            '110': '6',
            '111': '7'
        }

        octal = ""
        binario = ""

        number = str(args.number)

        for bit in number:
            binario = binario + hex_to_bin[bit]

        if ((len(binario) % 3)!=0):
            
            if debug:
                print(f"O valor de binário é {binario}")
                print(f"O tamanho do binário é: {len(binario)}")
            
            while (True):
                if ((len(binario) % 3)==0):
                    if debug:
                        print(f"O número passado foi modificado para: {binario}.")
                    break
                else:
                    binario = "0" + str(binario)
                    if debug:
                        print(f"O valor de binário é {binario}")
                        print(f"O tamanho do binário é: {len(binario)}")

        for i in range(0, len(binario),3):
            part = str(binario[i:i+3])    
            octal = octal + bin_to_octal[part]
        
        if (octal[0] == '0'):
            octal = octal[1:]

        print(f"O valor em octal é: {octal}")

    if args.decimal:

        number = str(args.number)
        contador = 0
        total = 0

        for bit in number[::-1]:
            
            # Correção das letras para números.

            if bit == "A":
                bit = "10"
            elif bit == "B":
                bit = "11"
            elif bit == "C":
                bit = "12"
            elif bit == "D":
                bit = "13"
            elif bit == "E":
                bit = "14"
            elif bit == "F":
                bit = "15"

            total = int(total) + int(bit) * 16 ** contador

            contador+=1

        print(f"O valor em decimal é {str(total)}")

if __name__ == "__main__":
    main()